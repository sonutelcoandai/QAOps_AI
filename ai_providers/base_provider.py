from abc import ABC, abstractmethod


class BaseProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str):
        """
        Generate response for a prompt
        """
        pass

    @abstractmethod
    def chat(self, messages: list):
        """
        Chat-style interaction
        """
        pass

    @abstractmethod
    def embeddings(self, text: str):
        """
        Generate vector embeddings
        """
        pass
