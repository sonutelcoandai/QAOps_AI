from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

result = WorkflowExecutionService.execute(
    workflow_name="billing_validation",
    input_data="Validate invoice charging and rating logic",
)

print(result)
