from abc import ABC, abstractmethod


class BaseFramework(ABC):
    @abstractmethod
    def create_agent(self, config: dict):
        """
        Create an agent
        """
        pass

    @abstractmethod
    def execute_agent(self, agent, task):
        """
        Execute an agent
        """
        pass

    @abstractmethod
    def create_workflow(self, workflow):
        """
        Create workflow
        """
        pass
