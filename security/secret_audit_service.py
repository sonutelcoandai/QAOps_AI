from security.secret_store import SecretStore


class SecretAuditService:
    @staticmethod
    def audit():

        return {"secret_count": len(SecretStore.secrets)}
