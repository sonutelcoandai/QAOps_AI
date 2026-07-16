from abc import ABC, abstractmethod


class BasePlugin(ABC):
    @abstractmethod
    def install(self):
        """
        Install plugin
        """
        pass

    @abstractmethod
    def initialize(self):
        """
        Initialize plugin
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Execute plugin
        """
        pass
