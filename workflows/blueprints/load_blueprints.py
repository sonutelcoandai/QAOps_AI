from workflows.blueprints.blueprint_registry import BlueprintRegistry

from workflows.blueprints.workflow_blueprint import WorkflowBlueprint


def load_blueprints():

    BlueprintRegistry.register(
        "requirement_to_test",
        WorkflowBlueprint(
            name="requirement_to_test",
            description="Requirement to Test Workflow",
            agents=["qa_engineer", "senior_qa_engineer", "test_architect"],
        ),
    )

    print("Blueprint Loaded: requirement_to_test")
