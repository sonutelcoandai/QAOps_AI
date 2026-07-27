from cost_management.usage_tracker import UsageTracker

from cost_management.cost_dashboard import CostDashboard

UsageTracker.track("workflow_started")

UsageTracker.track("workflow_started")

UsageTracker.track("agent_started")

print(CostDashboard.generate())
