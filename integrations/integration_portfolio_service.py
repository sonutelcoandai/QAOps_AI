from integrations.integration_dashboard import IntegrationDashboard

from integrations.integration_portfolio import IntegrationPortfolio


class IntegrationPortfolioService:
    @staticmethod
    def generate():

        dashboard = IntegrationDashboard.generate()

        portfolio = IntegrationPortfolio(
            integrations=dashboard["integrations"], metrics=dashboard["metrics"]
        )

        return portfolio.to_dict()
