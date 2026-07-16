from pathlib import Path
import sys
from ai_providers.load_providers import load_providers

from ai_providers.provider_factory import ProviderFactory

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_providers()

provider = ProviderFactory.get_provider("ollama")

response = provider.generate("Generate telecom test cases")

print(response)
