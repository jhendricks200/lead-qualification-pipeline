import json
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def classify_lead(form_data: dict) -> dict:
    prompt = f"""Analyze this website contact form submission and classify it.

Name: {form_data['name']}
Email: {form_data['email']}
Company: {form_data['company']}
Message: {form_data['message']}

Return a JSON object with exactly these fields:
- "classification": either "real" or "junk"
- "score": one of "hot", "warm", or "cold" (use "cold" for junk)
- "reason": a one-line explanation for your scoring

Rules:
- "junk" = spam, bots, test submissions, nonsense, or clearly not a real inquiry
- "hot" = urgent need, specific budget mentioned, ready to buy, decision-maker language
- "warm" = genuine interest, asking real questions, but no urgency signals
- "cold" = vague interest, early research, no clear intent

Return ONLY valid JSON, no other text."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text.strip()
    # Handle markdown code blocks
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()

    return json.loads(text)
