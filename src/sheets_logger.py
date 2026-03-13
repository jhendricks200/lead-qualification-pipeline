import csv
import os
from datetime import datetime

CSV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "leads.csv")

HEADERS = [
    "timestamp", "name", "email", "company", "message",
    "classification", "score", "reason", "draft_reply",
]


def _ensure_csv():
    if not os.path.exists(CSV_PATH):
        with open(CSV_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)


def log_lead(form_data: dict, classification: dict, draft_reply: str | None):
    _ensure_csv()
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            form_data["name"],
            form_data["email"],
            form_data["company"],
            form_data["message"],
            classification["classification"],
            classification["score"],
            classification["reason"],
            draft_reply or "",
        ])
