from governance_analytics.governance_dashboard import GovernanceDashboard

from governance_analytics.compliance_summary_service import ComplianceSummaryService

from governance_analytics.executive_analytics_service import ExecutiveAnalyticsService

from governance_analytics.governance_report import GovernanceReport


class GovernanceReportingService:
    @staticmethod
    def generate(workflow_name):

        report = GovernanceReport(
            governance=GovernanceDashboard.generate(workflow_name),
            compliance=ComplianceSummaryService.summarize(),
            analytics=ExecutiveAnalyticsService.generate(),
        )

        return report.to_dict()
