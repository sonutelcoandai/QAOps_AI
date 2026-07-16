class ProviderRegistry:
    providers = {}

    @classmethod
    def register(cls, provider_name, provider_instance):

        cls.providers[provider_name] = provider_instance

    @classmethod
    def get(cls, provider_name):

        return cls.providers.get(provider_name)

    @classmethod
    def get_all(cls):

        return cls.providers
