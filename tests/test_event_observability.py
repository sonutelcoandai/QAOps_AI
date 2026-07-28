from event_bus.register_event_handlers import register_handlers

register_handlers()

from event_bus.events.base_event import BaseEvent

from event_bus.publishers.event_publisher import EventPublisher

from observability.telemetry_service import TelemetryService

EventPublisher.publish(
    BaseEvent("workflow_started", {"workflow": "telecom_validation"})
)

EventPublisher.publish(
    BaseEvent("workflow_started", {"workflow": "billing_validation"})
)

print(TelemetryService.get_metrics())
