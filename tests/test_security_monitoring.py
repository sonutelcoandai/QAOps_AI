from event_bus.register_event_handlers import register_handlers

register_handlers()

from event_bus.events.base_event import BaseEvent

from event_bus.publishers.event_publisher import EventPublisher

from security.security_dashboard import SecurityDashboard

EventPublisher.publish(
    BaseEvent("workflow_started", {"workflow": "telecom_validation"})
)

print(SecurityDashboard.generate())
