"""Send 10 test form submissions through the webhook."""
import httpx
import time

BASE_URL = "http://localhost:8000/webhook"

SUBMISSIONS = [
    {
        "name": "Sarah Chen",
        "email": "sarah.chen@techcorp.com",
        "company": "TechCorp Solutions",
        "message": "We need to migrate our legacy CRM to a cloud-based solution by Q3. Budget is $200K. Can we schedule a call this week to discuss your enterprise plan?"
    },
    {
        "name": "asdfjkl",
        "email": "test@test.test",
        "company": "asdf",
        "message": "buy cheap viagra online best prices click here now!!! www.spam-link.com"
    },
    {
        "name": "Marcus Johnson",
        "email": "mjohnson@retailgroup.com",
        "company": "Retail Group Inc",
        "message": "I saw your presentation at the SaaS conference last month. We're exploring options for inventory management automation. Could you send over some case studies?"
    },
    {
        "name": "Elena Vasquez",
        "email": "elena.v@globalfinance.co",
        "company": "Global Finance Partners",
        "message": "Our CEO wants to implement AI-driven analytics across all departments by next quarter. We have 2,000 employees and need enterprise licensing. Who should I speak with about pricing?"
    },
    {
        "name": "",
        "email": "nobody@nowhere.com",
        "company": "",
        "message": "testing 123 testing"
    },
    {
        "name": "David Park",
        "email": "dpark@startupxyz.io",
        "company": "StartupXYZ",
        "message": "Hey, just browsing your site. What exactly do you guys do? I'm a student working on a project and curious about your tech stack."
    },
    {
        "name": "Rachel Torres",
        "email": "rtorres@medicohealth.com",
        "company": "MedicoHealth Systems",
        "message": "We're a hospital network with 15 locations. Our current patient portal is failing compliance audits. We need a HIPAA-compliant replacement deployed within 60 days. This is urgent — can your team handle this timeline?"
    },
    {
        "name": "FREE MONEY",
        "email": "winner@lottery.scam",
        "company": "Nigerian Prince Enterprises",
        "message": "CONGRATULATIONS!!! You have won $5,000,000. Send your bank details to claim your prize immediately. ACT NOW before offer expires!!!"
    },
    {
        "name": "James O'Brien",
        "email": "jobrien@constructco.com",
        "company": "ConstructCo Builders",
        "message": "We're a mid-size construction firm looking at project management tools. Nothing urgent, just want to understand what's available. Maybe a demo sometime next month?"
    },
    {
        "name": "Priya Sharma",
        "email": "priya@designstudio.com",
        "company": "Sharma Design Studio",
        "message": "I run a 12-person design agency. We need a client portal where customers can review and approve designs. Also interested in your API for integrating with Figma. Can we do a 30-minute call tomorrow?"
    },
]


def main():
    print(f"Sending {len(SUBMISSIONS)} test submissions to {BASE_URL}\n")

    for i, sub in enumerate(SUBMISSIONS, 1):
        try:
            resp = httpx.post(BASE_URL, json=sub, timeout=10)
            status = "OK" if resp.status_code == 200 else f"ERR {resp.status_code}"
            name = sub["name"] or "(empty)"
            print(f"  [{i}/10] {name:25s} — {status}")
        except httpx.ConnectError:
            print(f"  [{i}/10] FAILED — is the server running on port 8000?")
            return

    print("\nAll submissions sent!")
    print("Wait ~30 seconds for AI processing, then visit: http://localhost:8000/dashboard")


if __name__ == "__main__":
    main()
