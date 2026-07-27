from governance_analytics.governance_metrics_service import GovernanceMetricsService

from governance_analytics.governance_service import GovernanceService


class GovernanceDashboard:
    @staticmethod
    def generate(workflow_name):

        return {
            "governance": GovernanceService.evaluate(workflow_name),
            "metrics": GovernanceMetricsService.get_metrics(),
        }
