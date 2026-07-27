from cost_management.usage_tracker import UsageTracker


class CostEventHandler:
    @staticmethod
    def handle(event):

        UsageTracker.track(event.event_type)
