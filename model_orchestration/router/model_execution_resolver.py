from model_orchestration.router.model_router_engine import ModelRouterEngine

from ai_providers.provider_factory import ProviderFactory
from model_orchestration.benchmarking.benchmark_manager import BenchmarkManager


class ModelExecutionResolver:
    @staticmethod
    def execute(task_name, prompt):

        routing_result = ModelRouterEngine.resolve(task_name=task_name)

        provider_name = routing_result["provider"]

        provider = ProviderFactory.get_provider(provider_name)

        response = provider.generate(prompt)

        BenchmarkManager.record(
            task_name=task_name,
            provider=provider_name,
            model=routing_result["model_name"],
            success=True,
            latency_ms=0,
        )
        return {
            "task": task_name,
            "provider": provider_name,
            "model": routing_result["model_name"],
            "response": response,
        }
