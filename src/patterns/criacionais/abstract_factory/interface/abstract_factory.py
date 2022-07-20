from __future__ import annotations
from abc import ABC, abstractmethod
from .abstract_product import AbstractProductA, AbstractProductB

class AbstractFactory(ABC):
    """
    A interface declara um conjunto de métodos que retornam diferentes produtos abstratos.
    Esses produtos são chamados de família e são relacionados por um tema ou conceito de alto nível.
    Os produtos de uma família geralmente são capazes de colaborar entre si.
    Uma família de produtos pode ter vários variantes, mas os produtos de uma variante são incompatíveis com produtos de outro.
    """
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

