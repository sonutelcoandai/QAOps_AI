from marketplace.marketplace_service import MarketplaceService

MarketplaceService.publish("jira_plugin", "integration")

MarketplaceService.publish("github_plugin", "integration")

MarketplaceService.publish("postman_plugin", "testing")

print()

print(MarketplaceService.get_item("jira_plugin"))

print()

print(MarketplaceService.list_items())
