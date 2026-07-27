from event_bus.subscribers.event_subscriber import EventSubscriber

from human_in_loop.workflow_approval_service import WorkflowApprovalService


def listener(event):

    print(event.event_type)

    print(event.payload)


EventSubscriber.subscribe("approval_requested", listener)

WorkflowApprovalService.request_approval("release_readiness", "qa_manager")
