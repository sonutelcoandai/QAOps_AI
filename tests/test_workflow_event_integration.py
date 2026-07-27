import test_workflow_events

from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

WorkflowExecutionService.execute(
    workflow_name="telecom_validation", input_data="Validate TMF641 API"
)
