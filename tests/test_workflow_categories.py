from workflows.registry.workflow_catalog import WorkflowCatalog

from workflows.registry.workflow_manager import WorkflowManager

WorkflowManager.load()

print(WorkflowCatalog.get_workflows_by_category("quality-engineering"))

print(WorkflowCatalog.get_workflows_by_category("telecom"))
