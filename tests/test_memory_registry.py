from pathlib import Path
import sys
from memory_providers.load_memory_providers import load_memory_providers

from memory_providers.memory_registry import MemoryRegistry

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

print(MemoryRegistry.get_all())
