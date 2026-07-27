from governance_analytics.compliance_rule import ComplianceRule

from governance_analytics.compliance_report import ComplianceReport


class ComplianceService:
    @staticmethod
    def evaluate(item):

        result = ComplianceRule.get_rule(item)

        report = ComplianceReport(item=item, result=result)

        return report.to_dict()
