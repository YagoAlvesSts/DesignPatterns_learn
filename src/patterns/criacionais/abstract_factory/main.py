# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from concrete.factory import ConcreteFactory1, ConcreteFactory2
from client import client_code


if __name__ == "__main__":
    """
    Código cliente pode funcionar com qualquer classe de factory concrete.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteFactory2())