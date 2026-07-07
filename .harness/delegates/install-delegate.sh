#!/bin/bash
# Install Harness Delegate on dd-stg cluster
# Run this script to set up the delegate
# Replace ACCOUNT_ID and TOKEN with values from Harness UI

ACCOUNT_ID="WiFTuqq1S66Gdw6nwnGUJg"
DELEGATE_TOKEN="NmQ2Yjc3MWYxNzZmMzA4ZTUyOTQzYTAwMjBjNWY4Y2E="
DELEGATE_IMAGE="us-docker.pkg.dev/gar-prod-setup/harness-public/harness/delegate:26.06.89303"

# Step 1: Switch to correct cluster
kubectl config use-context kind-dd-stg

# Step 2: Add Harness helm repo
helm repo add harness-delegate https://app.harness.io/storage/harness-download/delegate-helm-chart/
helm repo update harness-delegate

# Step 3: Install delegate (single line - avoid PowerShell backtick issues)
helm install helm-delegate harness-delegate/harness-delegate-ng \
  --namespace harness-delegate-ng \
  --create-namespace \
  --set delegateName=helm-delegate \
  --set accountId=${ACCOUNT_ID} \
  --set delegateToken=${DELEGATE_TOKEN} \
  --set managerEndpoint=https://app.harness.io \
  --set delegateDockerImage=${DELEGATE_IMAGE} \
  --set replicas=1 \
  --set upgrader.enabled=false

# Step 4: Verify
echo "Waiting for delegate pod to start..."
kubectl wait --for=condition=ready pod \
  -l app=harness-delegate \
  -n harness-delegate-ng \
  --timeout=300s

echo "Delegate installed successfully"
kubectl get pods -n harness-delegate-ng

# Step 5: Create required namespaces
kubectl apply -f k8s/namespaces/namespaces.yaml
echo "Namespaces created"
