from event_bus.events.base_event import BaseEvent

from event_bus.publishers.event_publisher import EventPublisher

from event_bus.subscribers.event_subscriber import EventSubscriber


def workflow_listener(event):

    print(f"Received Event: {event.event_type}")

    print(event.payload)


EventSubscriber.subscribe("workflow_completed", workflow_listener)

event = BaseEvent(
    event_type="workflow_completed",
    payload={"workflow": "telecom_validation", "status": "completed"},
)

EventPublisher.publish(event)
