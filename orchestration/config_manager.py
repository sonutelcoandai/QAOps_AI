from config_loader import ConfigLoader


class ConfigManager:
    _platform = None

    @classmethod
    def initialize(cls):

        cls._platform = ConfigLoader.load_config("platform.yaml")

    @classmethod
    def get_platform(cls):

        return cls._platform
