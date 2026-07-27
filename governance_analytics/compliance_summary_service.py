from governance_analytics.compliance_service import ComplianceService


class ComplianceSummaryService:
    @staticmethod
    def summarize():

        items = ["telecom_validation", "billing_validation", "release_readiness"]

        return [ComplianceService.evaluate(item) for item in items]
