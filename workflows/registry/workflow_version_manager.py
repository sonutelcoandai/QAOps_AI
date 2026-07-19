from workflows.registry.workflow_manager import WorkflowManager


class WorkflowVersionManager:
    @staticmethod
    def get_version(workflow_name):

        workflow = WorkflowManager.get_workflow_config(workflow_name)

        if not workflow:
            return None

        return workflow.get("version")

    @staticmethod
    def get_status(workflow_name):

        workflow = WorkflowManager.get_workflow_config(workflow_name)

        if not workflow:
            return None

        return workflow.get("status")
