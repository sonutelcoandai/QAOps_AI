from abc import ABC, abstractmethod


class BaseAgent(ABC):
    @abstractmethod
    def execute(self, task: dict):
        """
        Execute a task
        """
        pass

    @abstractmethod
    def validate(self, task: dict):
        """
        Validate task input
        """
        pass

    @abstractmethod
    def get_agent_info(self):
        """
        Return agent metadata
        """
        pass
