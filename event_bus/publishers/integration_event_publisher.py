from event_bus.publishers.event_publisher import EventPublisher


class IntegrationEventPublisher:
    @staticmethod
    def publish(event):

        EventPublisher.publish(event)
