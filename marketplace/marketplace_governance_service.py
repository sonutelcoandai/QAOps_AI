from plugins.plugin_service import PluginService


class MarketplaceGovernanceService:
    @staticmethod
    def evaluate():

        plugins = PluginService.get_plugins()

        return {"registered_plugins": len(plugins), "status": "governed"}
