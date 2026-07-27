from observability.observability_dashboard import ObservabilityDashboard

from cost_management.cost_summary_service import CostSummaryService


class OperationsDashboard:
    @staticmethod
    def generate():

        return {
            "observability": ObservabilityDashboard.generate(),
            "cost_management": CostSummaryService.generate(),
        }
