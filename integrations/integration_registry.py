class IntegrationRegistry:
    integrations = {}

    @classmethod
    def register(cls, name, integration):

        cls.integrations[name] = integration

    @classmethod
    def get(cls, name):

        return cls.integrations.get(name)

    @classmethod
    def get_all(cls):

        return cls.integrations
