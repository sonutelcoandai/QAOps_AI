from human_in_loop.approval_service import ApprovalService

from event_bus.events.approval_decision_events import (
    ApprovalApprovedEvent,
    ApprovalRejectedEvent,
)

from event_bus.publishers.approval_event_publisher import ApprovalEventPublisher


class ApprovalDecisionService:
    @staticmethod
    def approve(request_id):

        request = ApprovalService.approve(request_id)

        if request is None:
            raise ValueError(f"Approval request '{request_id}' not found")

        ApprovalEventPublisher.publish(ApprovalApprovedEvent(request_id))

        return request

    @staticmethod
    def reject(request_id):

        request = ApprovalService.reject(request_id)

        if request is None:
            raise ValueError(f"Approval request '{request_id}' not found")

        ApprovalEventPublisher.publish(ApprovalRejectedEvent(request_id))

        return request
