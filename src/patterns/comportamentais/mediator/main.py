from __future__ import annotations
from abc import ABC

class Mediator(ABC):
    """
    A interface Mediator declara um método usado pelos componentes para notificar
     o mediador sobre vários eventos. O Mediador pode reagir a esses eventos e 
     passar a execução para outros componentes.
    """

    def notify(self, sender: object, event: str) -> None:
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self


    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("O mediador reage em A e aciona as seguintes operações:")
            self._component2.do_c()

        elif event == "D":
            print("O mediador reage em D e aciona as seguintes operações:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    O Componente Base fornece a funcionalidade básica de armazenar a instância
     de um mediador dentro de objetos componentes.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Os componentes concretos implementam várias funcionalidades. Eles não dependem de outros
componentes. Eles também não dependem de nenhuma classe mediadora concreta.
"""


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("component 1 fazendo A.")
        self.mediator.notify(self, "A")
        
    def do_b(self) -> None:
        print("Component 1 fazendo B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self) -> None:
        print("component 2 fazendo C")
        self.mediator.notify(self, "C")
        
    def do_d(self) -> None:
        print("Component 2 fazendo D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    #O código do cliente.
    c1 = Component1
    c2 = Component2
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
