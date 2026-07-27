from event_bus.register_event_handlers import register_handlers

register_handlers()

import test_workflow_events

from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

WorkflowExecutionService.execute("telecom_validation", "Validate TMF641 API")
