from fastapi.testclient import TestClient
from app.main import app, accounts_db

client = TestClient(app)

def setup_function():
    accounts_db.clear()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"

def test_create_account():
    r = client.post("/accounts", json={"name": "Pavan Goli", "email": "pavan@bank.com", "initial_balance": 1000.0})
    assert r.status_code == 201
    assert r.json()["name"] == "Pavan Goli"
    assert r.json()["balance"] == 1000.0

def test_get_account():
    r = client.post("/accounts", json={"name": "Test", "email": "test@bank.com"})
    account_id = r.json()["id"]
    r2 = client.get(f"/accounts/{account_id}")
    assert r2.status_code == 200
    assert r2.json()["id"] == account_id

def test_get_account_not_found():
    r = client.get("/accounts/nonexistent")
    assert r.status_code == 404

def test_list_accounts():
    client.post("/accounts", json={"name": "A", "email": "a@bank.com"})
    client.post("/accounts", json={"name": "B", "email": "b@bank.com"})
    r = client.get("/accounts")
    assert r.status_code == 200
    assert len(r.json()) >= 2

def test_default_balance():
    r = client.post("/accounts", json={"name": "Zero", "email": "zero@bank.com"})
    assert r.json()["balance"] == 0.0

