from __future__ import annotations
from abc import ABC, abstractmethod

class Component(ABC):
    """
    A classe base Component declara operações comuns para objetos simples e 
    complexos de uma composição.
    """

    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
        Opcionalmente, o componente base pode declarar uma interface para definir e acessar
        um pai do componente em uma estrutura em árvore.
        Ele também pode fornecer alguma implementação padrão para esses métodos.
        """

        self._parent = parent

    """
    Em alguns casos, seria benéfico definir o direito de operações de gerenciamento filho
    na classe Component base.
    Dessa forma, você não precisará expor nenhuma classe de componente concreta ao
    código do cliente, mesmo durante a montagem da árvore de objetos.
    A desvantagem é que esses métodos estarão vazios para os componentes de nível de folha.    
    """

    def add(self, component: Component) -> None:
        pass

    def remove(self, component: Component) -> None:
        pass

    def is_composite(self) -> bool:
        """Você pode fornecer um método que permite que o código do cliente descubra se
        um componente pode ter filhos. """
        return False

    @abstractmethod
    def operation(self) -> str:
        """
        O comportamento base pode implementar algum comportamento padrão ou deixá-lo
        para classes concretas (declarando o método que contém o comportamento como "abstrato").
        """
        pass

