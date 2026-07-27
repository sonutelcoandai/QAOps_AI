from event_bus.events.base_event import BaseEvent


class ApprovalRequestedEvent(BaseEvent):
    def __init__(self, request_id):

        super().__init__("approval_requested", {"request_id": request_id})


class ApprovalCompletedEvent(BaseEvent):
    def __init__(self, request_id):

        super().__init__("approval_completed", {"request_id": request_id})
