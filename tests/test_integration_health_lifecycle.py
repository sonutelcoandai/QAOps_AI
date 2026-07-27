from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_lifecycle_service import IntegrationLifecycleService

from integrations.integration_health_service import IntegrationHealthService

IntegrationCatalog.register("jira", "alm")

print(IntegrationHealthService.check("jira"))

IntegrationLifecycleService.deprecate("jira")

print(IntegrationHealthService.check("jira"))

IntegrationLifecycleService.retire("jira")

print(IntegrationHealthService.check("jira"))
