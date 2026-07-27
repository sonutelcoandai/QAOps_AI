class UsageTracker:
    usage = {}

    @classmethod
    def track(cls, service):

        cls.usage[service] = cls.usage.get(service, 0) + 1

    @classmethod
    def get_usage(cls):

        return cls.usage
