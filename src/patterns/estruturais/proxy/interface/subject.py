from abc import ABC, abstractmethod

class Subject(ABC):
    """
    A interface Subject declara operações comuns para RealSubject e Proxy.
     Desde que o cliente trabalhe com o RealSubject usando esta interface, 
     você poderá passar um proxy em vez de um assunto real.
    """

    @abstractmethod
    def request(self) -> None:
        pass
