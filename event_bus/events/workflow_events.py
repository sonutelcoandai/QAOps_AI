from event_bus.events.base_event import BaseEvent


class WorkflowStartedEvent(BaseEvent):
    def __init__(self, workflow_name):

        super().__init__("workflow_started", {"workflow": workflow_name})


class WorkflowCompletedEvent(BaseEvent):
    def __init__(self, workflow_name):

        super().__init__("workflow_completed", {"workflow": workflow_name})


class WorkflowFailedEvent(BaseEvent):
    def __init__(self, workflow_name, error):

        super().__init__(
            "workflow_failed", {"workflow": workflow_name, "error": str(error)}
        )
