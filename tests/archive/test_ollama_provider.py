from pathlib import Path
import sys
from ai_providers.ollama.ollama_provider import OllamaProvider

ROOT_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(ROOT_DIR))


provider = OllamaProvider()

print(provider.generate("Generate telecom test cases"))

print(provider.chat([]))

print(provider.embeddings("Telecom"))

print(isinstance(provider, OllamaProvider))
