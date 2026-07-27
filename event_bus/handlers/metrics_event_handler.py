class MetricsEventHandler:
    metrics = {
        "workflow_started": 0,
        "workflow_completed": 0,
        "agent_started": 0,
        "agent_completed": 0,
        "create_ticket": 0,
        "create_pr": 0,
        "run_collection": 0,
    }

    @classmethod
    def handle(cls, event):

        if event.event_type in cls.metrics:
            cls.metrics[event.event_type] += 1

    @classmethod
    def get_metrics(cls):

        return cls.metrics
