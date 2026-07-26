from abc import ABC
from abc import abstractmethod


class BaseClient(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self, request):
        pass
