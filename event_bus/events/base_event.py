class BaseEvent:
    def __init__(self, event_type, payload):

        self.event_type = event_type
        self.payload = payload

    def to_dict(self):

        return {"event_type": self.event_type, "payload": self.payload}
