from workflows.registry.workflow_manager import WorkflowManager


class WorkflowMetadataService:
    @staticmethod
    def get_metadata(workflow_name):

        return WorkflowManager.get_workflow_config(workflow_name)
