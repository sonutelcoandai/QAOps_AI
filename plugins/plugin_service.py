from plugins.plugin_registry import PluginRegistry

from plugins.plugin_metadata import PluginMetadata

from plugins.plugin_status_manager import PluginStatusManager


class PluginService:
    @staticmethod
    def register(name, version="1.0.0"):

        metadata = PluginMetadata(name=name, version=version, status="active")

        PluginRegistry.register(name, metadata)

        PluginStatusManager.set_status(name, "active")

    @staticmethod
    def get_plugins():

        return {
            name: {**plugin.to_dict(), "status": PluginStatusManager.get_status(name)}
            for name, plugin in PluginRegistry.get_all().items()
        }
