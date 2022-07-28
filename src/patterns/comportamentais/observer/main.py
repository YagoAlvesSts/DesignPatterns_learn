from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    A interface Subject declara um conjunto de métodos para gerenciar assinantes.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Anexar um observador ao assunto."""
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Separe um observador do assunto."""
        pass

    @abstractmethod
    def notify(self) -> None:
        """Notifique todos os observadores sobre um evento."""
        pass

class ConcreteSubject(Subject):
    """
    O Sujeito possui algum estado importante e notifica os observadores quando o estado muda.
    """

    _state: int = None

    """
    Para simplificar, o estado do Subject, essencial para todos os assinantes, é armazenado nessa variável.
    """

    _observers: List[Observer] = []

    """
    Lista de assinantes. Na vida real, a lista de assinantes pode ser armazenada de
     forma mais abrangente (categorizada por tipo de evento, etc.).
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Anexando um observer. ")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Os métodos de gerenciamento de assinatura.
    """

    def notify(self) -> None:
        """
        Acionar uma atualização em cada assinante.
        """

        print("Subject: Notificando observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Normalmente, a lógica de assinatura é apenas uma fração do que um Subject pode realmente fazer.
            Os Subjects geralmente contêm alguma lógica de negócios importante, que aciona um método de
            notificação sempre que algo importante está prestes a acontecer (ou depois).
        """

        print("\nSubject: Estou fazendo algo importante!")
        self._state = randrange(0, 10)

        print(f"Subject: Meu estado mudou para {self._state}")

class Observer(ABC):
    """
    A interface Observer declara o método de atualização, usado pelos sujeitos.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """Recebe atualização do Subject"""
        pass


"""
Observadores Concretos reagem às atualizações emitidas pelo Subject que foram
anexado a.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverB: Reagindo ao evento")



class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reagindo ao evento")

if __name__ == "__main__":
    #Código do cliente

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()


