from marketplace.marketplace_metrics_service import MarketplaceMetricsService

from marketplace.marketplace_governance_service import MarketplaceGovernanceService

from marketplace.marketplace_service import MarketplaceService


class MarketplaceDashboard:
    @staticmethod
    def generate():

        return {
            "catalog": MarketplaceService.list_items(),
            "metrics": MarketplaceMetricsService.generate(),
            "governance": MarketplaceGovernanceService.evaluate(),
        }
