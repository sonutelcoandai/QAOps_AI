from security.security_hardening_dashboard import SecurityHardeningDashboard


class SecurityPortfolioService:
    @staticmethod
    def generate():

        return {"security": SecurityHardeningDashboard.generate()}
