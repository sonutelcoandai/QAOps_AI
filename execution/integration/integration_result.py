class IntegrationResult:
    def __init__(self, status, systems):

        self.status = status
        self.systems = systems

    def to_dict(self):

        return {"status": self.status, "systems": self.systems}
