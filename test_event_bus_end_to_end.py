from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

from event_bus.handlers.metrics_event_handler import MetricsEventHandler

PlatformBootstrap.initialize()

WorkflowExecutionService.execute("telecom_validation", "Validate TMF641")

print()

print(MetricsEventHandler.get_metrics())
