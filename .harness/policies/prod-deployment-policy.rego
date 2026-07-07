package pipeline

# Block prod without 2 approvals
deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  count(input.approvals) < 2
  msg := "Production requires minimum 2 approvals (four-eyes principle)"
}

# Block self-approval
deny[msg] {
  input.pipeline.triggeredBy == input.approvals[_].approvedBy
  msg := "Cannot approve your own deployment"
}

# Block outside business hours (9am-5pm)
deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  hour := time.clock(time.now_ns())[0]
  hour >= 17
  msg := "Production deployments only 9am-5pm Monday-Friday"
}

deny[msg] {
  input.pipeline.stages[_].stage.spec.environment.identifier == "prod"
  hour := time.clock(time.now_ns())[0]
  hour < 9
  msg := "Production deployments only 9am-5pm Monday-Friday"
}

# Block if Checkov HIGH findings
deny[msg] {
  input.securityScan.status == "FAILED"
  input.securityScan.severity == "HIGH"
  msg := sprintf("HIGH security finding blocks deployment: %s", [input.securityScan.checkId])
}

# Block K8s deployments without resource limits
deny[msg] {
  container := input.manifest.spec.template.spec.containers[_]
  not container.resources.limits.memory
  msg := sprintf("Container %s missing memory limit", [container.name])
}
