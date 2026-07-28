from integrations.integration_portfolio_service import IntegrationPortfolioService


class IntegrationsCommandCenter:
    @staticmethod
    def generate():

        return {"integrations": IntegrationPortfolioService.generate()}
