from integrations.integration_metadata import IntegrationMetadata


class IntegrationCatalog:
    integrations = {}

    @classmethod
    def register(cls, name, category):

        metadata = IntegrationMetadata(name=name, category=category, status="active")

        cls.integrations[name] = metadata

    @classmethod
    def get(cls, name):

        return cls.integrations.get(name)

    @classmethod
    def get_all(cls):

        return {key: value.to_dict() for key, value in cls.integrations.items()}
