from event_bus.subscribers.event_subscriber import EventSubscriber


def listener(event):

    print(f"EVENT -> {event.event_type}")

    print(event.payload)


EventSubscriber.subscribe("agent_started", listener)

EventSubscriber.subscribe("agent_completed", listener)
