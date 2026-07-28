from marketplace.marketplace_portfolio_service import MarketplacePortfolioService


class MarketplaceCommandCenter:
    @staticmethod
    def generate():

        return {"marketplace": MarketplacePortfolioService.generate()}
