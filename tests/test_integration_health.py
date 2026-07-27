from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_health_service import IntegrationHealthService

IntegrationCatalog.register("jira", "alm")

IntegrationCatalog.register("github", "scm")

print(IntegrationHealthService.check("jira"))

print(IntegrationHealthService.check("github"))

print(IntegrationHealthService.check("unknown"))
