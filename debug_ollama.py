from ai_providers.ollama.ollama_provider import OllamaProvider

provider = OllamaProvider()

response = provider.generate("Explain TMF641 in 3 lines")

print(response)
