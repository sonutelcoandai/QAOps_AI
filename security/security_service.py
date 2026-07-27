from security.security_policy import SecurityPolicy

from security.security_report import SecurityReport


class SecurityService:
    @staticmethod
    def evaluate(operation):

        decision = SecurityPolicy.get_policy(operation)

        report = SecurityReport(operation=operation, decision=decision)

        return report.to_dict()
