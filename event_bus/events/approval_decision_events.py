from event_bus.events.base_event import BaseEvent


class ApprovalApprovedEvent(BaseEvent):
    def __init__(self, request_id):

        super().__init__("approval_approved", {"request_id": request_id})


class ApprovalRejectedEvent(BaseEvent):
    def __init__(self, request_id):

        super().__init__("approval_rejected", {"request_id": request_id})
