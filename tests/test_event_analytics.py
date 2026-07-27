from event_bus.register_event_handlers import register_handlers

register_handlers()

from event_bus.events.base_event import BaseEvent

from event_bus.publishers.event_publisher import EventPublisher

from governance_analytics.event_analytics_service import EventAnalyticsService

event = BaseEvent("workflow_started", {"workflow": "telecom_validation"})

EventPublisher.publish(event)

print(EventAnalyticsService.get_metrics())
