from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

from orchestration.knowledge_bootstrap import KnowledgeBootstrap

result = KnowledgeBootstrap.initialize()

print(result)
