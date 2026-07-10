# Harness Enterprise CI/CD Training — 10 Days

A complete hands-on enterprise Harness CI/CD training built on a real banking microservices platform (BankOps). Every day includes real pipeline runs, actual issues encountered and resolved, and interview Q&A.

## Course Site

**[View the interactive course → https://pavantechy09-hub.github.io/harness-enterprise-training](https://pavantechy09-hub.github.io/harness-enterprise-training)**

## What You Will Learn

| Day | Topic | Key Hands-On |
|-----|-------|-------------|
| Day 1 | Delegate + Connectors | Helm delegate on K8s, 5 connectors, first CI pipeline |
| Day 2 | Docker Build + Push | BuildAndPushDockerRegistry, vguardai/* images |
| Day 3 | Jenkins Migration | payments-service CI, approval gate |
| Day 4 | All 4 Services CI | Remote pipeline from GitHub, 19 tests |
| Day 5 | Canary + Blue-Green | Proved hands-on, 2-second cutover, rollback |
| Day 6 | RBAC + OPA + API Keys | sre-team group, policy step, PAT vs SA token |
| Day 7 | GitOps with Flux CD | Git commit = deploy, drift detection in 60s |
| Day 8 | AIOps + K8sGPT | Ollama llama3.2:1b, real cluster diagnosis |
| Day 9 | FinOps | kubectl top data, $45/month saving identified |
| Day 10 | Capstone | 7-stage pipeline, Build #3 SUCCESS |

## Stack

- **Harness CI** — Enterprise CI/CD platform
- **Kubernetes** — kind dd-stg cluster
- **Docker Hub** — vguardai/* image registry
- **Flux CD** — GitOps agent (drift detection proved)
- **K8sGPT + Ollama** — AIOps with local LLM
- **Python FastAPI** — 4 microservices, 19 tests
- **GitHub** — Remote pipeline storage

## Microservices

| Service | Port | Tests |
|---------|------|-------|
| accounts-service | 8000 | 6 |
| payments-service | 8001 | 5 |
| fraud-service | 8002 | 4 |
| notification-service | 8003 | 4 |

## Real Results

- 19/19 tests passing across all services
- 4 Docker images live on Docker Hub
- 5 Harness pipelines stored in GitHub
- Flux CD drift detection proved in 60 seconds
- $45/month FinOps saving identified from real cluster data
- Capstone Build #3 SUCCESS — all 7 stages complete

## Portfolio

- **This repo:** [github.com/pavantechy09-hub/harness-enterprise-training](https://github.com/pavantechy09-hub/harness-enterprise-training)
- **Cloud IAC:** [github.com/pavantechy09-hub/cloud-iac-learning](https://github.com/pavantechy09-hub/cloud-iac-learning)
- **Cloud IAC Site:** [pavantechy09-hub.github.io/cloud-iac-learning](https://pavantechy09-hub.github.io/cloud-iac-learning)
