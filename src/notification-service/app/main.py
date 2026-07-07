from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Notification Service", version="1.0.0")

notifications_db = []

FEATURE_FLAG_NEW_SMS = False  # Day 5: Feature flag

class NotifyRequest(BaseModel):
    account_id: str
    type: str  # email | sms | push
    message: str

class NotifyResult(BaseModel):
    id: str
    account_id: str
    type: str
    message: str
    provider: str
    sent_at: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "notification-service", "version": "1.0.0"}

@app.post("/notify", response_model=NotifyResult)
def send_notification(req: NotifyRequest):
    import uuid
    provider = "legacy-sms" if req.type == "sms" else "sendgrid"
    if req.type == "sms" and FEATURE_FLAG_NEW_SMS:
        provider = "twilio"  # Feature flag: new provider

    result = NotifyResult(
        id=str(uuid.uuid4()),
        account_id=req.account_id,
        type=req.type,
        message=req.message,
        provider=provider,
        sent_at=datetime.utcnow().isoformat()
    )
    notifications_db.append(result)
    return result

@app.get("/notifications")
def list_notifications():
    return notifications_db
