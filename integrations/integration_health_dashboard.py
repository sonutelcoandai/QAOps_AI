from integrations.integration_catalog import IntegrationCatalog

from integrations.integration_health_service import IntegrationHealthService


class IntegrationHealthDashboard:
    @staticmethod
    def get_summary():

        integrations = IntegrationCatalog.get_all()

        summary = {}

        for name in integrations:
            summary[name] = IntegrationHealthService.check(name)

        return summary
