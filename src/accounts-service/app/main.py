from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI(title="Accounts Service", version="1.0.0")

accounts_db = {}

class CreateAccountRequest(BaseModel):
    name: str
    email: str
    initial_balance: float = 0.0

class Account(BaseModel):
    id: str
    name: str
    email: str
    balance: float
    status: str
    created_at: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "accounts-service", "version": "1.0.0"}

@app.post("/accounts", response_model=Account, status_code=201)
def create_account(req: CreateAccountRequest):
    account = Account(
        id=str(uuid.uuid4()),
        name=req.name,
        email=req.email,
        balance=req.initial_balance,
        status="active",
        created_at=datetime.utcnow().isoformat()
    )
    accounts_db[account.id] = account
    return account

@app.get("/accounts/{account_id}", response_model=Account)
def get_account(account_id: str):
    if account_id not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts_db[account_id]

@app.get("/accounts", response_model=list[Account])
def list_accounts():
    return list(accounts_db.values())
