from security.security_service import SecurityService

print(SecurityService.evaluate("workflow_execution"))

print(SecurityService.evaluate("production_deployment"))

print(SecurityService.evaluate("unknown_operation"))
