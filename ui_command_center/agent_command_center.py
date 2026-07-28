from evaluation.platform_evaluation_service import PlatformEvaluationService


class AgentCommandCenter:
    @staticmethod
    def generate():

        return {"platform_evaluation": PlatformEvaluationService.evaluate_platform()}
