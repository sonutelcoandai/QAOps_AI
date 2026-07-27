from event_bus.publishers.event_publisher import EventPublisher


class WorkflowEventPublisher:
    @staticmethod
    def publish(event):

        EventPublisher.publish(event)
