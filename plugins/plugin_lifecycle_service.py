from plugins.plugin_status_manager import PluginStatusManager


class PluginLifecycleService:
    @staticmethod
    def activate(plugin_name):

        PluginStatusManager.set_status(plugin_name, "active")

    @staticmethod
    def deactivate(plugin_name):

        PluginStatusManager.set_status(plugin_name, "inactive")

    @staticmethod
    def deprecate(plugin_name):

        PluginStatusManager.set_status(plugin_name, "deprecated")

    @staticmethod
    def retire(plugin_name):

        PluginStatusManager.set_status(plugin_name, "retired")

    @staticmethod
    def get_status(plugin_name):

        return PluginStatusManager.get_status(plugin_name)
