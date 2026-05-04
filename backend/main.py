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
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

# ── Paths ─────────────────────────────────────────────────────────────
BACKEND_DIR  = Path(__file__).parent
BUILDER_PATH = BACKEND_DIR / "build_summary_v3.py"

# ── Industry name → 4-letter code mapping ─────────────────────────────
# Maps the strings sent by the frontend dropdown to the codes the builder uses.
# If the frontend sends a label not in this map, /generate returns 400.
INDUSTRY_MAP = {
    "Professional Services":          "PROF",
    "Financial Services":             "FINS",
    "Technology and SaaS":            "TECH",
    "Technology & SaaS":              "TECH",
    "Technology":                     "TECH",
    "Healthcare":                     "HCAR",
    "Healthcare and Life Sciences":   "HCAR",
    "Healthcare & Life Sciences":     "HCAR",
    "Retail":                         "RETL",
    "Retail and Consumer":            "RETL",
    "Retail & Consumer":              "RETL",
    "Manufacturing":                  "INDU",
    "Manufacturing and Industrial":   "INDU",
    "Industrial":                     "INDU",
    "Public Sector":                  "PUBL",
    "Public Sector and Not-for-Profit": "PUBL",
    "Public Sector & Not-for-Profit": "PUBL",
    "Not-for-Profit":                 "PUBL",
    "Government":                     "PUBL",
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
    # Map industry label to code
    industry_label = config.organisation.industry
    industry_code = INDUSTRY_MAP.get(industry_label)
    if industry_code is None:
        raise HTTPException(
            status_code=400,
            detail=(f"Unknown industry '{industry_label}'. "
                    f"Supported: {sorted(set(INDUSTRY_MAP.keys()))}"),
        )

    # Build output path (will hold the generated workbook)
    out_fd, out_path = tempfile.mkstemp(suffix=".xlsx", prefix="bpr_register_")
    os.close(out_fd)

    # Build config JSON for the builder subprocess
    builder_config = {
        "industry_code": industry_code,
        "output_path": out_path,
        "organisation": config.organisation.model_dump(),
        "financial": config.financial.model_dump(),
        "focus_areas": config.focus_areas,
        "rag_thresholds": [t.model_dump() for t in config.rag_thresholds],
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
            timeout=60,
        )
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=504, detail="Workbook generation timed out (>60s).")
    finally:
        # Clean up the config file regardless
        try:
            os.remove(cfg_path)
        except OSError:
            pass

    if result.returncode != 0:
        raise HTTPException(
            status_code=500,
            detail=f"Builder failed: {result.stderr[-500:] if result.stderr else 'no stderr'}",
        )

    if not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
        raise HTTPException(status_code=500, detail="Builder produced no output file.")

    # Build response filename
    org_slug = config.organisation.name.replace(" ", "_").replace("/", "_") or "Register"
    today = datetime.date.today().isoformat()
    download_name = f"BluePeakRisk_{org_slug}_{today}.xlsx"

    return FileResponse(
        out_path,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        filename=download_name,
        # FileResponse will stream and Starlette handles cleanup of the path
        # via its background cleanup if we use BackgroundTask; for simplicity
        # we rely on the OS to clean /tmp eventually.
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
