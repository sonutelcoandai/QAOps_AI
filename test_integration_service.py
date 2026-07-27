from integrations.integration_service import IntegrationService

IntegrationService.register("jira")

IntegrationService.register("github")

print(IntegrationService.execute("jira"))

print(IntegrationService.execute("github"))
