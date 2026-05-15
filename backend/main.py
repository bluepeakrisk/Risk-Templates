"""
SME Risk Register — Backend API
Generates customised Excel risk registers via the Blue Peak Risk library.

This is a thin FastAPI wrapper around build_summary_v3.py. The builder lives
in this same directory and is invoked via subprocess with a JSON config file.
"""
import os
import json
import datetime
import subprocess
import tempfile
from pathlib import Path
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel, Field

# ── Paths ─────────────────────────────────────────────────────────────
BACKEND_DIR  = Path(__file__).parent
BUILDER_PATH = BACKEND_DIR / "build_summary_v3.py"

# ── Warm up: pre-run builder once at startup to import all library modules ──
# This eliminates cold-start delays on the first real user request.
# Runs in background so it doesn't block startup.
import threading
def _warmup():
    try:
        import tempfile as _t
        _fd, _out = _t.mkstemp(suffix=".xlsx", prefix="bpr_warmup_")
        os.close(_fd)
        subprocess.run(
            ["python", str(BUILDER_PATH), "--industry", "PROF", "--npat", "1000000", "--out", _out],
            capture_output=True, text=True, cwd=str(BACKEND_DIR), timeout=120,
        )
        try: os.remove(_out)
        except: pass
    except Exception:
        pass  # warmup failure is non-fatal

threading.Thread(target=_warmup, daemon=True).start()

# ── Industry name → 4-letter code mapping ─────────────────────────────
# Maps the strings sent by the frontend dropdown to the codes the builder uses.
# The frontend sends the full label including bracketed descriptions.
# Fallback: if no exact match, try prefix matching on the first word.
INDUSTRY_MAP = {
    # Professional Services
    "Professional Services (Legal, Consulting, Accounting)": "PROF",
    "Professional Services":                                  "PROF",
    "Recruitment / HR Services":                              "PROF",
    "Marketing / Creative Agencies":                          "PROF",
    "Cybersecurity Services":                                 "PROF",
    "Media / Publishing / Advertising":                       "PROF",
    "Real Estate / Property Management":                      "PROF",
    "Hospitality / Tourism / Travel":                         "PROF",

    # Financial Services
    "Financial Services (Banking, Insurance, Investment)":    "FINS",
    "Financial Services":                                     "FINS",

    # Technology
    "Technology / SaaS / Software":                           "TECH",
    "Technology and SaaS":                                    "TECH",
    "Technology & SaaS":                                      "TECH",
    "Technology":                                             "TECH",
    "Telecommunications":                                     "TECH",

    # Healthcare
    "Healthcare (Hospitals / Clinics)":                       "HCAR",
    "Healthcare and Life Sciences":                           "HCAR",
    "Healthcare & Life Sciences":                             "HCAR",
    "Healthcare":                                             "HCAR",
    "Aged Care / Disability Services":                        "HCAR",
    "Childcare / Early Learning":                             "HCAR",
    "Pharmaceuticals / Biotechnology":                        "HCAR",

    # Retail
    "Retail / E-commerce":                                    "RETL",
    "Retail and Consumer":                                    "RETL",
    "Retail & Consumer":                                      "RETL",
    "Retail":                                                 "RETL",
    "Wholesale / Distribution":                               "RETL",
    "Logistics / Transport / Freight":                        "RETL",
    "Import / Export":                                        "RETL",
    "Consumer Goods / FMCG":                                  "RETL",
    "Food & Beverage":                                        "RETL",

    # Industrial / Manufacturing
    "Manufacturing (Light)":                                  "INDU",
    "Manufacturing (Heavy / Industrial)":                     "INDU",
    "Manufacturing and Industrial":                           "INDU",
    "Manufacturing":                                          "INDU",
    "Industrial":                                             "INDU",
    "Construction / Engineering":                             "INDU",
    "Mining / Resources":                                     "INDU",
    "Oil & Gas":                                              "INDU",
    "Energy / Utilities":                                     "INDU",
    "Renewable Energy":                                       "INDU",
    "Water / Wastewater":                                     "INDU",
    "Agriculture / Aquaculture / Forestry":                   "INDU",
    "Chemicals / Petrochemicals":                             "INDU",
    "Automotive":                                             "INDU",
    "Aerospace / Defence":                                    "INDU",

    # Public Sector / Not-for-profit
    "Government (Federal / State)":                           "PUBL",
    "Government (Local Council)":                             "PUBL",
    "Not-for-profit / Charity":                               "PUBL",
    "Religious / Community Organisations":                    "PUBL",
    "Public Sector and Not-for-Profit":                       "PUBL",
    "Public Sector & Not-for-Profit":                         "PUBL",
    "Public Sector":                                          "PUBL",
    "Not-for-Profit":                                         "PUBL",
    "Government":                                             "PUBL",
    "Education (K-12)":                                       "PUBL",
    "Higher Education / Universities":                        "PUBL",
    "Sports / Recreation":                                    "PUBL",
    "Arts / Culture":                                         "PUBL",
    "Other":                                                  "PROF",  # default fallback
}

# ── FastAPI app ───────────────────────────────────────────────────────
app = FastAPI(
    title="Blue Peak Risk Register API",
    description="Generate tailored risk registers for SMEs",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Request models ────────────────────────────────────────────────────
class OrganisationConfig(BaseModel):
    name: str = "SME"
    industry: str = "Professional Services"
    size: str = "Medium (20-199 staff)"
    country: str = "Australia"
    cycle: str = "Quarterly"
    notes: Optional[str] = ""


class FinancialConfig(BaseModel):
    npat: float = 2_000_000
    currency: str = "AUD"
    # 5 cumulative thresholds as fractions of NPAT for impact bands 1-5
    fin_pcts: List[float] = [0.01, 0.05, 0.15, 0.30, 1.00]


class RAGThreshold(BaseModel):
    label: str
    min: int
    max: int


class RegisterConfig(BaseModel):
    organisation: OrganisationConfig = Field(default_factory=OrganisationConfig)
    financial: FinancialConfig = Field(default_factory=FinancialConfig)
    focus_areas: List[str] = []
    # 4-tier RAG (Low/Moderate/High/Very High). Score ranges configurable;
    # labels are conventionally fixed for the colour mapping to work.
    rag_thresholds: List[RAGThreshold] = [
        RAGThreshold(label="Low",       min=1,  max=3),
        RAGThreshold(label="Moderate",  min=4,  max=9),
        RAGThreshold(label="High",      min=10, max=15),
        RAGThreshold(label="Very High", min=16, max=25),
    ]
    # "max" (default), "avg", or "weighted" (treated as max for now)
    scoring_method: str = "max"


# ── Health endpoints ──────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "ok", "service": "Blue Peak Risk Register API", "version": "2.0.0"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "builder_present": BUILDER_PATH.exists(),
    }


# ── Main endpoint ─────────────────────────────────────────────────────
@app.post("/generate")
def generate_register(config: RegisterConfig):
    """Generate a customised Excel risk register and return as a download."""
    # Map industry label to code — exact match first, then partial
    industry_label = config.organisation.industry
    industry_code = INDUSTRY_MAP.get(industry_label)
    if industry_code is None:
        # Partial match: check if any key starts with the sent label or vice versa
        for key, code in INDUSTRY_MAP.items():
            if industry_label.lower().startswith(key.lower().split("(")[0].strip().lower()):
                industry_code = code
                break
    if industry_code is None:
        raise HTTPException(
            status_code=400,
            detail=(f"Unknown industry '{industry_label}'. "
                    f"Please select from the dropdown options."),
        )

    # Build output path (will hold the generated workbook)
    out_fd, out_path = tempfile.mkstemp(suffix=".xlsx", prefix="bpr_register_")
    os.close(out_fd)

    # Build config JSON for the builder subprocess
    # Use model_dump() for pydantic v2, fall back to dict() for pydantic v1
    def _dump(obj):
        return obj.model_dump() if hasattr(obj, 'model_dump') else obj.dict()

    builder_config = {
        "industry_code": industry_code,
        "output_path": out_path,
        "organisation": _dump(config.organisation),
        "financial": _dump(config.financial),
        "focus_areas": config.focus_areas,
        "rag_thresholds": [_dump(t) for t in config.rag_thresholds],
        "scoring_method": config.scoring_method,
    }

    # Write config to a temporary JSON file
    cfg_fd, cfg_path = tempfile.mkstemp(suffix=".json", prefix="bpr_cfg_")
    os.close(cfg_fd)
    with open(cfg_path, "w") as f:
        json.dump(builder_config, f)

    # Invoke the builder
    try:
        result = subprocess.run(
            ["python", str(BUILDER_PATH), "--config", cfg_path],
            capture_output=True,
            text=True,
            cwd=str(BACKEND_DIR),
            timeout=120,  # 2 minutes — allows for Railway cold starts
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Workbook generation timed out (>120s).")
    finally:
        # Clean up the config file regardless
        try:
            os.remove(cfg_path)
        except OSError:
            pass

    if result.returncode != 0:
        # Print full stderr to Railway logs (visible in deploy log stream)
        print(f"[ERROR] Builder failed for industry={industry_code}")
        print(f"[ERROR] STDOUT: {result.stdout[-1000:]}")
        print(f"[ERROR] STDERR: {result.stderr[-2000:]}")
        raise HTTPException(
            status_code=500,
            detail=f"Builder failed: {result.stderr[-1000:] if result.stderr else result.stdout[-1000:] or 'no output'}",
        )

    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        raise HTTPException(status_code=500, detail="Builder produced no output file.")

    # Read file into memory then delete temp file - avoids FileResponse path issues
    with open(out_path, "rb") as f:
        file_bytes = f.read()
    try:
        os.remove(out_path)
    except OSError:
        pass

    # Build response filename
    org_slug = config.organisation.name.replace(" ", "_").replace("/", "_") or "Register"
    today = datetime.date.today().isoformat()
    download_name = f"BluePeakRisk_{org_slug}_{today}.xlsx"

    return StreamingResponse(
        iter([file_bytes]),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f'attachment; filename="{download_name}"'},
    )


@app.get("/debug")
def debug_builder():
    """Run builder with minimal test config and return full stdout/stderr.
    Remove this endpoint once the deployment is stable."""
    import tempfile, json, subprocess
    out_fd, out_path = tempfile.mkstemp(suffix=".xlsx", prefix="bpr_debug_")
    os.close(out_fd)
    test_cfg = {
        "industry_code": "FINS",
        "output_path": out_path,
        "organisation": {"name": "Debug", "industry": "Financial Services", "size": "", "country": "", "cycle": "", "notes": ""},
        "financial": {"npat": 1000000, "currency": "AUD", "fin_pcts": [0.01, 0.05, 0.15, 0.30, 1.00]},
        "focus_areas": [],
        "rag_thresholds": [{"label":"Low","min":1,"max":3},{"label":"Moderate","min":4,"max":9},{"label":"High","min":10,"max":15},{"label":"Very High","min":16,"max":25}],
        "scoring_method": "max",
    }
    cfg_fd, cfg_path = tempfile.mkstemp(suffix=".json", prefix="bpr_dbg_cfg_")
    os.close(cfg_fd)
    with open(cfg_path, "w") as f:
        json.dump(test_cfg, f)
    result = subprocess.run(
        ["python", str(BUILDER_PATH), "--config", cfg_path],
        capture_output=True, text=True, cwd=str(BACKEND_DIR), timeout=90,
    )
    try: os.remove(cfg_path)
    except: pass
    file_size = os.path.getsize(out_path) if os.path.exists(out_path) else 0
    try: os.remove(out_path)
    except: pass
    return {
        "returncode": result.returncode,
        "builder_path": str(BUILDER_PATH),
        "builder_exists": BUILDER_PATH.exists(),
        "backend_dir": str(BACKEND_DIR),
        "backend_dir_contents": os.listdir(str(BACKEND_DIR)),
        "stdout": result.stdout[-3000:],
        "stderr": result.stderr[-3000:],
        "output_file_size_bytes": file_size,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
