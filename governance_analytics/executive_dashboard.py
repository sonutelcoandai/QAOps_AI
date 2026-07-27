from governance_analytics.executive_analytics_service import ExecutiveAnalyticsService

from governance_analytics.compliance_summary_service import ComplianceSummaryService


class ExecutiveDashboard:
    @staticmethod
    def generate():

        return {
            "analytics": ExecutiveAnalyticsService.generate(),
            "compliance": ComplianceSummaryService.summarize(),
        }
