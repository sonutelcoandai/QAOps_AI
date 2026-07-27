from event_bus.register_event_handlers import register_handlers


class EventBusBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing Event Bus...\n")

        register_handlers()

        print("Event Handlers Registered")

        print("\nEvent Bus Ready\n")
