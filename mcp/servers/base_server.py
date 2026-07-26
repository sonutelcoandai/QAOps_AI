from abc import ABC
from abc import abstractmethod


class BaseServer(ABC):
    @abstractmethod
    def execute(self, request):
        pass
