from cost_management.usage_tracker import UsageTracker

from cost_management.cost_service import CostService

UsageTracker.track("ollama")

UsageTracker.track("ollama")

UsageTracker.track("ollama")

print(CostService.calculate("ollama"))
