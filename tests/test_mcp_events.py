from event_bus.subscribers.event_subscriber import EventSubscriber


def listener(event):

    print(f"EVENT -> {event.event_type}")

    print(event.payload)


EventSubscriber.subscribe("create_ticket", listener)

EventSubscriber.subscribe("create_pr", listener)

EventSubscriber.subscribe("run_collection", listener)
