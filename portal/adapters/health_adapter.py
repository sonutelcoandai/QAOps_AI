from observability.operations_dashboard import OperationsDashboard

from security.security_hardening_dashboard import SecurityHardeningDashboard


class HealthAdapter:
    @staticmethod
    def get_health():

        return {
            "operations": OperationsDashboard.generate(),
            "security": SecurityHardeningDashboard.generate(),
        }
