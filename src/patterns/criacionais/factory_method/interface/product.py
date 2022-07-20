from abc import ABC, abstractmethod


class Product(ABC):
    """
    A interface Product declara as operações que todos os produtos concretos devem implementar.
    """
    
    @abstractmethod
    def operation(self) -> str:
        pass