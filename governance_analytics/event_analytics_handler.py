from governance_analytics.event_analytics_service import EventAnalyticsService


class EventAnalyticsHandler:
    @staticmethod
    def handle(event):

        EventAnalyticsService.collect(event)
