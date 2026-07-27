from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_portfolio_service import IntegrationPortfolioService

IntegrationCatalog.register("jira", "alm")

IntegrationCatalog.register("github", "scm")

IntegrationCatalog.register("postman", "api_testing")

print(IntegrationPortfolioService.generate())
