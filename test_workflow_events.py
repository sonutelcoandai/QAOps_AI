from event_bus.subscribers.event_subscriber import EventSubscriber


def event_listener(event):

    print(f"EVENT -> {event.event_type}")

    print(event.payload)


EventSubscriber.subscribe("workflow_started", event_listener)

EventSubscriber.subscribe("workflow_completed", event_listener)
