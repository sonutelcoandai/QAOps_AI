from workflows.registry.workflow_registry import WorkflowRegistry

from workflows.requirement_to_test.requirement_to_test_workflow import (
    RequirementToTestWorkflow,
)


def load_workflows():

    WorkflowRegistry.register("requirement_to_test", RequirementToTestWorkflow())

    print("Workflow Loaded: requirement_to_test")
