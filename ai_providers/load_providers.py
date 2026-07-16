from config_loader import ConfigLoader

from ai_providers.provider_registry import ProviderRegistry

from ai_providers.ollama.ollama_provider import OllamaProvider


def load_providers():

    provider_config = ConfigLoader.load_config("providers.yaml")

    providers = provider_config["providers"]

    if providers["ollama"]["enabled"]:
        ProviderRegistry.register("ollama", OllamaProvider())

        print("Provider Loaded: ollama")
