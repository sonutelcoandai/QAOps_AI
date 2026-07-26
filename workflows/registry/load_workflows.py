from workflows.registry.workflow_registry import WorkflowRegistry

from workflows.requirement_to_test.requirement_to_test_workflow import (
    RequirementToTestWorkflow,
)

from workflows.telecom_validation.telecom_validation_workflow import (
    TelecomValidationWorkflow,
)
from workflows.billing_validation.billing_validation_workflow import (
    BillingValidationWorkflow,
)
from workflows.oss_validation.oss_validation_workflow import OSSValidationWorkflow
from workflows.api_validation.api_validation_workflow import APIValidationWorkflow


def load_workflows():

    WorkflowRegistry.register("requirement_to_test", RequirementToTestWorkflow())

    WorkflowRegistry.register("telecom_validation", TelecomValidationWorkflow())
    WorkflowRegistry.register("billing_validation", BillingValidationWorkflow())
    WorkflowRegistry.register("oss_validation", OSSValidationWorkflow())

    WorkflowRegistry.register("api_validation", APIValidationWorkflow())

    print("Workflow Loaded: api_validation")
    print("Workflow Loaded: oss_validation")

    print("Workflow Loaded: billing_validation")

    print("Workflow Loaded: telecom_validation")

    print("Workflow Loaded: requirement_to_test")
