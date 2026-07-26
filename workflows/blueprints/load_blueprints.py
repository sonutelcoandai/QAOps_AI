from workflows.blueprints.blueprint_registry import BlueprintRegistry
from workflows.blueprints.workflow_blueprint import WorkflowBlueprint


def load_blueprints():
    BlueprintRegistry.register(
        "requirement_to_test",
        WorkflowBlueprint(
            name="requirement_to_test",
            description="Requirement to Test Workflow",
            agents=[
                "qa_engineer",
                "senior_qa_engineer",
                "test_architect",
            ],
        ),
    )

    print("Blueprint Loaded: requirement_to_test")

    BlueprintRegistry.register(
        "telecom_validation",
        WorkflowBlueprint(
            name="telecom_validation",
            description="Telecom Validation Workflow",
            agents=[
                "tmforum_agent",
                "test_architect",
            ],
        ),
    )

    print("Blueprint Loaded: telecom_validation")

    BlueprintRegistry.register(
        "billing_validation",
        WorkflowBlueprint(
            name="billing_validation",
            description="Billing Validation Workflow",
            agents=["billing_agent", "telecom_architect_agent"],
        ),
    )

    print("Blueprint Loaded: billing_validation")

    BlueprintRegistry.register(
        "oss_validation",
        WorkflowBlueprint(
            name="oss_validation",
            description="OSS Validation Workflow",
            agents=["oss_agent", "telecom_architect_agent"],
        ),
    )

    print("Blueprint Loaded: oss_validation")
