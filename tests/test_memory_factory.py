from pathlib import Path
import sys
from memory_providers.load_memory_providers import load_memory_providers

from memory_providers.memory_factory import MemoryFactory

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

memory = MemoryFactory.get_memory("chroma")

memory.save("topic", "TMF641 Service Order API")

print(memory.retrieve("topic"))
