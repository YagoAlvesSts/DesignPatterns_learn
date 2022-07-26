from abc import abstractmethod
from typing import Any
from .interface.handler import Handler

class AbstractHandler(Handler):
    """
    O comportamento de encadeamento padrão pode ser implementado dentro de uma classe de manipulador base.
    """
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Retornar um manipulador daqui nos permitirá vincular manipuladores em um
        # maneira conveniente como esta:
        # monkey.set_next(squirrel).set_next(dog)

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None

        