from event_bus.events.base_event import BaseEvent


class IntegrationRegisteredEvent(BaseEvent):
    def __init__(self, integration_name):

        super().__init__("integration_registered", {"integration": integration_name})


class IntegrationDeprecatedEvent(BaseEvent):
    def __init__(self, integration_name):

        super().__init__("integration_deprecated", {"integration": integration_name})


class IntegrationRetiredEvent(BaseEvent):
    def __init__(self, integration_name):

        super().__init__("integration_retired", {"integration": integration_name})
