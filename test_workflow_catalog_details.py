from workflows.registry.workflow_catalog import WorkflowCatalog

from workflows.registry.workflow_manager import WorkflowManager

WorkflowManager.load()

print(WorkflowCatalog.list_workflow_details())
