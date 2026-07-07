from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI(title="Payments Service", version="1.0.0")

payments_db = {}

class CreatePaymentRequest(BaseModel):
    from_account: str
    to_account: str
    amount: float
    reference: str = ""

class Payment(BaseModel):
    id: str
    from_account: str
    to_account: str
    amount: float
    reference: str
    status: str
    created_at: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "payments-service", "version": "1.0.0"}

@app.post("/payments", response_model=Payment, status_code=201)
def create_payment(req: CreatePaymentRequest):
    if req.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    payment = Payment(
        id=str(uuid.uuid4()),
        from_account=req.from_account,
        to_account=req.to_account,
        amount=req.amount,
        reference=req.reference,
        status="processed",
        created_at=datetime.utcnow().isoformat()
    )
    payments_db[payment.id] = payment
    return payment

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: str):
    if payment_id not in payments_db:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payments_db[payment_id]

@app.get("/payments", response_model=list[Payment])
def list_payments():
    return list(payments_db.values())
