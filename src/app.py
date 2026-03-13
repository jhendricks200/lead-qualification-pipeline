import csv
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "leads.csv")


def load_leads() -> list[dict]:
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    leads = load_leads()
    total = len(leads)
    hot = sum(1 for l in leads if l["score"] == "hot")
    warm = sum(1 for l in leads if l["score"] == "warm")
    cold = sum(1 for l in leads if l["score"] == "cold")
    junk = sum(1 for l in leads if l["classification"] == "junk")
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "leads": leads,
        "total": total,
        "hot": hot,
        "warm": warm,
        "cold": cold,
        "junk": junk,
    })


@app.get("/lead/{index}", response_class=HTMLResponse)
async def lead_detail(request: Request, index: int):
    leads = load_leads()
    if index < 0 or index >= len(leads):
        return HTMLResponse("Lead not found", status_code=404)
    lead = leads[index]
    return templates.TemplateResponse("detail.html", {
        "request": request,
        "lead": lead,
        "index": index,
    })
