from workflows.registry.load_workflows import load_workflows

from workflows.registry.workflow_registry import WorkflowRegistry

load_workflows()

print(WorkflowRegistry.get_all())
