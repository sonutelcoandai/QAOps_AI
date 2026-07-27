class ObservabilityEventHandler:
    @staticmethod
    def handle(event):

        print(f"[Observability] {event.event_type}")
