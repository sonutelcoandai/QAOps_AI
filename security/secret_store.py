class SecretStore:
    secrets = {}

    @classmethod
    def save(cls, key, value):

        cls.secrets[key] = value

    @classmethod
    def get(cls, key):

        return cls.secrets.get(key)
