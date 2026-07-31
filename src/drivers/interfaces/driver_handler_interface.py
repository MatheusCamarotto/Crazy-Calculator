from abc import ABC, abstractmethod

class DriverHandlerInterface(ABC):

    @abstractmethod
    def standart_derivation(self, numbers:list[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers:list[float]) -> float:
        pass

    @abstractmethod
    def average(self, numbers:list[float]) -> float:
        pass