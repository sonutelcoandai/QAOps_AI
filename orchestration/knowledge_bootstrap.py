from knowledge.knowledge_pack_loader import KnowledgePackLoader

from memory.memory_manager import MemoryManager

from memory_providers.load_memory_providers import load_memory_providers


class KnowledgeBootstrap:
    @staticmethod
    def initialize():

        print("\nInitializing Knowledge Layer...\n")

        load_memory_providers()

        MemoryManager.initialize()

        loaded = KnowledgePackLoader.load_all()

        print(f"Knowledge Documents Loaded: {len(loaded)}")

        print("\nKnowledge Layer Ready\n")

        return loaded
