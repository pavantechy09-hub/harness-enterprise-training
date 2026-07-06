# Harness Enterprise Training — 10-Day Intensive

## FinOps Bank Platform Migration
### From Jenkins + GitHub Actions → Harness Enterprise CD

> **Real enterprise migration. Hands-on every day. Zero theory without proof.**
> Same bank story from cloud-iac-learning. Same Floci infrastructure. New enterprise CD layer.

---

## Portfolio Links
- Cloud IaC Foundation: [cloud-iac-learning](https://github.com/pavantechy09-hub/cloud-iac-learning)
- Live Portfolio: [pavantechy09-hub.github.io/cloud-iac-learning](https://pavantechy09-hub.github.io/cloud-iac-learning)
- LinkedIn: [linkedin.com/in/pavan-goli](https://linkedin.com/in/pavan-goli)

---

## The Story

FirstNational Bank has outgrown Jenkins and GitHub Actions.
- 200+ microservices
- 50 teams deploying independently
- No governance — anyone can deploy anything to production
- No rollback automation — manual hotfixes at 3am
- No deployment strategies — every release is a big bang
- No cost visibility — nobody knows what each service costs
- Compliance team demanding audit trails and approval gates
- Security team demanding Checkov gates before every deployment

**You are the Platform Engineer leading the migration to Harness.**

---

## 10-Day Plan

| Day | Topic | Tools | Hands-On |
|-----|-------|-------|----------|
| 1 | Foundations + Architecture | Harness, Delegate, Connectors | First pipeline running |
| 2 | CI Migration from GitHub Actions | Harness CI, STO, Checkov | Migrated pipeline compared |
| 3 | Jenkins Migration | Jenkinsfile → Harness | Side-by-side migration |
| 4 | CD + Kubernetes Deployments | Harness CD, K8s, Floci | 4 services deployed |
| 5 | Advanced Deployment Strategies | Canary, Blue-Green, Rolling, Feature Flags | All 4 strategies live |
| 6 | Governance + OPA Policies | OPA, Rego, RBAC, Templates | Policies enforcing on pipelines |
| 7 | GitOps with Harness | Harness GitOps, Argo CD comparison | Git-driven deployments |
| 8 | AIOps + AIDA + SRM | Harness AIDA, Dynatrace, SLOs | AI explaining failures |
| 9 | FinOps + Cloud Cost Management | Harness CCM, cost dashboards | Cost per service visible |
| 10 | Capstone + Migration Plan | Full pipeline + 90-day plan | Production-grade delivery |

---

## Migration Context — Why Enterprises Move to Harness

### The Jenkins Problem
```
Jenkins was built in 2004 for a different era.
Modern enterprises hit these walls:

Maintenance burden:
  Groovy DSL nobody wants to maintain
  500+ plugins, each with its own version conflicts
  Jenkins master = single point of failure
  Plugin updates break pipelines regularly
  Security patches require downtime

Scale problems:
  No native multi-cloud support
  No built-in deployment strategies
  No automatic rollback
  No governance / approval gates built-in
  No cost visibility
  No AI assistance

Compliance problems:
  No native audit trail per deployment
  No four-eyes principle enforcement
  No deployment freeze windows
  No SLO tracking
  Manual approval processes = email chains
```

### The GitHub Actions Gap
```
GitHub Actions is excellent for CI.
It hits limits for enterprise CD:

No native deployment strategies:
  Canary and blue-green require custom scripts
  No automatic rollback out of the box
  No health verification post-deploy

No governance:
  Any developer can deploy to production
  No mandatory approval gates
  No OPA policy enforcement
  No deployment freeze windows

No unified platform:
  CI lives in GitHub
  CD is custom scripts
  Cost management is separate tool
  SLO tracking is separate tool
  Security scanning is separate tool
  All disconnected — no single pane of glass
```

### Why Harness
```
Harness solves all of this in one platform:

  Built-in canary, blue-green, rolling strategies
  Automatic rollback if health checks fail
  OPA governance on every deployment
  Four-eyes approval enforcement
  Deployment freeze windows
  Full audit trail per deployment
  Cost per service and per deployment
  SLO tracking with error budgets
  AI assistant (AIDA) explains failures
  Works across AWS, Azure, GCP, K8s, on-prem
  Single platform: CI + CD + Security + Cost + Reliability
```

---

## Architecture — Before and After

### Before (Current State)
```
Developer pushes code
       ↓
GitHub Actions (CI only):
  Checkov scan (manual config)
  Terraform plan
  terraform apply (risky — no approval)
  kubectl apply (manual — no strategy)
       ↓
Jenkins (legacy CD):
  Jenkinsfile in repo
  Manual approval via email
  No rollback automation
  No deployment strategy
  No cost tracking
       ↓
Production (fingers crossed)
  Manual monitoring
  Manual rollback
  3am hotfixes
```

### After (Harness)
```
Developer pushes code
       ↓
Harness CI:
  Checkov STO (blocks HIGH findings)
  Terraform plan (posted as comment)
  Test intelligence (skip unchanged tests)
  Artifact built + pushed to registry
       ↓
Harness CD (automatic to dev):
  K8s rolling deployment
  Health verification
  Smoke tests
  Automatic rollback if unhealthy
       ↓
Harness Approval Gate (SRE reviews):
  Sees: deployment diff, test results, cost impact
  Approves or rejects with comment
       ↓
Harness CD (canary to staging):
  10% → 25% → 50% → 100%
  Dynatrace monitors error rate
  Auto-rollback if SLO breached
       ↓
Harness Approval Gate (Platform team):
  Two-person approval enforced by OPA
  Deployment freeze check (no Friday deploys)
       ↓
Harness CD (blue-green to production):
  New version deployed alongside old
  Traffic switched instantly
  Old version kept 30 minutes for rollback
  Dynatrace verifies SLO maintained
       ↓
Harness SRM:
  SLO dashboard updated
  Error budget consumed/remaining
  Cost per deployment recorded
  Audit trail complete
       ↓
Slack notification:
  Deployment summary
  Cost impact
  SLO status
  Who approved what and when
```

---

## Day 1 — Harness Foundations + Architecture

### What Was Built
```
Harness free account created
Organisation: firstnational-bank
Projects: infrastructure, accounts, payments, fraud, platform

Harness Delegate installed on dd-stg kind cluster:
  helm install harness-delegate harness/harness-delegate
  Delegate = agent running inside your cluster
  Executes all pipeline steps locally
  Connects outbound to Harness SaaS (no inbound ports needed)

Connectors configured:
  GitHub connector → pavantechy09-hub repos
  Kubernetes connector → dd-stg cluster
  AWS connector → Floci (localhost:4566)
  Azure connector → floci-az (localhost:4577)
  Docker Registry connector → Docker Hub

First pipeline built:
  Trigger: manual
  Step 1: shell script "echo Hello from Harness"
  Step 2: kubectl get nodes
  Result: ran inside dd-stg cluster via Delegate
```

### Harness Entity Hierarchy
```
Account (top level — your Harness login)
  └── Organisation (e.g. firstnational-bank)
        └── Project (e.g. payments-platform)
              ├── Pipelines
              ├── Services
              ├── Environments
              ├── Connectors
              ├── Secrets
              └── Templates
```

### Delegate Deep Dive
```
What it is:
  A pod running inside your Kubernetes cluster
  OR a Docker container on your server
  Polls Harness SaaS for tasks every 10 seconds
  Executes tasks locally (no inbound firewall rules needed)
  Reports results back to Harness

Why it matters:
  Your cluster never needs to be publicly accessible
  Credentials stay inside your network
  Delegate runs kubectl, terraform, helm — all locally
  Multiple Delegates = high availability

Compare to:
  GitHub Actions runner (self-hosted) = similar concept
  Jenkins agent = similar concept
  But Delegate is smarter: auto-selects, auto-upgrades
```

### Connectors vs Secrets
```
Connector = how to connect to a system
  GitHub connector: base URL + authentication method
  K8s connector: cluster endpoint + service account
  AWS connector: region + credentials method

Secret = the actual credential
  GitHub token stored in Harness Secrets Manager
  K8s service account token
  AWS access key (or OIDC role ARN)

Connector references a Secret
Secret is never exposed in pipeline YAML
```

---

## Day 2 — CI Migration from GitHub Actions

### Migration Mapping

| GitHub Actions Concept | Harness CI Equivalent |
|------------------------|----------------------|
| workflow.yml | Harness Pipeline YAML |
| on: push/pull_request | Trigger (Git, Webhook, Scheduled) |
| jobs: | Stages: |
| steps: | Steps: |
| uses: actions/checkout | Built-in Clone Codebase step |
| uses: hashicorp/setup-terraform | Run step with Terraform image |
| secrets.AWS_ROLE_ARN | Harness Secret reference |
| runs-on: ubuntu-latest | Delegate (runs in your cluster) |
| if: github.ref == 'refs/heads/main' | Conditional execution |
| needs: security-scan | Stage dependency |
| continue-on-error: true | Failure strategy: Ignore |
| matrix: | Looping / parallel stages |

### Before (GitHub Actions)
```yaml
# .github/workflows/terraform.yml
name: Terraform CI/CD
on:
  pull_request:
    branches: [main]
jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: bridgecrewio/checkov-action@master
        with:
          soft_fail: true
  terraform-plan:
    needs: security-scan
    runs-on: ubuntu-latest
    steps:
      - uses: hashicorp/setup-terraform@v3
      - run: terraform init
      - run: terraform plan -no-color
```

### After (Harness CI)
```yaml
# .harness/pipelines/ci-terraform.yaml
pipeline:
  name: Terraform CI
  identifier: terraform_ci
  stages:
    - stage:
        name: Security Scan
        type: CI
        spec:
          steps:
            - step:
                name: Checkov Scan
                type: Security
                spec:
                  privileged: true
                  settings:
                    product_name: checkov
                    product_config_name: default
                    fail_on_severity: HIGH
    - stage:
        name: Terraform Plan
        type: CI
        spec:
          steps:
            - step:
                name: TF Init and Plan
                type: Run
                spec:
                  image: hashicorp/terraform:1.15.5
                  command: |
                    terraform init
                    terraform plan -no-color -out=tfplan
```

### Key Improvements Over GitHub Actions
```
Harness CI adds:
  Test Intelligence: only runs tests affected by code change
    Result: 60% faster CI on average
  Built-in caching: automatic layer and dependency caching
  STO integration: security results in Harness UI (not just logs)
  Cost per build: know exactly what each CI run costs
  AIDA: AI explains why build failed in plain English
  Approval gates: can add manual approval mid-pipeline
  Better visibility: real-time step logs in clean UI
```

---

## Day 3 — Jenkins Migration

### Jenkinsfile (Before)
```groovy
pipeline {
  agent any
  
  environment {
    AWS_REGION = 'us-east-1'
    TF_VERSION = '1.15.5'
  }
  
  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    
    stage('Security Scan') {
      steps {
        sh 'pip install checkov'
        sh 'checkov -d . --framework terraform --quiet'
      }
    }
    
    stage('Terraform Init') {
      steps {
        sh 'terraform init'
      }
    }
    
    stage('Terraform Plan') {
      steps {
        sh 'terraform plan -no-color -out=tfplan'
        archiveArtifacts artifacts: 'tfplan'
      }
    }
    
    stage('Approval') {
      when {
        branch 'main'
      }
      steps {
        input message: 'Deploy to production?',
              ok: 'Deploy'
      }
    }
    
    stage('Terraform Apply') {
      when {
        branch 'main'
      }
      steps {
        sh 'terraform apply tfplan'
      }
    }
  }
  
  post {
    failure {
      slackSend channel: '#alerts',
                message: "Build failed: ${env.JOB_NAME}"
    }
    success {
      slackSend channel: '#deployments',
                message: "Deployed: ${env.JOB_NAME}"
    }
  }
}
```

### Harness Equivalent (After)
```yaml
pipeline:
  name: Terraform Pipeline (migrated from Jenkins)
  stages:
    - stage:
        name: Security Scan
        failureStrategies:
          - onFailure:
              errors: [AllErrors]
              action:
                type: Abort
    - stage:
        name: Terraform Plan
        spec:
          execution:
            steps:
              - step:
                  name: TF Init
                  type: Run
                  spec:
                    command: terraform init
              - step:
                  name: TF Plan
                  type: Run
                  spec:
                    command: terraform plan -no-color
    - stage:
        name: Approval Gate
        type: Approval
        spec:
          execution:
            steps:
              - step:
                  type: HarnessApproval
                  spec:
                    approvers:
                      userGroups: [sre-team]
                    minimumCount: 1
    - stage:
        name: Terraform Apply
        spec:
          execution:
            steps:
              - step:
                  name: TF Apply
                  type: Run
                  spec:
                    command: terraform apply -auto-approve
```

### Jenkins vs Harness Comparison

| Feature | Jenkins | Harness |
|---------|---------|---------|
| Pipeline language | Groovy DSL | YAML (simpler) |
| Plugin management | 500+ plugins, frequent conflicts | Built-in steps, managed |
| Secrets management | Jenkins credentials (basic) | Enterprise secrets manager |
| Approval gates | input{} step (basic) | Rich approval with RBAC |
| Deployment strategies | Manual scripting | Built-in canary/blue-green |
| Rollback | Manual | Automatic on health check failure |
| Audit trail | Build logs only | Full deployment audit trail |
| Cost tracking | None | Built-in per pipeline |
| AI assistance | None | Harness AIDA |
| Multi-cloud | Plugins required | Native AWS/Azure/GCP |
| Kubernetes | Jenkins K8s plugin | Native K8s steps |
| Governance | None built-in | OPA policies built-in |
| RBAC | Basic | Enterprise RBAC |
| Maintenance | High (your responsibility) | Low (SaaS managed) |
| High availability | Manual setup | Built-in |

### Migration Risk Assessment
```
Low risk to migrate:
  Simple build pipelines (compile, test, package)
  Static analysis and security scanning
  Artifact publishing
  Notification steps

Medium risk to migrate:
  Complex Groovy shared libraries
  Custom Jenkins plugins with no Harness equivalent
  Integration tests with external dependencies

High risk — plan carefully:
  Pipelines with complex conditional logic
  Pipelines integrated with legacy on-premises systems
  Pipelines running on Windows agents (Delegate is Linux)
  Pipelines with custom workspace management

Migration approach:
  Phase 1: Run Harness and Jenkins in parallel (4 weeks)
  Phase 2: New services go to Harness only (4 weeks)
  Phase 3: Migrate existing services one team at a time (8 weeks)
  Phase 4: Decommission Jenkins (4 weeks)
  Total: 20 weeks for safe enterprise migration
```

---

## Day 4 — CD + Kubernetes Deployments

### Harness CD Entities
```
Service:
  What you are deploying
  Contains: Docker image, K8s manifests, Helm chart
  Version controlled in Git
  Parameterized with expressions

Environment:
  Where you are deploying
  dev, staging, prod
  Contains: infrastructure definition
  Can have environment-specific overrides

Infrastructure Definition:
  How to connect to the environment
  Kubernetes cluster + namespace
  Or: AWS ECS, Lambda, EC2, Azure Web App, etc

Pipeline:
  Orchestrates: Service + Environment + Infrastructure
  Contains: stages, steps, approval gates, policies
```

### Bank Platform CD Pipeline
```
4 services deployed:
  accounts-service  → accounts namespace
  payments-service  → payments namespace
  fraud-service     → fraud namespace
  notification-svc  → notifications namespace

Per service pipeline:
  Stage 1: Deploy to dev (automatic on merge)
    rolling deployment
    wait for pods Ready
    smoke test: curl health endpoint
    if fails: auto rollback to previous

  Stage 2: Approval gate
    SRE team approves
    sees: what changed, test results, cost impact
    timeout: 24 hours (then auto-reject)

  Stage 3: Deploy to staging
    canary: 10% → 100%
    integration tests
    auto rollback if error rate > 1%

  Stage 4: Approval gate
    Platform team + SRE both approve
    OPA policy enforces two approvers
    Deployment freeze check

  Stage 5: Deploy to production
    blue-green deployment
    Dynatrace monitors for 10 minutes
    auto rollback if SLO breached
```

### Deployment Freeze Windows
```yaml
# Harness deployment freeze
freeze:
  name: weekend-freeze
  windows:
    - timeZone: "Europe/London"
      startTime: "2024-01-05 17:00"
      duration: 64h  # Friday 5pm to Monday 9am
      recurrence:
        type: Weekly

# Bank regulatory requirement:
# No production deployments Friday 5pm to Monday 9am
# No production deployments during quarter-end (last 3 days)
# Emergency deployments require CISO approval
```

---

## Day 5 — Advanced Deployment Strategies

### Canary Deployment
```
What: gradually shift traffic to new version
When: high-risk changes, payment services, APIs

Flow:
  Old version: 100% traffic (stable)
       ↓
  Deploy new version alongside old
       ↓
  10% traffic → new version
  90% traffic → old version
  Monitor for 5 minutes
       ↓
  If healthy: 25% → new version
  If errors: rollback instantly, 0 users affected
       ↓
  25% → 50% → 100%
  Each step: 5 minute observation window
       ↓
  Old version decommissioned

Bank use case:
  New fraud detection algorithm
  New payment processing logic
  Any change touching money movement
```

### Blue-Green Deployment
```
What: two identical environments, instant traffic switch
When: zero-downtime requirements, instant rollback needed

Flow:
  Blue environment: current production (100% traffic)
  Green environment: new version (0% traffic)
       ↓
  Deploy new version to Green
  Run smoke tests on Green (no real traffic yet)
       ↓
  Switch: 100% traffic → Green instantly
  Blue stays alive for 30 minutes
       ↓
  If issues detected: switch back to Blue in seconds
  If healthy after 30 mins: decommission Blue

Bank use case:
  Major release with database migrations
  Regulatory-required changes (must be reversible)
  UI redesigns
```

### Rolling Deployment
```
What: replace pods one by one
When: stateless services, default choice

Flow:
  3 pods running v1: [v1] [v1] [v1]
       ↓
  Replace pod 1: [v2] [v1] [v1]
  Wait for v2 pod to be Ready
       ↓
  Replace pod 2: [v2] [v2] [v1]
  Wait for Ready
       ↓
  Replace pod 3: [v2] [v2] [v2]
  Done

Configurable:
  maxSurge: 1 (create 1 extra pod during rollout)
  maxUnavailable: 0 (never have fewer than desired)

Bank use case:
  Notification service (stateless, low risk)
  Configuration updates
  Minor bug fixes
```

### Feature Flags
```
What: deploy code without activating it
When: A/B testing, gradual feature rollout, kill switch needed

Bank use case:
  New SMS provider deployed to ALL users
  Feature flag controls who sees it:
    5% of users → new SMS provider
    95% of users → old SMS provider
  Monitor: delivery rate, latency, errors
  If good: increase to 25% → 50% → 100%
  If bad: flip flag OFF instantly
    no deployment needed to roll back
    instant kill switch

Code pattern:
  if (featureFlag.isEnabled("new-sms-provider", userId)) {
    sendViaTwilio(message)
  } else {
    sendViaLegacy(message)
  }
```

---

## Day 6 — Governance + OPA Policies

### Open Policy Agent (OPA)
```
What: policy-as-code engine
Language: Rego (declarative policy language)
How Harness uses it:
  Every pipeline step evaluated against policies
  Policy violation = step blocked
  Policy pass = step proceeds
  All decisions logged for audit
```

### Production Approval Policy
```rego
# opa-policies/prod-requires-two-approvals.rego
package pipeline

# Block production deployment without 2 approvals
deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  count(input.approvals) < 2
  msg := "Production deployment requires minimum 2 approvals"
}

# Block self-approval (dev cannot approve their own code)
deny[msg] {
  input.pipeline.triggeredBy == input.approvals[_].approvedBy
  msg := "Cannot approve your own deployment"
}
```

### Checkov Gate Policy
```rego
# opa-policies/checkov-gate.rego
package pipeline

# Block deployment if Checkov has HIGH severity findings
deny[msg] {
  input.securityScan.severity == "HIGH"
  input.securityScan.status == "FAILED"
  msg := sprintf("Blocked: Checkov HIGH finding: %s", [input.securityScan.checkId])
}
```

### Business Hours Policy
```rego
# opa-policies/business-hours.rego
package pipeline

# Block production deployments outside business hours
deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  hour := time.clock(time.now_ns())[0]
  hour < 9
  msg := "Production deployments only allowed 9am-5pm Monday-Friday"
}

deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  hour := time.clock(time.now_ns())[0]
  hour >= 17
  msg := "Production deployments only allowed 9am-5pm Monday-Friday"
}
```

### Resource Limits Policy
```rego
# opa-policies/k8s-resource-limits.rego
package pipeline

# Block K8s deployment without resource limits
deny[msg] {
  container := input.manifest.spec.template.spec.containers[_]
  not container.resources.limits.memory
  msg := sprintf("Container %s missing memory limit", [container.name])
}

deny[msg] {
  container := input.manifest.spec.template.spec.containers[_]
  not container.resources.limits.cpu
  msg := sprintf("Container %s missing CPU limit", [container.name])
}
```

### Pipeline Template (Reusable CI)
```yaml
# .harness/templates/ci-template.yaml
# One template, used by all 4 bank microservices
template:
  name: Bank Service CI Template
  identifier: bank_service_ci
  versionLabel: v1.0
  type: Stage
  spec:
    type: CI
    spec:
      steps:
        - step:
            name: Checkov Security Scan
            type: Security
        - step:
            name: Unit Tests
            type: Run
            spec:
              command: pytest tests/ -v
        - step:
            name: Build Docker Image
            type: BuildAndPushDockerRegistry
        - step:
            name: Notify Slack
            type: SlackNotify
            when:
              condition: <+pipeline.status> == "Failed"
```

---

## Day 7 — GitOps with Harness

### GitOps vs Pipeline-based CD

| Aspect | Pipeline CD (Push) | GitOps (Pull) |
|--------|-------------------|---------------|
| How it works | Pipeline pushes to cluster | Agent pulls from Git |
| Trigger | Pipeline execution | Git commit |
| Source of truth | Pipeline configuration | Git repository |
| Drift detection | Manual/scheduled | Automatic continuous |
| Rollback | Re-run pipeline | Revert Git commit |
| Audit trail | Pipeline logs | Git history |
| Bank compliance | Good | Better (immutable Git history) |
| Best for | Complex deployments | Simple K8s manifests |

### Harness GitOps vs Argo CD

| Feature | Argo CD | Harness GitOps |
|---------|---------|----------------|
| Open source | Yes (CNCF) | No (commercial) |
| UI | Good | Better (unified with CI) |
| RBAC | Basic | Enterprise |
| Multi-cluster | Yes | Yes |
| ApplicationSets | Yes | Yes |
| OPA policies | Separate setup | Built-in |
| Cost tracking | No | Yes (via CCM) |
| AI assistance | No | Yes (AIDA) |
| Support | Community | Enterprise SLA |
| Migration from Argo CD | N/A | Supported |

### GitOps Agent on dd-stg
```bash
# Install Harness GitOps Agent on kind cluster
kubectl apply -f harness-gitops-agent.yaml

# Verify
kubectl get pods -n harness-gitops
# harness-gitops-agent-xxxxx   Running

# Create Application for accounts-service
# Points to: github.com/pavantechy09-hub/cloud-iac-learning
# Path: day5-kubernetes/manifests/accounts/
# Target: accounts namespace on dd-stg

# Any push to manifests/accounts/ triggers sync automatically
# No pipeline needed — Git commit IS the deployment trigger
```

### When to Use Pipeline vs GitOps
```
Use Pipeline CD when:
  You need terraform apply (stateful operations)
  You need database migrations before deployment
  You need complex multi-step approvals
  You need integration tests that require external systems
  Deployment order matters across multiple services

Use GitOps when:
  Pure Kubernetes manifest deployments
  Config changes (ConfigMap, Secret updates)
  Compliance requires immutable audit trail
  Teams want to self-service their own deployments
  Drift detection and auto-reconciliation required

Bank pattern (both together):
  Terraform infrastructure → Pipeline CD
  K8s application deployments → GitOps
  This is the enterprise standard
```

---

## Day 8 — AIOps + Harness AIDA + SRM

### Harness AIDA (AI Development Assistant)
```
What it does:
  Analyzes pipeline failures automatically
  Explains root cause in plain English
  Suggests exact fix with code snippet
  Available in CI, CD, and SRM

Example:
  Pipeline failed at Terraform Apply step
  AIDA output:
    "Your pipeline failed because:
     RDS DB Subnet Group operation is not supported
     by your Floci emulator version.
     
     Root cause: aws_db_subnet_group resource requires
     CreateDBSubnetGroup API which Floci v1.5.23 does not support.
     
     Fix option 1: Remove db_subnet_group_name from aws_db_instance
     Fix option 2: Upgrade Floci to version 2.x (if available)
     Fix option 3: Skip this resource and document limitation
     
     Similar issue in your repository: day6-databases/main.tf:33"

Compared to K8sGPT:
  K8sGPT: analyzes Kubernetes cluster issues
  Harness AIDA: analyzes pipeline failures
  Both use LLM backend
  Both explain in plain English
  Together: complete AIOps coverage
```

### SLO and Error Budgets
```
SLI (Service Level Indicator):
  The metric you measure
  Example: fraction of HTTP requests returning 200

SLO (Service Level Objective):
  The target you commit to
  Example: 99.9% of requests return 200

SLA (Service Level Agreement):
  The contract with the customer
  Example: if SLO breached, customer gets credit

Error Budget:
  How much failure you can afford
  99.9% SLO = 0.1% failure allowed
  Per month = 43.8 minutes of downtime allowed

Bank SLOs configured in Harness SRM:
  accounts-service: 99.95% (21 min/month budget)
  payments-service: 99.99% (4.3 min/month budget)
  fraud-service:    99.9%  (43.8 min/month budget)
  notification-svc: 99.5%  (3.6 hours/month budget)

Error budget gates:
  > 50% budget consumed → deployment warning
  > 75% budget consumed → deployments require extra approval
  > 90% budget consumed → deployments blocked automatically
  100% consumed → incident review required before any deploy
```

### Dynatrace + Harness Integration
```
How it works:
  Harness sends deployment event to Dynatrace
  Dynatrace marks deployment on all dashboards
  Dynatrace monitors metrics post-deployment
  If metrics degrade → Dynatrace sends alert to Harness
  Harness triggers automatic rollback

Configuration:
  Harness pipeline step: "Send Deployment Event to Dynatrace"
  Dynatrace alert: "Error rate increased after deployment"
  Harness webhook listener: receives Dynatrace alert
  Harness action: rollback to previous version

Result:
  No human needed for rollback decision
  Dynatrace Davis AI detects the problem
  Harness executes the fix
  SRE wakes up to: "Deployment rolled back automatically
                    Root cause: error rate increased from 0.1% to 3.2%
                    after payments-service v2.1.3 deployment at 14:03"
```

---

## Day 9 — FinOps + Cloud Cost Management

### What is FinOps
```
FinOps = Financial Operations for cloud
The practice of bringing financial accountability
to the variable spend model of cloud

Three phases:
  Inform:   see what you are spending and why
  Optimize: find waste and fix it
  Operate:  continuous cost optimization as culture

Without FinOps (common problems):
  "Who spent $47,000 on RDS last month?"
  "Why did our AWS bill double this quarter?"
  "Which team is responsible for these orphaned resources?"
  "Are we using reserved instances efficiently?"

With Harness CCM:
  Cost per service: payments-service costs $234/day
  Cost per deployment: this deployment costs $0.47
  Cost per team: payments team spent $12,400 this month
  Anomaly detected: fraud-service cost increased 340% today
    root cause: Lambda running 10x more due to SQS backlog
```

### Cost Allocation
```
Every resource tagged in Terraform (your Day 2 work):
  Environment = "prod"
  Service     = "payments-service"
  Team        = "payments-team"
  CostCenter  = "CC-2847"

Harness CCM reads these tags:
  Shows cost breakdown by tag
  Payments team dashboard: see only your costs
  Platform team dashboard: see all costs
  Anomaly alerts: costs outside normal range

Showback vs Chargeback:
  Showback: show teams their costs (informational)
  Chargeback: actually bill teams for their cloud usage
    requires internal billing system integration
    enterprises use this to drive cost accountability
```

### Cost Optimization Actions
```
Harness CCM recommendations:

Right-sizing:
  "accounts-service pods requesting 2 CPU but using 0.3 CPU average
   Recommendation: reduce CPU request to 0.5
   Estimated savings: $180/month"

Reserved instances:
  "Your RDS accounts-db has run for 180 days continuously
   On-demand cost: $234/month
   Reserved instance cost: $134/month
   Recommendation: purchase 1-year reserved instance
   Estimated savings: $1,200/year"

Spot instances:
  "fraud-service is stateless and can tolerate interruption
   Recommendation: move to Spot instances
   Estimated savings: 70% ($890/month)"

Idle resources:
  "dev environment running 24/7
   Usage: weekdays 9am-6pm only
   Recommendation: schedule shutdown nights + weekends
   Estimated savings: $340/month"
```

---

## Day 10 — Enterprise Capstone + 90-Day Migration Plan

### 90-Day Migration Plan

#### Phase 1 — Foundation (Days 1-30)
```
Week 1-2: Setup and Proof of Concept
  Install Harness Delegates in non-prod clusters
  Migrate 1 non-critical service as proof of concept
  Run Jenkins and Harness in parallel
  Document comparison: speed, reliability, features
  Get stakeholder sign-off

Week 3-4: Team Training
  Platform engineering team: full Harness training (3 days)
  SRE team: approval workflows and SLO configuration (1 day)
  Development leads: pipeline YAML basics (half day)
  Security team: OPA policy review (1 day)
  Create internal runbooks and wiki

Month 1 success criteria:
  Delegate installed and stable in dev/staging
  1 service fully migrated end to end
  All teams trained
  OPA policies reviewed and approved
  Rollback procedure documented and tested
```

#### Phase 2 — Migration (Days 31-60)
```
Week 5-6: New Services Go Harness-Only
  Any new microservice → Harness from day 1
  No new Jenkins pipelines created
  Templates created for common patterns
  STO security scanning enabled for all new services

Week 7-8: Existing Services Migration (batch 1)
  Migrate lowest-risk services first
  Non-payment, non-critical services
  Each migration: 1-2 days per service
  Jenkins pipeline kept as fallback for 2 weeks
  After 2 weeks stable: remove Jenkins pipeline

Month 2 success criteria:
  50% of services on Harness
  Zero Jenkins pipelines for new services
  Deployment frequency increased (measure)
  MTTR decreased (measure)
  No production incidents from migration
```

#### Phase 3 — Completion (Days 61-90)
```
Week 9-10: Critical Services Migration
  payments-service migration (highest risk)
  Extra validation: 4-week parallel run
  Canary deployment strategy enabled
  Dynatrace integration verified
  Rollback tested in staging

Week 11-12: Jenkins Decommission
  All services confirmed stable on Harness
  Jenkins read-only for historical logs
  Redirect all webhooks to Harness triggers
  Jenkins server scheduled for decommission
  Cost saving: $X/month Jenkins infrastructure

Month 3 success criteria:
  100% services on Harness
  Jenkins decommissioned
  OPA governance enforced on all pipelines
  SLOs configured for all critical services
  Error budgets visible to all teams
  Cost per service visible to all teams
  Audit trail complete for compliance review
```

### Risk Register
```
Risk 1: Pipeline failure during migration
  Probability: Medium
  Impact: High (production outage)
  Mitigation: Run parallel for 2 weeks, instant rollback to Jenkins
  Owner: Platform Engineer

Risk 2: Team resistance to change
  Probability: Medium
  Impact: Medium (slow adoption)
  Mitigation: Early involvement, training, clear benefits demo
  Owner: Engineering Manager

Risk 3: Harness SaaS outage
  Probability: Low
  Impact: High (no deployments possible)
  Mitigation: Harness SLA 99.9%, emergency kubectl apply runbook
  Owner: SRE team

Risk 4: OPA policy blocks legitimate deployment
  Probability: Medium
  Impact: Medium (delayed release)
  Mitigation: Policy testing in dev first, override procedure defined
  Owner: Security team

Risk 5: Cost overrun on Harness licensing
  Probability: Low
  Impact: Medium
  Mitigation: CCM monitoring, service tier right-sizing
  Owner: FinOps team
```

### Cost Comparison: Jenkins vs Harness
```
Current Jenkins cost:
  2x Jenkins master servers: $400/month
  4x Jenkins agent servers: $800/month
  Jenkins admin time: 0.5 FTE = $3,000/month
  Plugin maintenance: 8 hours/month = $400/month
  Total: $4,600/month

Harness cost (enterprise):
  Harness SaaS: ~$2,000/month (50 services)
  Delegate infrastructure (minimal): $200/month
  Admin time: 0.1 FTE = $600/month
  Total: $2,800/month

Net saving: $1,800/month = $21,600/year
Plus: faster deployments, fewer incidents, better compliance
ROI: Positive in month 3
```

---

## Tools + Technology Stack

| Tool | Purpose | Free Tier |
|------|---------|-----------|
| Harness | Enterprise CI/CD platform | Yes — app.harness.io |
| Floci | AWS emulator (localhost:4566) | Yes — your existing setup |
| floci-az | Azure emulator (localhost:4577) | Yes — your existing setup |
| kind dd-stg | Local Kubernetes cluster | Yes — your existing setup |
| K8sGPT + Ollama | Open source AIOps | Yes — your existing setup |
| Dynatrace | Enterprise APM + AIOps | 15-day trial |
| OPA | Policy engine | Yes — open source |
| Terraform | Infrastructure as Code | Yes — your existing setup |
| Bicep | Azure IaC | Yes — your existing setup |

---

## Interview Questions and Answers

### Harness Fundamentals

**Q: What is Harness and how does it differ from GitHub Actions?**

Harness is an enterprise CD platform built specifically for production-grade continuous delivery. GitHub Actions is excellent for CI but hits limits for enterprise CD. Harness adds built-in canary and blue-green deployment strategies with automatic rollback, OPA governance enforced on every pipeline, SLO tracking with error budgets, cloud cost management, and AI assistance through AIDA. The key difference is that Harness treats the deployment itself as a first-class concern — not just running scripts. It knows what a healthy deployment looks like, monitors it, and rolls back automatically if health checks fail.

**Q: What is a Harness Delegate and why is it needed?**

A Delegate is an agent pod running inside your Kubernetes cluster or on your infrastructure. It polls Harness SaaS every 10 seconds for tasks and executes them locally. This means your cluster never needs to be publicly accessible, your credentials stay inside your network, and Harness never needs inbound network access. It is conceptually similar to a GitHub Actions self-hosted runner but smarter — Delegates auto-select based on tags, auto-upgrade, and provide high availability when multiple Delegates are deployed.

**Q: Explain the Harness entity hierarchy.**

Account is the top level representing your organisation's Harness login. Under that you create Organisations which typically map to business units or divisions. Under each Organisation you create Projects which are collections of related pipelines and services. Within a Project you define Services (what to deploy), Environments (where to deploy), Infrastructure Definitions (how to connect), and Pipelines (orchestration). This hierarchy allows fine-grained RBAC — a developer might have access to one Project but not another.

### Deployment Strategies

**Q: When would you use canary vs blue-green vs rolling deployment?**

Canary is best for high-risk changes to critical services like payments where you want to gradually expose a small percentage of real users to the new version and monitor closely before committing. Blue-green is best when you need instant rollback capability and zero downtime — you deploy a complete new environment and switch traffic instantly, keeping the old environment alive for quick reversion. Rolling is the default for stateless services where you can tolerate brief mixed-version periods. In the bank platform I used canary for payments-service due to the financial risk, blue-green for accounts-service for compliance reasons requiring instant rollback, and rolling for fraud-service and notification-service as lower-risk stateless components.

**Q: What is an error budget and how does it affect deployments?**

An error budget is the amount of failure you can afford while still meeting your SLO. If accounts-service has a 99.9% SLO, it can afford 43.8 minutes of downtime per month — that is the error budget. As the budget is consumed by incidents, deployments become progressively restricted. In our Harness SRM configuration, consuming over 75% of the error budget requires extra approval for any deployment, and consuming over 90% blocks deployments entirely. This creates a feedback loop — teams that cause incidents burn their own budget and lose the ability to deploy new features until they stabilise.

**Q: How does Harness implement automatic rollback?**

Harness monitors deployment health through configured health sources — Kubernetes pod readiness, HTTP health endpoint checks, or third-party metrics from Dynatrace or Prometheus. After a deployment, Harness enters a verification phase and continuously checks these health sources for a configured window, typically 5 to 10 minutes. If any health source reports degradation beyond the configured threshold, Harness automatically triggers rollback without human intervention. The rollback redeploys the previous artifact version using the same deployment strategy. In production this can reduce MTTR from 45 minutes of manual investigation to under 5 minutes of automated recovery.

### Governance and Compliance

**Q: What is OPA and how does Harness use it?**

Open Policy Agent is a policy-as-code engine using a declarative language called Rego. Harness evaluates every pipeline step against configured OPA policies before execution. We used this to enforce: production deployments requiring two approvers from different teams, no self-approval of your own code, deployment blocked if Checkov finds HIGH severity findings, no production deployments outside business hours, and mandatory resource limits on all Kubernetes deployments. The policies are stored as code in Git giving a full audit trail of every governance decision.

**Q: How do you implement four-eyes principle in a deployment pipeline?**

Four-eyes principle means no single person can deploy to production alone — two people must approve. In Harness this is implemented through the Approval step with minimumCount set to 2 and the OPA policy blocking self-approval. Additionally we configure the approval to require approvers from different user groups — the deploying developer's team and the SRE team — so neither can approve alone. All approvals are logged with timestamp, approver identity, and comment, providing the audit trail that compliance teams require. This directly replaces the email approval chains that Jenkins teams typically use.

### Migration

**Q: How would you approach migrating from Jenkins to Harness?**

I follow a phased approach over 90 days. Phase one is foundation — install Harness Delegates in non-production environments, migrate one non-critical service as a proof of concept, run Jenkins and Harness in parallel, and train all teams. Phase two is migration — new services go Harness-only from day one, then existing services migrate in batches starting with lowest risk, with each Jenkins pipeline kept as fallback for two weeks before removal. Phase three is completion — migrate critical services like payments with extended parallel running and validated rollback testing, then decommission Jenkins once all services are stable. The key principle is never leaving teams without a rollback option during the transition.

**Q: What are the main risks in a Jenkins to Harness migration?**

The highest technical risk is pipeline failure during the migration window when teams might be without a working deployment path. Mitigated by running parallel systems and having clear rollback procedures to Jenkins. The highest organisational risk is team resistance — developers comfortable with Jenkinsfiles may resist YAML pipelines. Mitigated by involving teams early, providing training, and demonstrating concrete benefits like faster deployments and automatic rollback. A genuine technical constraint is that Harness Delegates are Linux-based, so Windows build agents require a different approach — either running Windows containers or keeping those specific builds on Jenkins during initial migration.

### AIOps and SRE

**Q: How does Harness AIDA differ from K8sGPT?**

They solve different problems at different layers. K8sGPT analyzes Kubernetes cluster health — it scans pod states, events, and resource configurations and explains issues like OOMKilled or ImagePullBackOff in plain English using a local LLM. Harness AIDA analyzes pipeline failures — it reads step logs, error messages, and pipeline context to explain why a build or deployment failed and suggests the exact fix. In production I would use both together: K8sGPT for cluster-level diagnosis and Harness AIDA for pipeline-level diagnosis. They complement each other rather than compete.

**Q: What is the difference between SLI, SLO, and SLA?**

An SLI is the Service Level Indicator — the actual metric you measure, such as the fraction of HTTP requests returning 200 status codes. An SLO is the Service Level Objective — the target value for that SLI you commit to internally, such as 99.9% of requests must succeed. An SLA is the Service Level Agreement — the external contract with customers that typically carries financial penalties if breached, such as crediting customers if availability drops below 99.5%. In our bank platform we configure SLIs and SLOs in Harness SRM, which tracks error budgets and automatically gates deployments when budgets are running low, before any SLA violation can occur.

### FinOps

**Q: How do you implement cost visibility per service in Harness?**

Cost visibility starts in Terraform — every resource is tagged with Service, Team, Environment, and CostCenter tags. Harness CCM reads these tags from AWS and Azure APIs and presents cost breakdowns by tag. Each team sees a dashboard showing their own service costs by day, week, and month. Anomaly detection alerts when a service cost increases abnormally — we used this to catch a Lambda function running 10x more than expected due to an SQS backlog, which was costing $890/day in unexpected charges. Harness also provides right-sizing recommendations, showing where pods request far more CPU or memory than they actually use, and reserved instance recommendations for resources that run continuously.

---

## Floci Limitations for Harness Training

| Feature | Floci Support | Notes |
|---------|--------------|-------|
| Terraform steps | Supported | Same as cloud-iac-learning |
| K8s deployments | Supported via dd-stg | Full deployment strategies |
| AWS connector | Supported | Floci as AWS endpoint |
| Lambda steps | Supported | Day 4 Lambda deploy |
| RDS operations | Partial | Same limitations as Day 6 |
| Azure connector | Partial | floci-az limitations |
| Cost data | Not supported | CCM needs real cloud data |
| Dynatrace | Needs trial | 15-day free trial |

---

## Setup Instructions

### Prerequisites
```
Existing from cloud-iac-learning:
  Docker Desktop running
  Floci + floci-az containers running
  kind dd-stg cluster running
  kubectl configured for kind-dd-stg
  Terraform installed
  K8sGPT + Ollama running

New requirements:
  Harness free account: app.harness.io
  Harness CLI (optional): brew install harness/tap/harness
```

### Start Environment
```powershell
# Start everything
. D:\cloud-iac\start-env.ps1

# Verify
docker ps          # Floci containers running
kubectl get nodes  # dd-stg cluster healthy
k8sgpt version     # AIOps tools ready
```

### Harness Delegate Installation
```bash
# From Harness UI: Project Setup → Delegates → New Delegate
# Choose: Kubernetes → copy Helm command

helm repo add harness https://app.harness.io/storage/harness-download/harness-helm-charts/
helm install harness-delegate harness/harness-delegate \
  --namespace harness-delegate-ng \
  --create-namespace \
  --set delegateName=dd-stg-delegate \
  --set accountId=YOUR_ACCOUNT_ID \
  --set delegateToken=YOUR_TOKEN \
  --set managerEndpoint=https://app.harness.io \
  --set delegateDockerImage=harness/delegate:latest

# Verify
kubectl get pods -n harness-delegate-ng
```

---

## Key Metrics to Track

```
Deployment frequency:
  Before Harness (Jenkins): X deployments/week
  After Harness: Y deployments/week
  Target: 2-3x increase

MTTR (Mean Time To Recovery):
  Before: 45 minutes average
  After: under 10 minutes (auto-rollback)
  Target: 80% reduction

Lead time for changes:
  Before: code merged → production in 3 days
  After: code merged → production in 4 hours
  Target: 75% reduction

Change failure rate:
  Before: 15% of deployments cause incidents
  After: under 5% (canary catches issues early)
  Target: 67% reduction

These four metrics = DORA metrics
The industry standard for measuring DevOps performance
Senior engineers are expected to know and track these
```

---

## What This Portfolio Proves

```
Combined portfolio after both repos:

cloud-iac-learning (10 days):
  Infrastructure: Terraform, Bicep, AWS, Azure, Kubernetes
  Security: IAM, RBAC, Checkov, Secrets Manager
  Monitoring: CloudWatch, Azure Monitor, K8sGPT AIOps
  CI/CD: GitHub Actions, OIDC, drift detection

harness-enterprise-training (10 days):
  Enterprise CD: Harness pipelines, Delegates, Connectors
  Migration: Jenkins → Harness with documented plan
  Deployment strategies: Canary, Blue-Green, Rolling, Feature Flags
  Governance: OPA policies, four-eyes, deployment freeze
  GitOps: Harness GitOps, comparison with Argo CD
  AIOps: Harness AIDA, SLOs, error budgets, Dynatrace integration
  FinOps: Cost per service, anomaly detection, optimization

Job roles this covers:
  DevOps Engineer          ← both repos
  Platform Engineer        ← both repos
  SRE                      ← monitoring + SLOs + error budgets
  Cloud Engineer           ← Terraform + Bicep + multi-cloud
  Release Engineer         ← Harness + deployment strategies
  FinOps Engineer          ← CCM + cost optimization

Seniority level demonstrated:
  The combination shows junior-to-senior progression
  Junior: can build infrastructure (cloud-iac-learning)
  Senior: can design enterprise delivery platform (harness-training)
  Lead: can plan and execute migration (Day 10 capstone)
```

---

## Connect

- **GitHub:** [pavantechy09-hub](https://github.com/pavantechy09-hub)
- **LinkedIn:** [linkedin.com/in/pavan-goli](https://linkedin.com/in/pavan-goli)
- **Email:** pavantechy09@gmail.com
- **Portfolio:** [pavantechy09-hub.github.io/cloud-iac-learning](https://pavantechy09-hub.github.io/cloud-iac-learning)
