from orchestration.config_manager import ConfigManager

from orchestration.provider_manager import ProviderManager

from feature_flags.feature_manager import FeatureManager

from ai_providers.load_providers import load_providers
from orchestration.agent_bootstrap import AgentBootstrap

from orchestration.framework_bootstrap import FrameworkBootstrap

from orchestration.knowledge_bootstrap import KnowledgeBootstrap

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.fallback.fallback_manager import FallbackManager
from orchestration.workflow_bootstrap import WorkflowBootstrap


class PlatformBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing QAOps-AI...\n")

        ConfigManager.initialize()

        FeatureManager.load()

        ProviderManager.load()

        load_providers()

        ModelRegistry.load()

        RoutingPolicy.load()

        FallbackManager.load()

        KnowledgeBootstrap.initialize()

        FrameworkBootstrap.initialize()

        AgentBootstrap.initialize()
        WorkflowBootstrap.initialize()

        print("\nQAOps-AI Ready\n")
