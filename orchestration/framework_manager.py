from config_loader import ConfigLoader


class FrameworkManager:
    config = {}

    @classmethod
    def load(cls):

        data = ConfigLoader.load_config("agents.yaml")

        cls.config = data["framework"]

    @classmethod
    def get_default_framework(cls):

        return cls.config["default"]
