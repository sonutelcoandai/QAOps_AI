from pathlib import Path
import sys
from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.fallback.fallback_manager import FallbackManager

from orchestration.provider_manager import ProviderManager

from ai_providers.load_providers import load_providers

from model_orchestration.router.model_execution_resolver import ModelExecutionResolver


ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

ModelRegistry.load()

RoutingPolicy.load()

FallbackManager.load()

ProviderManager.load()

load_providers()

result = ModelExecutionResolver.execute(
    task_name="architecture_review", prompt="Generate telecom test cases"
)

print(result)
