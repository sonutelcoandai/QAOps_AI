from pathlib import Path
import sys
from model_orchestration.router.model_router import ModelRouter

from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.router.task_model_resolver import TaskModelResolver

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


ModelRegistry.load()

ModelRouter.load()

result = TaskModelResolver.resolve("architecture_review")

print(result)
