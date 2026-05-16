"""
Blue Peak Risk — Backend API
Generates tailored Excel risk registers via build_summary_v3.py.
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
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

# ── Paths — use abspath so they resolve correctly however uvicorn is invoked ──
BACKEND_DIR  = Path(os.path.abspath(__file__)).parent
BUILDER_PATH = BACKEND_DIR / "build_summary_v3.py"

# ── Industry label → 4-letter code ────────────────────────────────────────────
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
    # Industrial
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
    # Public / NFP
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
    "Other":                                                  "PROF",
}

# ── App ────────────────────────────────────────────────────────────────────────
app = FastAPI(title="Blue Peak Risk API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Request models ─────────────────────────────────────────────────────────────
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
    fin_pcts: List[float] = [0.01, 0.05, 0.15, 0.30, 1.00]

class RAGThreshold(BaseModel):
    label: str
    min: int
    max: int

class RegisterConfig(BaseModel):
    organisation: OrganisationConfig = Field(default_factory=OrganisationConfig)
    financial: FinancialConfig = Field(default_factory=FinancialConfig)
    focus_areas: List[str] = []
    rag_thresholds: List[RAGThreshold] = [
        RAGThreshold(label="Low",       min=1,  max=3),
        RAGThreshold(label="Moderate",  min=4,  max=9),
        RAGThreshold(label="High",      min=10, max=15),
        RAGThreshold(label="Very High", min=16, max=25),
    ]
    scoring_method: str = "max"

# ── Helpers ────────────────────────────────────────────────────────────────────
def _dump(obj):
    """Pydantic v1/v2 compatibility."""
    return obj.model_dump() if hasattr(obj, "model_dump") else obj.dict()

def _map_industry(label: str) -> str:
    """Map frontend industry label to 4-letter code. Falls back to prefix match."""
    code = INDUSTRY_MAP.get(label)
    if code:
        return code
    label_lower = label.lower()
    for key, val in INDUSTRY_MAP.items():
        if label_lower.startswith(key.lower().split("(")[0].strip()):
            return val
    return "PROF"  # final fallback

# ── Endpoints ──────────────────────────────────────────────────────────────────
@app.get("/")
def root():
    return {"status": "ok", "service": "Blue Peak Risk API", "version": "2.0.0"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "builder_present": BUILDER_PATH.exists(),
    }

@app.post("/generate")
def generate_register(config: RegisterConfig):
    """Generate a tailored Excel risk register and return as a download."""

    industry_code = _map_industry(config.organisation.industry)

    # Write output and config to temp files
    out_fd, out_path = tempfile.mkstemp(suffix=".xlsx", prefix="bpr_")
    os.close(out_fd)

    builder_config = {
        "industry_code": industry_code,
        "output_path": out_path,
        "organisation": _dump(config.organisation),
        "financial": _dump(config.financial),
        "focus_areas": config.focus_areas,
        "rag_thresholds": [_dump(t) for t in config.rag_thresholds],
        "scoring_method": config.scoring_method,
    }

    cfg_fd, cfg_path = tempfile.mkstemp(suffix=".json", prefix="bpr_cfg_")
    os.close(cfg_fd)
    try:
        with open(cfg_path, "w") as f:
            json.dump(builder_config, f)

        result = subprocess.run(
            ["python", str(BUILDER_PATH), "--config", cfg_path],
            capture_output=True,
            text=True,
            cwd=str(BACKEND_DIR),
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Generation timed out. Please try again.")
    finally:
        try: os.remove(cfg_path)
        except OSError: pass

    if result.returncode != 0:
        print(f"[ERROR] industry={industry_code} stdout={result.stdout[-500:]} stderr={result.stderr[-500:]}")
        raise HTTPException(
            status_code=500,
            detail=f"Generation failed: {(result.stderr or result.stdout)[-800:]}",
        )

    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        raise HTTPException(status_code=500, detail="Builder produced no output.")

    # Read into memory and stream back
    with open(out_path, "rb") as f:
        file_bytes = f.read()
    try: os.remove(out_path)
    except OSError: pass

    org_slug = config.organisation.name.replace(" ", "_").replace("/", "_") or "Register"
    filename = f"BluePeakRisk_{org_slug}_{datetime.date.today().isoformat()}.xlsx"

    return StreamingResponse(
        iter([file_bytes]),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
