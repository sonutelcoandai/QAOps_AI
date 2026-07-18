from pathlib import Path
import sys

from ai_providers.load_providers import load_providers

from orchestration.provider_manager import ProviderManager

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.fallback.fallback_manager import FallbackManager

from model_orchestration.collaboration.collaboration_manager import CollaborationManager

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

ModelRegistry.load()

RoutingPolicy.load()

FallbackManager.load()

ProviderManager.load()

load_providers()

result = CollaborationManager.execute_chain(
    ["test_case_generation", "automation_generation"],
    "Generate telecom validation assets",
)

print(result)
