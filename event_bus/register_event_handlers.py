from event_bus.subscribers.event_subscriber import EventSubscriber

from event_bus.handlers.analytics_event_handler import AnalyticsEventHandler

from event_bus.handlers.observability_event_handler import ObservabilityEventHandler

from event_bus.handlers.governance_event_handler import GovernanceEventHandler
from event_bus.handlers.metrics_event_handler import MetricsEventHandler
from governance_analytics.event_analytics_handler import EventAnalyticsHandler

EVENTS = [
    "workflow_started",
    "workflow_completed",
    "agent_started",
    "agent_completed",
    "create_ticket",
    "create_pr",
    "run_collection",
]


def register_handlers():

    for event_name in EVENTS:
        EventSubscriber.subscribe(event_name, AnalyticsEventHandler.handle)

        EventSubscriber.subscribe(event_name, ObservabilityEventHandler.handle)

        EventSubscriber.subscribe(event_name, GovernanceEventHandler.handle)
        EventSubscriber.subscribe(event_name, MetricsEventHandler.handle)
        EventSubscriber.subscribe(event_name, EventAnalyticsHandler.handle)
