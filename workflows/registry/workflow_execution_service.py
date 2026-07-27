from workflows.registry.workflow_factory import WorkflowFactory
from workflows.registry.workflow_manager import WorkflowManager

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

        if config.get("status") != "active":
            raise ValueError(f"Workflow '{workflow_name}' is not active")

        WorkflowEventPublisher.publish(WorkflowStartedEvent(workflow_name))

        try:
            workflow = WorkflowFactory.get_workflow(workflow_name)

            result = workflow.execute(input_data)

            WorkflowEventPublisher.publish(WorkflowCompletedEvent(workflow_name))

            return result

        except Exception as error:
            WorkflowEventPublisher.publish(WorkflowFailedEvent(workflow_name, error))
            raise
