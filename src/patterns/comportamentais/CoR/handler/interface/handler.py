from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    """
    A interface Handler declara um método para construir a cadeia de handlers.
     Ele também declara um método para executar uma solicitação.
    """
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass

