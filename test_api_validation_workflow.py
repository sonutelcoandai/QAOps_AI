from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

result = WorkflowExecutionService.execute(
    workflow_name="api_validation", input_data="Validate TMF641 Service Order API"
)

print(result)
