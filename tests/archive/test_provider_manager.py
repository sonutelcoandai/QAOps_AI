from pathlib import Path
import sys
from orchestration.provider_manager import ProviderManager

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))


ProviderManager.load()

print(ProviderManager.get_provider_config("ollama"))
