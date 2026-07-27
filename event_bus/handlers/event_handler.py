class EventHandler:
    @staticmethod
    def handle(event):

        print(f"Handling Event: {event.event_type}")

        print(event.payload)
