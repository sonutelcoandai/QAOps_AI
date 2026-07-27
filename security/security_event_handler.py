class SecurityEventHandler:
    events = []

    @classmethod
    def handle(cls, event):

        cls.events.append({"event_type": event.event_type, "payload": event.payload})

    @classmethod
    def get_events(cls):

        return cls.events
