from security.security_portfolio_service import SecurityPortfolioService


class SecurityCommandCenter:
    @staticmethod
    def generate():

        return {"security": SecurityPortfolioService.generate()}
