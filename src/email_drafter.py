import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def draft_reply(form_data: dict, classification: dict) -> str:
    prompt = f"""Write a personalized follow-up email to this lead. Reference what they specifically asked about. Keep it professional but human — not a generic template.

Lead info:
Name: {form_data['name']}
Email: {form_data['email']}
Company: {form_data['company']}
Message: {form_data['message']}

Lead score: {classification['score']}
Reason: {classification['reason']}

Guidelines:
- For hot leads: be direct, mention next steps like a call or demo
- For warm leads: answer their question, invite further conversation
- For cold leads: be helpful, share a useful resource or insight
- Keep it under 150 words
- Use a friendly professional tone
- Sign off as "The Team"

Return ONLY the email body text, no subject line or metadata."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.content[0].text.strip()
