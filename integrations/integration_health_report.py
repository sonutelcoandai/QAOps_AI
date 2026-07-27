class IntegrationHealthReport:
    def __init__(self, integration, health):

        self.integration = integration

        self.health = health

    def to_dict(self):

        return {"integration": self.integration, "health": self.health}
