from memory_providers.memory_registry import MemoryRegistry


class MemoryFactory:
    @staticmethod
    def get_memory(memory_name):

        memory = MemoryRegistry.get(memory_name)

        if memory is None:
            raise ValueError(f"Memory Provider '{memory_name}' not found")

        return memory
