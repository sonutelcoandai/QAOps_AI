class EventAnalyticsService:
    metrics = {
        "workflow_started": 0,
        "workflow_completed": 0,
        "agent_started": 0,
        "agent_completed": 0,
        "create_ticket": 0,
        "create_pr": 0,
        "integration_registered": 0,
        "integration_deprecated": 0,
        "integration_retired": 0,
    }

    @classmethod
    def collect(cls, event):

        if event.event_type in cls.metrics:
            cls.metrics[event.event_type] += 1

    @classmethod
    def get_metrics(cls):

        return cls.metrics
