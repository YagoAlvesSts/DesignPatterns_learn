from typing import Any
from .abstract_handler import AbstractHandler

"""
Todos os manipuladores de concreto traram de uma solicitação ou
passam para o próximo manipulador na corrente.
"""

class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Macaco: vou comer a {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Esquilo: vou comer a {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Cachorro: vou comer a {request}"
        else:
            return super().handle(request)

