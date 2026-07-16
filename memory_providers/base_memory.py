from abc import ABC, abstractmethod


class BaseMemory(ABC):
    @abstractmethod
    def save(self, key, value):
        """
        Save data
        """
        pass

    @abstractmethod
    def retrieve(self, key):
        """
        Retrieve data
        """
        pass

    @abstractmethod
    def search(self, query):
        """
        Search memory
        """
        pass
