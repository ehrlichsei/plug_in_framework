from abc import ABC, abstractmethod

class MessagePlugin(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str):
        pass