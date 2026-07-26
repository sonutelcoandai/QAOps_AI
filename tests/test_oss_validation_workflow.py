from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

result = WorkflowExecutionService.execute(
    workflow_name="oss_validation",
    input_data="Validate telecom service provisioning flow",
)

print(result)
