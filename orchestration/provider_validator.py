from ai_providers.provider_registry import ProviderRegistry


class ProviderValidator:
    @staticmethod
    def is_available(provider_name):

        provider = ProviderRegistry.get(provider_name)

        return provider is not None
