from plugins.plugin_service import PluginService

from plugins.plugin_lifecycle_service import PluginLifecycleService

PluginService.register("jira_plugin")

print(PluginLifecycleService.get_status("jira_plugin"))

PluginLifecycleService.deprecate("jira_plugin")

print(PluginLifecycleService.get_status("jira_plugin"))

PluginLifecycleService.retire("jira_plugin")

print(PluginLifecycleService.get_status("jira_plugin"))
