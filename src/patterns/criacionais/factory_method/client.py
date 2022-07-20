# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:42:28 2022

@author: yagoa
"""
from __future__ import annotations
from abc import abstractmethod
from interface.creator import Creator

def client_code(creator: Creator) -> None:
    """
    O código cliente trabalha com uma instância de um criador concreto, embora por meio da sua interface básica.
    Enquanto o cliente continuar trabalhando com o Creator via interface base, você pode passar a subclasse de qualquer criador.
    """
    print(f"client: I'm not aware of the creator's, but it still works. \n"
            f"{creator.some_operation()}", end="")