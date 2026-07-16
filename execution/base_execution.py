from abc import ABC, abstractmethod


class BaseExecution(ABC):
    @abstractmethod
    def execute_test(self, test_case):
        """
        Execute test
        """
        pass

    @abstractmethod
    def collect_results(self):
        """
        Collect results
        """
        pass
