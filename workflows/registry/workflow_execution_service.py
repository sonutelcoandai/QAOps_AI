from workflows.registry.workflow_factory import WorkflowFactory

from workflows.registry.workflow_manager import WorkflowManager


class WorkflowExecutionService:
    @staticmethod
    def execute(workflow_name, input_data):

        config = WorkflowManager.get_workflow_config(workflow_name)

        if config.get("status") != "active":
            raise ValueError(f"Workflow '{workflow_name}' is not active")

        workflow = WorkflowFactory.get_workflow(workflow_name)

        return workflow.execute(input_data)
