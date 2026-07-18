from pathlib import Path
import sys
from knowledge.document_loader import DocumentLoader

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))


content = DocumentLoader.load("knowledge/tmforum/tmf641.md")

print(content)
