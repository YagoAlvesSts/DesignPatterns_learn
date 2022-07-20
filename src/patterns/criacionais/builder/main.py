from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from interface.builder import Builder
from director.director import Director
from concrete_builder.concrete_builder import ConcreteBuilder1

    
if __name__ == "__main__":
    """
    O código do cliente cria um objeto construtor, passa para o diretor e inicia o processo de construção.
    O resultado final é o objeto construtor recuperado.
    """


    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()


    print("\n")


    print("Standart full feature product: ")
    director.build_full_feature_product()
    builder.product.list_parts()


    print("\n")


    print("custom product: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()




    