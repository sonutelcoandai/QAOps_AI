from config_loader import ConfigLoader

from memory_providers.memory_factory import MemoryFactory


class MemoryManager:
    default_provider = None

    @classmethod
    def initialize(cls):

        config = ConfigLoader.load_config("memory.yaml")

        cls.default_provider = config["memory"]["default_provider"]

    @classmethod
    def get_memory(cls):

        return MemoryFactory.get_memory(cls.default_provider)

    @classmethod
    def save(cls, key, value):

        memory = cls.get_memory()

        memory.save(key, value)

    @classmethod
    def retrieve(cls, key):

        memory = cls.get_memory()

        return memory.retrieve(key)

    @classmethod
    def search(cls, query):

        memory = cls.get_memory()

        return memory.search(query)
