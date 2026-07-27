from security.secret_audit_service import SecretAuditService

from security.security_event_handler import SecurityEventHandler


class SecurityMetricsService:
    @staticmethod
    def generate():

        return {
            "secret_metrics": SecretAuditService.audit(),
            "security_events": len(SecurityEventHandler.get_events()),
        }
