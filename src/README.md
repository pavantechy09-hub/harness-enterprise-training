# BankOps Platform — Application Code

## Services

| Service | Port | Day Added | Description |
|---------|------|-----------|-------------|
| accounts-service | 8000 | Day 1 | Account management |
| payments-service | 8001 | Day 3 | Payment processing |
| fraud-service | 8002 | Day 5 | ML fraud scoring |
| notification-service | 8003 | Day 7 | Email/SMS/Push |

## Run Locally

```bash
# Any service
cd src/accounts-service
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# Run tests
pytest app/tests/ -v --cov=app
```

## API Endpoints

accounts-service:
  GET  /health
  POST /accounts
  GET  /accounts/{id}
  GET  /accounts

payments-service:
  GET  /health
  POST /payments
  GET  /payments/{id}

fraud-service:
  GET  /health
  POST /fraud/check

notification-service:
  GET  /health
  POST /notify
  GET  /notifications
