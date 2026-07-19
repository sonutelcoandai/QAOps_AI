from workflows.registry.workflow_manager import WorkflowManager

WorkflowManager.load()

print(WorkflowManager.get_workflow_config("requirement_to_test"))
