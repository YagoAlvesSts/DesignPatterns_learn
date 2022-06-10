# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from interface.product import Product
from interface.creator import Creator
from client import client_code
from creator.contrete.creator import ConcreteCreator1, ConcreteCreator2

if __name__ == "__main__":
    print("App: launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("App: launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())

