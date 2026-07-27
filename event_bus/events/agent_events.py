from event_bus.events.base_event import BaseEvent


class AgentStartedEvent(BaseEvent):
    def __init__(self, agent_name):

        super().__init__("agent_started", {"agent": agent_name})


class AgentCompletedEvent(BaseEvent):
    def __init__(self, agent_name):

        super().__init__("agent_completed", {"agent": agent_name})


class AgentFailedEvent(BaseEvent):
    def __init__(self, agent_name, error):

        super().__init__("agent_failed", {"agent": agent_name, "error": str(error)})
