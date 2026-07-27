from event_bus.subscribers.event_subscriber import EventSubscriber

from human_in_loop.workflow_approval_service import WorkflowApprovalService

from human_in_loop.approval_decision_service import ApprovalDecisionService


def listener(event):

    print(event.event_type)

    print(event.payload)


EventSubscriber.subscribe("approval_approved", listener)

request = WorkflowApprovalService.request_approval("release_readiness", "qa_manager")

ApprovalDecisionService.approve(request.request_id)
