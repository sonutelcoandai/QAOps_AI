from marketplace.marketplace_catalog import MarketplaceCatalog


class MarketplaceMetricsService:
    @staticmethod
    def generate():

        return {"published_plugins": len(MarketplaceCatalog.get_all())}
