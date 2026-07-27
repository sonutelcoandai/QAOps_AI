from cost_management.budget_service import BudgetService


class CostGovernanceService:
    @staticmethod
    def evaluate():

        budget = BudgetService.get_budget_status()

        status = "within_budget"

        if budget["remaining"] <= 0:
            status = "budget_exceeded"

        return {"status": status, "budget": budget}
