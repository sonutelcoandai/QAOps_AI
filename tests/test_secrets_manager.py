from security.secrets_manager import SecretsManager

SecretsManager.save_secret("provider", "ollama_api_key", "secret-value")

print(SecretsManager.get_secret("ollama_api_key"))
