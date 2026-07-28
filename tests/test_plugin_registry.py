from plugins.plugin_service import PluginService

PluginService.register("jira_plugin")

PluginService.register("github_plugin")

print(PluginService.get_plugins())
