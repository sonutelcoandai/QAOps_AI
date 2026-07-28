from plugins.plugin_lifecycle_service import PluginLifecycleService


class MarketplaceLifecycleService:
    @staticmethod
    def activate(plugin_name):

        PluginLifecycleService.activate(plugin_name)

    @staticmethod
    def deactivate(plugin_name):

        PluginLifecycleService.deactivate(plugin_name)

    @staticmethod
    def deprecate(plugin_name):

        PluginLifecycleService.deprecate(plugin_name)

    @staticmethod
    def retire(plugin_name):

        PluginLifecycleService.retire(plugin_name)
