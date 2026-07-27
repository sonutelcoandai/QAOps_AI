from cost_management.usage_tracker import UsageTracker

from cost_management.budget_service import BudgetService


class CostSummaryService:
    @staticmethod
    def generate():

        return {
            "usage": UsageTracker.get_usage(),
            "budget": BudgetService.get_budget_status(),
        }
