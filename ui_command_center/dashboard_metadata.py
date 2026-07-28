class DashboardMetadata:
    def __init__(self, name, category):

        self.name = name
        self.category = category

    def to_dict(self):

        return {"name": self.name, "category": self.category}
