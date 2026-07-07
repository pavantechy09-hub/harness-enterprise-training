# Day 9 — FinOps + Cloud Cost Management

## Service Added / Updated
Cost per service visible, anomaly detection

## Pipeline File
`.harness/pipelines/day9-finops-ccm.yaml`

## Prerequisites
```bash
# Start environment
. D:\cloud-iac\start-env.ps1
kubectl config use-context kind-dd-stg
kubectl get nodes
kubectl get pods -n harness-delegate-ng
kubectl apply -f k8s/namespaces/namespaces.yaml
```

## Connectors Required
- `bankopsgithub` — GitHub connector
- `ddstgk8s` — Kubernetes cluster connector  
- `dockerhub` — Docker Hub connector

## How to Run
1. Open Harness UI → bank-platform project
2. Go to Pipelines
3. Find the Day 9 pipeline
4. Click Run

## Course UI
Full interactive content with simulators, YAML, and Q&A:
https://pavantechy09-hub.github.io/harness-enterprise-training

## Key Concepts This Day
See the Day 9 tab in the course UI for:
- Concept explanations with diagrams
- Live simulators (Day 5: canary and blue-green)
- Pipeline YAML with comments
- Issues we hit and how we fixed them
- Interview questions and answers
