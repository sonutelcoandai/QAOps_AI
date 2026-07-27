from security.security_service import SecurityService

from security.security_audit_service import SecurityAuditService

from security.vulnerability_dashboard import VulnerabilityDashboard

from security.security_metrics_service import SecurityMetricsService

from security.security_monitoring_service import SecurityMonitoringService


class SecurityHardeningDashboard:
    @staticmethod
    def generate():

        return {
            "policies": {
                "workflow_execution": SecurityService.evaluate("workflow_execution"),
                "production_deployment": SecurityService.evaluate(
                    "production_deployment"
                ),
            },
            "audits": {"workflow": SecurityAuditService.audit("workflow_execution")},
            "vulnerabilities": VulnerabilityDashboard.generate(),
            "monitoring": SecurityMonitoringService.get_summary(),
            "metrics": SecurityMetricsService.generate(),
        }
