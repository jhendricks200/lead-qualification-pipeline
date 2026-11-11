# Lead Qualification Pipeline

An AI-powered pipeline for inbound contact-form leads. A FastAPI webhook receives each form submission, Claude classifies it as a real inquiry or junk and scores real leads as hot, warm or cold with a one-line reason, Claude drafts a personalized reply for real leads, and every result is logged to a local CSV file that a small web dashboard reads.

## How it works

```
form submission ──► POST /webhook ──► background task
                                         │
                                         ├─ src/classifier.py     Claude: real/junk, hot/warm/cold, reason (JSON)
                                         ├─ src/email_drafter.py  Claude: reply draft (real leads only)
                                         └─ src/sheets_logger.py  append a row to leads.csv
                                                                      │
GET /dashboard ◄── src/app.py reads leads.csv ◄───────────────────────┘
```

- `main.py` runs one FastAPI app: the webhook at `/webhook` and the dashboard mounted at `/dashboard`.
- The webhook returns immediately and does the Claude calls in a FastAPI background task.
- `src/sheets_logger.py` writes to a local CSV file (`leads.csv` in the project root), despite its name.
- The dashboard shows totals for all, hot, warm, cold and junk leads, a table of leads, and a detail page per lead.

## Setup

Requires Python 3.10+.

```bash
git clone https://github.com/jhendricks200/lead-qualification-pipeline.git
cd lead-qualification-pipeline

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then add your ANTHROPIC_API_KEY
```

## Run

```bash
python main.py
```

- Webhook: `POST http://localhost:8000/webhook`
- Dashboard: `http://localhost:8000/dashboard`

To send a batch of sample submissions to the running server (this calls the Claude API once or twice per submission):

```bash
python test_submissions.py
```

## Example output (format)

The webhook accepts JSON with these fields:

```json
{ "name": "...", "email": "...", "company": "...", "message": "..." }
```

and responds immediately with:

```json
{ "status": "received", "name": "<the submitted name>" }
```

The classifier asks Claude to return JSON in this shape:

```json
{ "classification": "real | junk", "score": "hot | warm | cold", "reason": "<one-line explanation>" }
```

Each processed lead is appended to `leads.csv` with these columns:

```
timestamp,name,email,company,message,classification,score,reason,draft_reply
```

`draft_reply` is empty for leads classified as junk.
