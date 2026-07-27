from event_bus.publishers.event_publisher import EventPublisher


class ApprovalEventPublisher:
    @staticmethod
    def publish(event):

        EventPublisher.publish(event)
