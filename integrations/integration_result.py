class IntegrationResult:
    def __init__(self, integration, status):

        self.integration = integration
        self.status = status

    def to_dict(self):

        return {"integration": self.integration, "status": self.status}
