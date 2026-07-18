from pathlib import Path
import sys
from model_orchestration.registry.model_registry import ModelRegistry

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


ModelRegistry.load()

print(ModelRegistry.get_all_models())
