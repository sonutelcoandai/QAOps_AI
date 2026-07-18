from pathlib import Path
import sys
from model_orchestration.registry.model_registry import ModelRegistry

from model_orchestration.fallback.fallback_manager import FallbackManager

from ai_providers.load_providers import load_providers

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

ModelRegistry.load()

FallbackManager.load()

load_providers()

print(FallbackManager.resolve_model("claude"))
