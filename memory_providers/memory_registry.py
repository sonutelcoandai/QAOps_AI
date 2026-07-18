class MemoryRegistry:
    memories = {}

    @classmethod
    def register(cls, memory_name, memory_instance):

        cls.memories[memory_name] = memory_instance

    @classmethod
    def get(cls, memory_name):

        return cls.memories.get(memory_name)

    @classmethod
    def get_all(cls):

        return cls.memories
