from ai_providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    def generate(self, prompt: str):
        return f"Ollama Generate: {prompt}"

    def chat(self, messages: list):
        return "Ollama Chat Response"

    def embeddings(self, text: str):
        return []
