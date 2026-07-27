from integrations.integration_health_report import IntegrationHealthReport

from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_status_manager import IntegrationStatusManager


class IntegrationHealthService:
    @staticmethod
    def check(integration_name):

        integration = IntegrationCatalog.get(integration_name)

        if integration is None:
            health = "unknown"

        else:
            status = IntegrationStatusManager.get_status(integration_name)

            if status == "retired":
                health = "unavailable"

            elif status == "deprecated":
                health = "warning"

            else:
                health = "healthy"

        report = IntegrationHealthReport(integration=integration_name, health=health)

        return report.to_dict()
