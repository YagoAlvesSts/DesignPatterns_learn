from __future__ import annotations
from abc import ABC, abstractmethod
from interface.builder import Builder


class Director:
    """
    O Director é responsável apenas por executar as etapas de construção em uma determinada sequência.
    É útil ao produzir produtos de acordo com um pedido ou configuração específica.
    A rigor, a classe Director é opcional, pois o cliente pode controlar diretamente os construtores.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        O Director trabalha com qualquer instância do construtor que o código do cliente passa para ele.
        Desta forma, o código do cliente pode alterar o tipo final do produto recém-montado.
        """
        self._builder = builder

    """O Director pode construir diversas variações de produtos usando as mesmas etapas de construção."""
    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_feature_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()