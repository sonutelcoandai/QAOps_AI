class EventSubscriber:
    subscribers = {}

    @classmethod
    def subscribe(cls, event_type, callback):

        cls.subscribers.setdefault(event_type, []).append(callback)

    @classmethod
    def get_subscribers(cls, event_type):

        return cls.subscribers.get(event_type, [])
