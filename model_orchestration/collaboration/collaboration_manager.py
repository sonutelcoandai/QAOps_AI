from ai_providers.provider_factory import ProviderFactory

from model_orchestration.router.model_router_engine import ModelRouterEngine


class CollaborationManager:
    @staticmethod
    def execute_chain(collaboration_steps, prompt):

        results = []

        for step in collaboration_steps:
            routing_result = ModelRouterEngine.resolve(task_name=step)

            provider = ProviderFactory.get_provider(routing_result["provider"])

            response = provider.generate(prompt)

            results.append(
                {
                    "task": step,
                    "model": routing_result["model_name"],
                    "provider": routing_result["provider"],
                    "response": response,
                }
            )

        return results
