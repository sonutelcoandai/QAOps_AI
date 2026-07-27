from integrations.integration_result import IntegrationResult

from integrations.integration_registry import IntegrationRegistry

from integrations.integration_catalog import IntegrationCatalog

from event_bus.events.integration_events import IntegrationRegisteredEvent

from event_bus.publishers.integration_event_publisher import IntegrationEventPublisher


class IntegrationService:
    @staticmethod
    def register(name, category="general"):

        IntegrationRegistry.register(name, name)

        IntegrationCatalog.register(name, category)

        IntegrationEventPublisher.publish(IntegrationRegisteredEvent(name))

    @staticmethod
    def execute(name):

        integration = IntegrationRegistry.get(name)

        if integration is None:
            raise ValueError(f"Integration '{name}' not found")

        result = IntegrationResult(integration=name, status="connected")

        return result.to_dict()
