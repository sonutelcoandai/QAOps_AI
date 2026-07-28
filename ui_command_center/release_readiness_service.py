from evaluation.platform_evaluation_service import PlatformEvaluationService

from security.security_portfolio_service import SecurityPortfolioService


class ReleaseReadinessService:
    @staticmethod
    def evaluate():

        platform = PlatformEvaluationService.evaluate_platform()

        security = SecurityPortfolioService.generate()

        ready = platform["grade"] == "A"

        return {"release_ready": ready, "platform": platform, "security": security}
