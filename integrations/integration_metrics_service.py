from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_status_manager import IntegrationStatusManager


class IntegrationMetricsService:
    @staticmethod
    def get_metrics():

        integrations = IntegrationCatalog.get_all()

        metrics = {
            "total_integrations": 0,
            "active": 0,
            "inactive": 0,
            "deprecated": 0,
            "retired": 0,
        }

        metrics["total_integrations"] = len(integrations)

        for integration_name in integrations:
            status = IntegrationStatusManager.get_status(integration_name)

            if status in metrics:
                metrics[status] += 1

        return metrics
