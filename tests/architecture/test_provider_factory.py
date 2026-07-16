from pathlib import Path
import sys

from ai_providers.provider_registry import ProviderRegistry

from ai_providers.provider_factory import ProviderFactory

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))


class DummyProvider:
    pass


ProviderRegistry.register("dummy", DummyProvider())

provider = ProviderFactory.get_provider("dummy")

print(type(provider).__name__)
