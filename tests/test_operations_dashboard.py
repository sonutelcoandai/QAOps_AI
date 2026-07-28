from cost_management.usage_tracker import UsageTracker

from observability.alert_service import AlertService

from observability.operations_dashboard import OperationsDashboard

UsageTracker.track("workflow_started")

UsageTracker.track("agent_started")

AlertService.create_alert("workflow_engine", "Workflow latency increased")

print(OperationsDashboard.generate())
