from event_bus.register_event_handlers import register_handlers

register_handlers()

from event_bus.events.base_event import BaseEvent

from event_bus.publishers.event_publisher import EventPublisher

from cost_management.usage_tracker import UsageTracker

EventPublisher.publish(BaseEvent("workflow_started", {}))

EventPublisher.publish(BaseEvent("workflow_started", {}))

print(UsageTracker.get_usage())
