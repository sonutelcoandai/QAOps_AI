from event_bus.subscribers.event_subscriber import EventSubscriber

from integrations.integration_service import IntegrationService

from integrations.integration_lifecycle_service import IntegrationLifecycleService


def listener(event):

    print(event.event_type)

    print(event.payload)


EventSubscriber.subscribe("integration_registered", listener)

EventSubscriber.subscribe("integration_deprecated", listener)

EventSubscriber.subscribe("integration_retired", listener)

IntegrationService.register("jira", "alm")

IntegrationLifecycleService.deprecate("jira")

IntegrationLifecycleService.retire("jira")
