from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, EmailStr
from src.classifier import classify_lead
from src.email_drafter import draft_reply
from src.sheets_logger import log_lead

app = FastAPI()


class FormSubmission(BaseModel):
    name: str
    email: str
    company: str
    message: str


def process_submission(submission: FormSubmission):
    classification = classify_lead(submission.model_dump())

    draft = None
    if classification["classification"] == "real":
        draft = draft_reply(submission.model_dump(), classification)

    log_lead(submission.model_dump(), classification, draft)


@app.post("/webhook")
async def receive_submission(submission: FormSubmission, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_submission, submission)
    return {"status": "received", "name": submission.name}
