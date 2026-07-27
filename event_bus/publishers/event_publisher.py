from event_bus.subscribers.event_subscriber import EventSubscriber


class EventPublisher:
    @staticmethod
    def publish(event):

        subscribers = EventSubscriber.get_subscribers(event.event_type)

        for callback in subscribers:
            callback(event)
