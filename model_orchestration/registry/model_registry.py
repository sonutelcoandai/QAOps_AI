from config_loader import ConfigLoader


class ModelRegistry:
    models = {}

    @classmethod
    def load(cls):

        config = ConfigLoader.load_config("model-catalog.yaml")

        cls.models = config["models"]

    @classmethod
    def get_model(cls, model_name):

        return cls.models.get(model_name)

    @classmethod
    def get_all_models(cls):

        return cls.models
