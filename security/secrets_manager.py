from security.secret_store import SecretStore

from security.secret_policy import SecretPolicy


class SecretsManager:
    @staticmethod
    def save_secret(secret_type, key, value):

        if not SecretPolicy.validate(secret_type):
            raise ValueError(f"Secret type '{secret_type}' not allowed.")

        SecretStore.save(key, value)

    @staticmethod
    def get_secret(key):

        return SecretStore.get(key)
