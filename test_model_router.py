from pathlib import Path
import sys
from model_orchestration.router.model_router import ModelRouter

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


ModelRouter.load()

print(ModelRouter.get_model_for_task("test_case_generation"))

print(ModelRouter.get_model_for_task("automation_generation"))

print(ModelRouter.get_model_for_task("architecture_review"))
print(ModelRouter.get_model_for_task("unknown_task"))
