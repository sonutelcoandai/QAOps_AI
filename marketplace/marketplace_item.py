class MarketplaceItem:
    def __init__(self, name, category, version):

        self.name = name

        self.category = category

        self.version = version

    def to_dict(self):

        return {"name": self.name, "category": self.category, "version": self.version}
