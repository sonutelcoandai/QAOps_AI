from human_in_loop.approval_service import ApprovalService

from event_bus.events.approval_events import ApprovalRequestedEvent

from event_bus.publishers.event_publisher import EventPublisher


class WorkflowApprovalService:
    @staticmethod
    def request_approval(workflow_name, requester):

        request_id = f"{workflow_name}_approval"

        request = ApprovalService.create_request(
            request_id, f"{workflow_name} Approval", requester
        )

        EventPublisher.publish(ApprovalRequestedEvent(request_id))

        return request
