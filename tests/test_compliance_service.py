from governance_analytics.compliance_service import ComplianceService

print(ComplianceService.evaluate("telecom_validation"))

print(ComplianceService.evaluate("release_readiness"))

print(ComplianceService.evaluate("unknown_workflow"))
