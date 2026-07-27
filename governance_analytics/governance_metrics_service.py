from governance_analytics.event_analytics_service import EventAnalyticsService


class GovernanceMetricsService:
    @staticmethod
    def get_metrics():

        analytics_metrics = EventAnalyticsService.get_metrics()

        return {
            "analytics_metrics": analytics_metrics,
            "total_events": sum(analytics_metrics.values()),
        }
