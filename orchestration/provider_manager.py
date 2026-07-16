from config_loader import ConfigLoader


class ProviderManager:
    provider_config = {}

    @classmethod
    def load(cls):

        config = ConfigLoader.load_config("providers.yaml")

        cls.provider_config = config["providers"]

    @classmethod
    def get_default_provider_name(cls):

        return cls.provider_config["default_provider"]

    @classmethod
    def get_provider_config(cls, provider_name):

        return cls.provider_config.get(provider_name, {})
