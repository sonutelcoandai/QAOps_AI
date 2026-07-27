class IntegrationPortfolio:
    def __init__(self, integrations, metrics):

        self.integrations = integrations

        self.metrics = metrics

    def to_dict(self):

        return {"integrations": self.integrations, "metrics": self.metrics}
