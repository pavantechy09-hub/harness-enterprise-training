from fastapi.testclient import TestClient
from app.main import app, payments_db

client = TestClient(app)

def setup_function():
    payments_db.clear()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["service"] == "payments-service"

def test_create_payment():
    r = client.post("/payments", json={"from_account": "acc-1", "to_account": "acc-2", "amount": 500.0, "reference": "INV-001"})
    assert r.status_code == 201
    assert r.json()["status"] == "processed"
    assert r.json()["amount"] == 500.0

def test_negative_amount():
    r = client.post("/payments", json={"from_account": "acc-1", "to_account": "acc-2", "amount": -100.0})
    assert r.status_code == 400

def test_get_payment():
    r = client.post("/payments", json={"from_account": "a", "to_account": "b", "amount": 100.0})
    pid = r.json()["id"]
    r2 = client.get(f"/payments/{pid}")
    assert r2.status_code == 200

def test_payment_not_found():
    r = client.get("/payments/nonexistent")
    assert r.status_code == 404
