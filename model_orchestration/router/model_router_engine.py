from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.policies.policy_resolver import PolicyResolver

from model_orchestration.fallback.fallback_manager import FallbackManager

from model_orchestration.registry.model_registry import ModelRegistry


class ModelRouterEngine:
    @staticmethod
    def resolve(task_name=None, agent_name=None, domain_name=None):

        strategy = RoutingPolicy.get_strategy()

        model_name = None

        if strategy == "task_based":
            model_name = PolicyResolver.resolve_task_model(task_name)

        elif strategy == "agent_based":
            model_name = PolicyResolver.resolve_agent_model(agent_name)

        elif strategy == "domain_based":
            model_name = PolicyResolver.resolve_domain_model(domain_name)

        model_name = FallbackManager.resolve_model(model_name)

        return {
            "model_name": model_name,
            "provider": ModelRegistry.get_model(model_name)["provider"],
        }
