from marketplace.marketplace_lifecycle_service import MarketplaceLifecycleService

from plugins.plugin_lifecycle_service import PluginLifecycleService

MarketplaceLifecycleService.deprecate("jira_plugin")

print(PluginLifecycleService.get_status("jira_plugin"))
