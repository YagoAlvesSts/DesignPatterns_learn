from __future__ import annotations
from abc import ABC, abstractmethod
from interface.implementation import Implementation
from abstraction.abstraction import Abstraction
from abstraction.entended import ExtendedAbstraction
from implementation.concrete_implementation1 import ConcreteImplementationA
from implementation.concrete_implementation2 import ConcreteImplementationB
from client_code import client_code

"""Cada implementação Concreta corresponde a uma plataforma específica a uma plataforma específica e
implementa a interface de implementação usando a API dessa plataforma."""

if __name__ == "__main__":
    """
    
    """
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)

