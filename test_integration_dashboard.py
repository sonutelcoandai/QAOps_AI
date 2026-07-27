from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_lifecycle_service import IntegrationLifecycleService

from integrations.integration_dashboard import IntegrationDashboard

IntegrationCatalog.register("jira", "alm")

IntegrationCatalog.register("github", "scm")

IntegrationCatalog.register("postman", "api_testing")

IntegrationLifecycleService.deprecate("github")

print(IntegrationDashboard.generate())
