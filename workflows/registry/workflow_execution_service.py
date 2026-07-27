from workflows.registry.workflow_factory import WorkflowFactory

from workflows.registry.workflow_manager import WorkflowManager

from human_in_loop.hitl_policy_service import HITLPolicyService

from human_in_loop.workflow_gate_service import WorkflowGateService

from event_bus.events.workflow_events import (
    WorkflowStartedEvent,
    WorkflowCompletedEvent,
    WorkflowFailedEvent,
)

from event_bus.publishers.workflow_event_publisher import WorkflowEventPublisher


class WorkflowExecutionService:
    @staticmethod
    def execute(workflow_name, input_data):

        config = WorkflowManager.get_workflow_config(workflow_name)

        if config is None:
            raise ValueError(f"Workflow '{workflow_name}' not configured")

        if config.get("status") != "active":
            raise ValueError(f"Workflow '{workflow_name}' is not active")

        if HITLPolicyService.requires_approval(workflow_name):
            approval = WorkflowGateService.require_approval(workflow_name, "system")

            return {
                "workflow": workflow_name,
                "status": "awaiting_approval",
                "approval_request": approval["approval_request"].to_dict(),
            }

        WorkflowEventPublisher.publish(WorkflowStartedEvent(workflow_name))

        try:
            workflow = WorkflowFactory.get_workflow(workflow_name)

            result = workflow.execute(input_data)

            WorkflowEventPublisher.publish(WorkflowCompletedEvent(workflow_name))

            return result

        except Exception as error:
            WorkflowEventPublisher.publish(WorkflowFailedEvent(workflow_name, error))

            raise
