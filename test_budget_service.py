from cost_management.usage_tracker import UsageTracker

from cost_management.budget_service import BudgetService

for _ in range(10):
    UsageTracker.track("workflow_started")

print(BudgetService.get_budget_status())
