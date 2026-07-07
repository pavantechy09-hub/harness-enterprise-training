from fastapi.testclient import TestClient
from app.main import app, notifications_db

client = TestClient(app)

def setup_function():
    notifications_db.clear()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_send_email():
    r = client.post("/notify", json={"account_id": "acc-1", "type": "email", "message": "Your payment was processed"})
    assert r.status_code == 200
    assert r.json()["provider"] == "sendgrid"

def test_send_sms_legacy():
    r = client.post("/notify", json={"account_id": "acc-1", "type": "sms", "message": "OTP: 123456"})
    assert r.status_code == 200
    assert r.json()["provider"] == "legacy-sms"

def test_list_notifications():
    client.post("/notify", json={"account_id": "acc-1", "type": "email", "message": "Test"})
    r = client.get("/notifications")
    assert r.status_code == 200
    assert len(r.json()) >= 1
