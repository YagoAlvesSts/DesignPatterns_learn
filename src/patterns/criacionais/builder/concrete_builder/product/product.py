from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Product1():
    """
    Faz sentido usar o padrão Builder apenas quando seus produtos são bastante complexos e exigem uma configuração extensa.
    Ao contrário de outros padrões de criação, diferentes construtores de concreto podem produsir produtos não relacionados.
    Em outras palavras, os resultados de vários construtores nem sempre seguem a mesma interface.
    """
    

    def __init__(self) -> None:
        self.parts = []


    def add(self, part: Any) -> None:
        self.parts.append(part)

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '. join(self.parts)}", end="")
