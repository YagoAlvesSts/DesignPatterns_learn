from __future__ import annotations
from abc import ABC, abstractmethod

class Implementation(ABC):
    """
    A implementação define a interface para todas as classes de implementação.
    Ele não precisa corresponder à interface da abstração.
    Na verdade, as duas interfaces podem ser totalmente diferentes.
    Normalmente, a interface da Implementação fornece apenas operações primitivas, enquanto a Abstração
    define operações de nível superior com base nessas primitivas.
    """
    @abstractmethod
    def operation_implementation(self) -> str:
        pass