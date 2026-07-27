class AnalyticsEventHandler:
    @staticmethod
    def handle(event):

        print(f"[Analytics] {event.event_type}")
