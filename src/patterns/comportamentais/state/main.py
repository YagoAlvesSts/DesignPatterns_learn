from __future__ import annotations
from abc import ABC, abstractmethod

class Context:
    """
    O Contexto define a interface de interesse dos clientes. Ele também mantém uma referência a uma instância de uma subclasse State, que representa o estado atual do Context.
    """

    _state = None

    """
    Uma referência ao estado atual do Contexto.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        O Context permite alterar o objeto State em tempo de execução.
        """
        print(f"Context: Transição para {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    O Context delega parte de seu comportamento ao objeto State atual.
    """

    def request1(self):
        self._state.handle1()
    
    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    A classe base State declara métodos que todo Concrete State deve implementar e também fornece uma referência inversa ao objeto Context, associado ao State. Essa referência anterior pode ser usada pelos Estados para fazer a transição do Contexto para outro Estado.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

"""
Os Estados Concretos implementam diversos comportamentos, associados a um estado de
Contexto.
"""

class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA deseja alterar o estado do contexto.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("concreteStateA handles request2.")

class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB deseja alterar o estado do contexto.")
        self.context.transition_to(ConcreteStateA)

if __name__ == "__main__":
    #O código do cliente

    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
