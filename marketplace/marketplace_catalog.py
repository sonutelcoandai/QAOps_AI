class MarketplaceCatalog:
    items = {}

    @classmethod
    def add(cls, name, item):

        cls.items[name] = item

    @classmethod
    def get(cls, name):

        return cls.items.get(name)

    @classmethod
    def get_all(cls):

        return cls.items
