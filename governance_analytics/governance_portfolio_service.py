from governance_analytics.governance_reporting_service import GovernanceReportingService


class GovernancePortfolioService:
    @staticmethod
    def generate():

        workflows = ["telecom_validation", "billing_validation", "requirement_to_test"]

        return {
            workflow: GovernanceReportingService.generate(workflow)
            for workflow in workflows
        }
