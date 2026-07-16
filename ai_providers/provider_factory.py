from ai_providers.provider_registry import ProviderRegistry


class ProviderFactory:
    @staticmethod
    def get_provider(provider_name):

        provider = ProviderRegistry.get(provider_name)

        if provider is None:
            raise ValueError(f"Provider '{provider_name}' not found")

        return provider
