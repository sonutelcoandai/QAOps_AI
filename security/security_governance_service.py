from security.access_control_service import AccessControlService


class SecurityGovernanceService:
    @staticmethod
    def evaluate(role, permission):

        return {
            "role": role,
            "permission": permission,
            "authorized": AccessControlService.authorize(role, permission),
        }
