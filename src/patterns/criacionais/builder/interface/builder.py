from __future__ import annotations
from abc import ABC, abstractmethod

class Builder(ABC):
    """
    A interface Builder especifica métodos para criar as diferentes partes dos objetos Product.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass
