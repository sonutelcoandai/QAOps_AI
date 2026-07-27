from cost_management.usage_tracker import UsageTracker

from cost_management.budget_report import BudgetReport


class BudgetService:
    BUDGET_LIMIT = 100.00

    @classmethod
    def get_budget_status(cls):

        total_usage = sum(UsageTracker.get_usage().values())

        current_cost = total_usage * 0.01

        remaining = cls.BUDGET_LIMIT - current_cost

        report = BudgetReport(
            budget=cls.BUDGET_LIMIT,
            current_cost=round(current_cost, 2),
            remaining=round(remaining, 2),
        )

        return report.to_dict()
