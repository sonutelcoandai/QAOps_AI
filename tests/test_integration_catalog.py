from integrations.integration_catalog import IntegrationCatalog

IntegrationCatalog.register("jira", "alm")

IntegrationCatalog.register("github", "scm")

IntegrationCatalog.register("postman", "api_testing")

print(IntegrationCatalog.get_all())
