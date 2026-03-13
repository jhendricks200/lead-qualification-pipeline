import uvicorn
from fastapi import FastAPI, BackgroundTasks
from src.webhook_server import FormSubmission, process_submission
from src.app import app as dashboard_app

app = FastAPI()

# Mount dashboard first so it takes priority
app.mount("/dashboard", dashboard_app)


@app.post("/webhook")
async def receive_webhook(submission: FormSubmission, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_submission, submission)
    return {"status": "received", "name": submission.name}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
