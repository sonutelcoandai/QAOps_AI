from security.security_service import SecurityService

from security.security_audit_service import SecurityAuditService

from security.security_monitoring_service import SecurityMonitoringService


class SecurityDashboard:
    @staticmethod
    def generate():

        return {
            "policies": {
                "workflow_execution": SecurityService.evaluate("workflow_execution"),
                "production_deployment": SecurityService.evaluate(
                    "production_deployment"
                ),
            },
            "audits": {
                "workflow": SecurityAuditService.audit("workflow_execution"),
                "agent": SecurityAuditService.audit("agent_execution"),
            },
            "monitoring": SecurityMonitoringService.get_summary(),
        }
