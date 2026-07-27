class SecretPolicy:
    ALLOWED_TYPES = ["provider", "integration", "mcp", "api_key"]

    @classmethod
    def validate(cls, secret_type):

        return secret_type in cls.ALLOWED_TYPES
