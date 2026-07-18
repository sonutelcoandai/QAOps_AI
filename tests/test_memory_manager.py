from pathlib import Path
import sys
from memory_providers.load_memory_providers import load_memory_providers

from memory.memory_manager import MemoryManager

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(ROOT_DIR))

load_memory_providers()

MemoryManager.initialize()

MemoryManager.save("tmf641", "Service Order Management API")

print(MemoryManager.retrieve("tmf641"))

MemoryManager.save("tmf641", "Service Order Management API")

MemoryManager.save("tmf620", "Product Catalog API")

print(MemoryManager.search("Order"))
