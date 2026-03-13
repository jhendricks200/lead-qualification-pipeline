# Lead Automation

AI-powered lead qualification pipeline. Webhook receives form submissions, Claude classifies and scores them, drafts personalized replies, and logs everything to a dashboard.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your ANTHROPIC_API_KEY
```

## Run

```bash
python main.py
```

- Webhook: POST to `http://localhost:8000/webhook`
- Dashboard: `http://localhost:8000/dashboard`

## Test

```bash
python test_submissions.py
```
