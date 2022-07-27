from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

class Originator():
    """
    O Originador mantém algum estado importante que pode mudar com o tempo. Ele também define um método para salvar o estado dentro de um memento e outro método para restaurar o estado dele.
    """

    _state = None

    """
    Por uma questão de simplicidade, o estado do originador é armazenado dentro de uma única variável.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Meu estado inicial é: {self._state}")

    def do_something(self) -> None:
        """
        A lógica de negócios do Originador pode afetar seu estado interno. Portanto, o cliente deve fazer backup do estado antes de iniciar os métodos da lógica de negócios por meio do método save().
        """

        print("Originator: Eu estou fazendo algo importante.")
        self._state = self._generate_random_string(30)
        print(f"Originator: e meu estado mudou  para: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """Salva o estado atual dentro do memento"""

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """Reconstroi o estado dos Originators a partir do objeto memento"""

        self._state = memento.get_state()
        print(f"Originator: Meu estato mudou para : {self._state}")

class Memento(ABC):
    """
    A interface Memento fornece uma maneira de recuperar os metadados do memento, como data de criação ou nome. No entanto, não expõe o estado do Originador.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass

class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """O Originator usa esse método quando reconstroi este estado"""
        return self._state

    def get_name(self) -> str:
        """O resto do método é usado pelo Caretaker para mostrar metadados."""

        return f"{self._date} / ({self._state[:9]}...)"

    def get_date(self) -> str:
        return self.get_date

class Caretaker():
    """
    O Zelador não depende da classe Concrete Memento. Portanto, ele não tem acesso ao estado do originador, armazenado dentro do memento. Isto
    funciona com todos os mementos através da interface base do Memento não tem acesso ao estado do originador, armazenado dentro do memento. Ele funciona com todos os mementos através da interface base do Memento.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Salvando Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Reconstruindo estato para: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Aqui a lista dos mementos: ")
        for memento in self._mementos:
            print(memento.get_name())

if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Agora, vamos retornar! \n")
    caretaker.undo()

    print("\nClient: Mais uma vez!\n")
    caretaker.undo()

