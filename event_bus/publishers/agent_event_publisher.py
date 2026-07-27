from event_bus.publishers.event_publisher import EventPublisher


class AgentEventPublisher:
    @staticmethod
    def publish(event):

        EventPublisher.publish(event)
