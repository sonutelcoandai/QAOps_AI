from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_health_dashboard import IntegrationHealthDashboard

IntegrationCatalog.register("jira", "alm")

IntegrationCatalog.register("github", "scm")

IntegrationCatalog.register("postman", "api_testing")

print(IntegrationHealthDashboard.get_summary())
