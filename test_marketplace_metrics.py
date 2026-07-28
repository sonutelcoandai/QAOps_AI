from marketplace.marketplace_service import MarketplaceService

from marketplace.marketplace_metrics_service import MarketplaceMetricsService

MarketplaceService.publish("jira_plugin", "integration")

MarketplaceService.publish("github_plugin", "integration")

print(MarketplaceMetricsService.generate())
