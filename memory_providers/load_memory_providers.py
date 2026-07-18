from memory_providers.memory_registry import MemoryRegistry

from memory_providers.chroma.chroma_memory import ChromaMemory


def load_memory_providers():

    MemoryRegistry.register("chroma", ChromaMemory())

    print("Memory Loaded: chroma")
