from integrations.integration_status_manager import IntegrationStatusManager

from event_bus.events.integration_events import (
    IntegrationDeprecatedEvent,
    IntegrationRetiredEvent,
)

from event_bus.publishers.integration_event_publisher import IntegrationEventPublisher


class IntegrationLifecycleService:
    @staticmethod
    def activate(integration_name):

        IntegrationStatusManager.set_status(integration_name, "active")

    @staticmethod
    def deactivate(integration_name):

        IntegrationStatusManager.set_status(integration_name, "inactive")

    @staticmethod
    def deprecate(integration_name):

        IntegrationStatusManager.set_status(integration_name, "deprecated")

        IntegrationEventPublisher.publish(IntegrationDeprecatedEvent(integration_name))

    @staticmethod
    def retire(integration_name):

        IntegrationStatusManager.set_status(integration_name, "retired")

        IntegrationEventPublisher.publish(IntegrationRetiredEvent(integration_name))

    @staticmethod
    def get_status(integration_name):

        return IntegrationStatusManager.get_status(integration_name)
