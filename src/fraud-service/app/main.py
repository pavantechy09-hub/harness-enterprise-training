from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fraud Service", version="1.0.0")

class FraudCheckRequest(BaseModel):
    account_id: str
    amount: float
    merchant: str = ""

class FraudCheckResult(BaseModel):
    account_id: str
    amount: float
    risk_score: float
    decision: str
    reason: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "fraud-service", "version": "1.0.0"}

@app.post("/fraud/check", response_model=FraudCheckResult)
def check_fraud(req: FraudCheckRequest):
    risk_score = 0.0
    reasons = []

    if req.amount > 10000:
        risk_score += 0.5
        reasons.append("high_amount")
    if req.amount > 50000:
        risk_score += 0.3
        reasons.append("very_high_amount")
    if "casino" in req.merchant.lower():
        risk_score += 0.4
        reasons.append("high_risk_merchant")

    risk_score = min(risk_score, 1.0)
    decision = "BLOCK" if risk_score >= 0.7 else "ALLOW"

    return FraudCheckResult(
        account_id=req.account_id,
        amount=req.amount,
        risk_score=round(risk_score, 2),
        decision=decision,
        reason=", ".join(reasons) if reasons else "normal_transaction"
    )
