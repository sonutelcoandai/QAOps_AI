from workflows.registry.workflow_registry import WorkflowRegistry


class WorkflowFactory:
    @staticmethod
    def get_workflow(workflow_name):

        workflow = WorkflowRegistry.get(workflow_name)

        if workflow is None:
            raise ValueError(f"Workflow '{workflow_name}' not found")

        return workflow
