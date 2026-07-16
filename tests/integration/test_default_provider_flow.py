from pathlib import Path
import sys
from orchestration.provider_manager import ProviderManager

from ai_providers.load_providers import load_providers

from ai_providers.provider_factory import ProviderFactory

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))


ProviderManager.load()

load_providers()

provider_name = ProviderManager.get_default_provider_name()

provider = ProviderFactory.get_provider(provider_name)

response = provider.generate("Generate telecom test cases")

print(response)
