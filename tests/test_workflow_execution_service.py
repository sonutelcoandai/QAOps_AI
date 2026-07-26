from orchestration.platform_bootstrap import PlatformBootstrap

from workflows.registry.load_workflows import load_workflows

from workflows.registry.workflow_execution_service import WorkflowExecutionService

PlatformBootstrap.initialize()

result = WorkflowExecutionService.execute(
    workflow_name="requirement_to_test", input_data="Generate TMF641 API test cases"
)

print(result)
