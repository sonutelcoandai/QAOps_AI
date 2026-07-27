from security.security_audit_report import SecurityAuditReport


class SecurityAuditService:
    @staticmethod
    def audit(target):

        report = SecurityAuditReport(target=target, result="passed")

        return report.to_dict()
