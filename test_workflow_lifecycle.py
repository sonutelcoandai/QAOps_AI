from workflows.registry.workflow_catalog import WorkflowCatalog

from workflows.registry.workflow_manager import WorkflowManager

WorkflowManager.load()

print(WorkflowCatalog.get_active_workflows())

print(WorkflowCatalog.get_workflow_info("requirement_to_test"))
