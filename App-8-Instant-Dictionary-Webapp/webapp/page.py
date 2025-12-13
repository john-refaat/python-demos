from abc import ABC, abstractmethod

class Page(ABC):

    @classmethod
    @abstractmethod
    def serve(cls, req):
        pass