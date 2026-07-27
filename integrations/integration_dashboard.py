from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_health_service import IntegrationHealthService

from integrations.integration_status_manager import IntegrationStatusManager

from integrations.integration_metrics_service import IntegrationMetricsService


class IntegrationDashboard:
    @staticmethod
    def generate():

        dashboard = {}

        integrations = IntegrationCatalog.get_all()

        for integration_name in integrations:
            dashboard[integration_name] = {
                "status": IntegrationStatusManager.get_status(integration_name),
                "health": IntegrationHealthService.check(integration_name)["health"],
            }

        return {
            "metrics": IntegrationMetricsService.get_metrics(),
            "integrations": dashboard,
        }
