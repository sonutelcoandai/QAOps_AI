from pathlib import Path
import sys
from ai_providers.load_providers import load_providers

from ai_providers.provider_registry import ProviderRegistry

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_providers()

print(ProviderRegistry.get_all())
