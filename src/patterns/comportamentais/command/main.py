from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """
    A interface command declara o método para executar o comando.
    """
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    """
    Alguns comandos podem implementar operações simples por conta própria.
    """
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: Veja, eu consigo fazer coisas simples como printar ({self._payload})")

class ComplexCommand(Command):
    """
    No entanto, alguns comandos podem delegar operações mais complexas
     a outros objetos, chamados de "receivers".
    """

    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        """
        Comandos complexos podem aceitar um ou vários objetos receptores
         junto com quaisquer dados de contexto por meio do construtor.
        """

        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        """
        Commands conseguem delegar a qualquer método de um receptor.
        """

        print("ComplexCommand: Complex...", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    """
    As classes Receiver contêm alguma lógica de negócios importante.
     Sabem realizar todo o tipo de operações associadas à realização
     de um pedido. De fato, qualquer classe pode servir como Receiver.
    """

    def do_something(self, a:str) -> None:
        print(f"\nReceiver: Trabalhando em ({a}.)", end="")

    def do_something_else(self, b:str) -> None:
        print(f"\nReceiver: Também trabalhando em ({b}.)", end="")

class Invoker:
    """
    O Invoker está associado a um ou vários commands. Ele envia uma solicitação ao command.
    """

    _on_start = None
    _on_finish = None

    """
    Inicializa comandos.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        """
        O Invoker não depende de comandos concretos ou classes receptoras.
         O Invoker passa uma solicitação para um receptor indiretamente, executando um comando.
        """
        print("Invoker: ")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...Fazendo algo realmente importante...")

        print("Invoker: ")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    """
    O código do cliente consegue parametrizar o invoker com qualquer comando.
    """

    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Enviar email", "Salvar report"))

    invoker.do_something_important()