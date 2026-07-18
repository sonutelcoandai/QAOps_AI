from config_loader import ConfigLoader

from model_orchestration.registry.model_registry import ModelRegistry

from orchestration.provider_validator import ProviderValidator


class FallbackManager:
    fallback_config = {}

    @classmethod
    def load(cls):

        config = ConfigLoader.load_config("llm-routing.yaml")

        cls.fallback_config = config["fallback"]

    @classmethod
    def get_fallback_model(cls):

        return cls.fallback_config["model"]

    @classmethod
    def resolve_model(cls, model_name):

        model = ModelRegistry.get_model(model_name)

        if not model:
            return cls.get_fallback_model()

        provider = model["provider"]

        if not ProviderValidator.is_available(provider):
            return cls.get_fallback_model()

        return model_name
