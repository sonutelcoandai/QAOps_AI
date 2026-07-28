from marketplace.marketplace_item import MarketplaceItem

from marketplace.marketplace_catalog import MarketplaceCatalog


class MarketplaceService:
    @staticmethod
    def publish(name, category, version="1.0.0"):

        item = MarketplaceItem(name=name, category=category, version=version)

        MarketplaceCatalog.add(name, item)

        return item.to_dict()

    @staticmethod
    def get_item(name):

        item = MarketplaceCatalog.get(name)

        if item is None:
            return None

        return item.to_dict()

    @staticmethod
    def list_items():

        return {
            name: item.to_dict() for name, item in MarketplaceCatalog.get_all().items()
        }
