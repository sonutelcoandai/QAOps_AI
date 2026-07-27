class IntegrationMetadata:
    def __init__(self, name, category, status):

        self.name = name

        self.category = category

        self.status = status

    def to_dict(self):

        return {"name": self.name, "category": self.category, "status": self.status}
