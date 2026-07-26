from workflows.registry.load_workflows import load_workflows

from workflows.registry.workflow_factory import WorkflowFactory

load_workflows()

workflow = WorkflowFactory.get_workflow("requirement_to_test")

print(workflow)
