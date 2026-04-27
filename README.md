# SME Risk Register

A free, professional risk register tool for small and medium enterprises. Configure your scoring framework, set financial thresholds linked to NPAT, and download a tailored Excel register.

## Features

- 7 impact categories (Financial, Customer, Regulatory, Reputational, People, Social, Environmental)
- NPAT-linked financial impact thresholds
- Customisable likelihood scale and RAG thresholds
- Pre-loaded starter risks based on focus areas
- Single-page web app with Excel file generation

## Architecture

```
sme-risk-register/
├── frontend/          # Static HTML/CSS/JS — deployed to GitHub Pages
│   └── index.html
├── backend/           # FastAPI Python service — deployed to Railway
│   ├── main.py
│   ├── requirements.txt
│   ├── Procfile
│   └── railway.json
├── DEPLOY.md          # Step-by-step deployment guide
└── README.md          # This file
```

## Deployment

See **[DEPLOY.md](DEPLOY.md)** for complete step-by-step instructions. Total time: ~15 minutes.

The deployment uses:
- **GitHub Pages** for the frontend (free)
- **Railway** for the backend API ($5/month after free trial)

## Local development

### Run backend locally:

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API will be available at `http://localhost:8000`. Test with:
```bash
curl http://localhost:8000/health
```

### Run frontend locally:

The frontend automatically uses `localhost:8000` when served from `localhost`. Open `frontend/index.html` directly in a browser, or run a simple server:

```bash
cd frontend
python -m http.server 3000
```

Then visit `http://localhost:3000`.

## API

### `POST /generate`

Request body:
```json
{
  "organisation": {
    "name": "Acme Pty Ltd",
    "industry": "Professional Services",
    "size": "Medium (20-199 staff)",
    "country": "Australia",
    "cycle": "Quarterly",
    "notes": ""
  },
  "financial": {
    "npat": 2000000,
    "currency": "AUD",
    "fin_pcts": [0.01, 0.03, 0.08, 0.15, 0.25]
  },
  "focus_areas": ["Cyber & Data", "Financial"],
  "rag_thresholds": [
    { "label": "Green", "min": 1, "max": 5 },
    { "label": "Amber", "min": 6, "max": 14 },
    { "label": "Red", "min": 15, "max": 25 }
  ],
  "scoring_method": "max"
}
```

Returns: An `.xlsx` file as a streaming download.

## Licence

Free for any business use. No warranty.
