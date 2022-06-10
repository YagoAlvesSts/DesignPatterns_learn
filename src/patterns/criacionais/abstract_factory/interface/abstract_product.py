
from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    """
    Cada produto distinto de uma família de produtos deve ter uma interface básica.
    Todas as variantes do produto devem implementar esta interface.
    """
    
    
    @abstractmethod
    def useful_function_a(self) -> str:
        pass



class AbstractProductB(ABC):
    """
    Aqui é outra interface base de outro produto. Todos os produtos podem interagir uns com os outros,
    mas a interação adequada só é possível entre produtos da mesma variante concreta.
    """
    
    
    @abstractmethod
    def useful_function_b(self) -> None:
        """Product B é capaz de fazer suas próprias coisas..."""
        pass

    @abstractmethod
    def annother_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """...Mas também pode colaborar com o ProductA. A Abstract Factory garante que todos os produtos que cria 
        sejam da mesma variante e, portanto, compatíveis."""
        pass
     