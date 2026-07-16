from pathlib import Path
import sys

from ai_providers.provider_registry import ProviderRegistry

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))


class DummyProvider:
    pass


class ProviderOne:
    pass


class ProviderTwo:
    pass


# Register providers
ProviderRegistry.register("dummy", DummyProvider())
ProviderRegistry.register("provider1", ProviderOne())
ProviderRegistry.register("provider2", ProviderTwo())


# Validate single provider retrieval
provider = ProviderRegistry.get("dummy")
print("Retrieved Provider:", type(provider).__name__)


# Validate multiple registrations
print("All Registered Providers:")
for name, provider in ProviderRegistry.get_all().items():
    print(f"{name}: {type(provider).__name__}")
