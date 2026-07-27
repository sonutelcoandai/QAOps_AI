from governance_analytics.event_analytics_service import EventAnalyticsService

from integrations.integration_metrics_service import IntegrationMetricsService

from human_in_loop.approval_metrics_service import ApprovalMetricsService


class ExecutiveAnalyticsService:
    @staticmethod
    def generate():

        return {
            "events": EventAnalyticsService.get_metrics(),
            "integrations": IntegrationMetricsService.get_metrics(),
            "approvals": ApprovalMetricsService.get_summary(),
        }
