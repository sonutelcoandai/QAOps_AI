from abc import ABC, abstractmethod


class BaseWorkflow(ABC):
    @abstractmethod
    def start(self):
        """
        Start workflow
        """
        pass

    @abstractmethod
    def execute(self):
        """
        Execute workflow
        """
        pass

    @abstractmethod
    def finish(self):
        """
        Finish workflow
        """
        pass
