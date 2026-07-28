from marketplace.marketplace_service import MarketplaceService

from marketplace.marketplace_dashboard import MarketplaceDashboard

MarketplaceService.publish("jira_plugin", "integration")

MarketplaceService.publish("github_plugin", "integration")

print(MarketplaceDashboard.generate())
