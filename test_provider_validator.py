from pathlib import Path
import sys
from ai_providers.load_providers import load_providers

from orchestration.provider_validator import ProviderValidator

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


load_providers()

print(ProviderValidator.is_available("ollama"))

print(ProviderValidator.is_available("claude"))
