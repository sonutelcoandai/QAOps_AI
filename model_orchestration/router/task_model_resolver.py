from model_orchestration.router.model_router import ModelRouter

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.fallback.fallback_manager import FallbackManager


class TaskModelResolver:
    @staticmethod
    def resolve(task_name):

        model_name = ModelRouter.get_model_for_task(task_name)

        model_name = FallbackManager.resolve_model(model_name)

        model_details = ModelRegistry.get_model(model_name)

        return {
            "model_name": model_name,
            "provider": model_details["provider"],
            "strengths": model_details["strengths"],
        }
