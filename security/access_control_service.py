from security.role_manager import RoleManager

from security.permission_policy import PermissionPolicy


class AccessControlService:
    @staticmethod
    def authorize(role, permission):

        if not RoleManager.is_valid_role(role):
            return False

        return permission in PermissionPolicy.get_permissions(role)
