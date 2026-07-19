from workflows.registry.workflow_manager import WorkflowManager

from workflows.registry.workflow_version_manager import WorkflowVersionManager

WorkflowManager.load()

print(WorkflowVersionManager.get_version("requirement_to_test"))

print(WorkflowVersionManager.get_status("requirement_to_test"))
