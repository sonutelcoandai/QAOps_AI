from event_bus.publishers.event_publisher import EventPublisher


class MCPEventPublisher:
    @staticmethod
    def publish(event):

        EventPublisher.publish(event)
