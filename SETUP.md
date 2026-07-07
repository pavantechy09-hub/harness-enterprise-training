# Harness Enterprise Training — Setup Guide

## Prerequisites
- Docker Desktop running
- Floci running (. D:\cloud-iac\start-env.ps1)
- kind dd-stg cluster running
- Helm installed
- kubectl configured for kind-dd-stg
- Harness account at app.harness.io

## One-Time Setup (Do This Once)

### 1. Install Helm (Windows)
```powershell
choco install kubernetes-helm -y
$env:PATH += ";C:\Program Files\Microsoft SDKs\Azure\CLI2\wbin\lib\kubernetes-helm\tools\windows-amd64"
helm version
```

### 2. Install Harness Delegate
```powershell
kubectl config use-context kind-dd-stg

helm repo add harness-delegate https://app.harness.io/storage/harness-download/delegate-helm-chart/
helm repo update harness-delegate

helm install helm-delegate harness-delegate/harness-delegate-ng --namespace harness-delegate-ng --create-namespace --set delegateName=helm-delegate --set accountId=WiFTuqq1S66Gdw6nwnGUJg --set delegateToken=NmQ2Yjc3MWYxNzZmMzA4ZTUyOTQzYTAwMjBjNWY4Y2E= --set managerEndpoint=https://app.harness.io --set delegateDockerImage=us-docker.pkg.dev/gar-prod-setup/harness-public/harness/delegate:26.06.89303 --set replicas=1 --set upgrader.enabled=false
```

### 3. Create Kubernetes Namespaces
```powershell
kubectl apply -f k8s/namespaces/namespaces.yaml
kubectl get namespaces
```

### 4. Create Connectors in Harness UI
Go to: bank-platform project → Project Settings → Connectors

| Name | Type | Details |
|------|------|---------|
| bankopsgithub | GitHub | URL: github.com/pavantechy09-hub/harness-enterprise-training, Auth: PAT |
| ddstgk8s | Kubernetes | Use Delegate credentials |
| dockerhub | Docker Registry | URL: index.docker.io/v1/, Anonymous |

### 5. Verify Setup
```powershell
kubectl get pods -n harness-delegate-ng
# Expected: helm-delegate-xxxxx   1/1   Running

kubectl get namespaces
# Expected: harness-builds, accounts, payments, fraud, notifications
```

## Daily Startup
```powershell
. D:\cloud-iac\start-env.ps1
kubectl config use-context kind-dd-stg
kubectl get pods -n harness-delegate-ng
```

## Connectors IDs (use these in pipeline YAML)
- GitHub: bankopsgithub
- Kubernetes: ddstgk8s
- Docker Hub: dockerhub

## Harness Project Details
- Account: pavantechy09
- Org: default
- Project: bank-platform (identifier: bankplatform)
- URL: app.harness.io/ng/account/WiFTuqq1S66Gdw6nwnGUJg/module/ci/orgs/default/projects/bankplatform
