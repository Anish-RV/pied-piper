from abc import ABC, abstractmethod

class Algorithm(ABC):
    @abstractmethod
    def compress(self, filepath):
        raise NotImplemented
    
    @abstractmethod
    def decompress(self, filepath):
        raise NotImplemented