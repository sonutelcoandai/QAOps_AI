from pathlib import Path
import sys
from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.router.model_router import ModelRouter

from model_orchestration.fallback.fallback_manager import FallbackManager

from model_orchestration.policies.routing_policy import RoutingPolicy

from model_orchestration.router.model_router_engine import ModelRouterEngine

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

ModelRegistry.load()

ModelRouter.load()

RoutingPolicy.load()

FallbackManager.load()

result = ModelRouterEngine.resolve(task_name="automation_generation")

print(result)
