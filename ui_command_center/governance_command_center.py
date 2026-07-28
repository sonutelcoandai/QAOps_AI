from governance_analytics.governance_portfolio_service import GovernancePortfolioService


class GovernanceCommandCenter:
    @staticmethod
    def generate():

        return {"governance": GovernancePortfolioService.generate()}
