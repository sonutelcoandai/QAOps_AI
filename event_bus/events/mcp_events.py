from event_bus.events.base_event import BaseEvent


class MCPActionEvent(BaseEvent):
    def __init__(self, action, payload):

        super().__init__(action, payload)
