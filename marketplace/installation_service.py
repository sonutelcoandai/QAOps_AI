from plugins.plugin_service import PluginService


class InstallationService:
    @staticmethod
    def install(plugin_name, version="1.0.0"):

        PluginService.register(plugin_name, version)

        return {"plugin": plugin_name, "status": "installed"}
