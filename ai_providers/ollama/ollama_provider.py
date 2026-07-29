import requests

from ai_providers.base_provider import BaseProvider


class OllamaProvider(BaseProvider):
    def generate(self, prompt: str):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "qwen3:latest",
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        result = response.json()

        return result.get("response", "")

    def chat(self, messages: list):

        prompt = "\n".join(message.get("content", "") for message in messages)

        return self.generate(prompt)

    def embeddings(self, text: str):

        return []
