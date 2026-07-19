from workflows.registry.load_workflows import load_workflows

from workflows.registry.workflow_manager import WorkflowManager


class WorkflowBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing Workflow Layer...\n")

        WorkflowManager.load()

        load_workflows()

        print("Workflows Loaded")

        print("\nWorkflow Layer Ready\n")
