from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_normal_transaction_allowed():
    r = client.post("/fraud/check", json={"account_id": "acc-1", "amount": 100.0, "merchant": "Tesco"})
    assert r.status_code == 200
    assert r.json()["decision"] == "ALLOW"
    assert r.json()["risk_score"] == 0.0

def test_high_amount_flagged():
    r = client.post("/fraud/check", json={"account_id": "acc-1", "amount": 15000.0, "merchant": "Amazon"})
    assert r.json()["risk_score"] > 0
    assert "high_amount" in r.json()["reason"]

def test_casino_blocked():
    r = client.post("/fraud/check", json={"account_id": "acc-1", "amount": 15000.0, "merchant": "Online Casino"})
    assert r.json()["decision"] == "BLOCK"
    assert r.json()["risk_score"] >= 0.7
