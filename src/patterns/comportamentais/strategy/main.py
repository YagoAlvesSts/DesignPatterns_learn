from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from src.patterns.comportamentais.strategy import Strategy

class Context():
    """
    O contexto define a interface de interesse dos clientes
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Normalmente, o Context aceita uma estratégia por meio do construtor,
         mas também fornece um setter para alterá-la em tempo de execução.
        """

        self._strategy = strategy


    @property
    def strategy(self) -> Strategy:
        """
        O Context mantém uma referência a um dos objetos Strategy. O Contexto não
         conhece a classe concreta de uma strategy. Deve funcionar com todas
         as strategies através da interface Strategy.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """ Normalmente, o Context permite substituir um objeto Strategy em tempo de execução."""
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        """
        O Context delega algum trabalho ao objeto Strategy em vez
         de implementar várias versões do algoritmo por conta própria.
        """
        #...

        print("Context: Classificando dados usando o strategy (não tenho certeza de como isso será feito)")
        result=self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

        #...


class Strategy(ABC):
    """
    A interface Strategy declara operações comuns a todas as versões suportadas de algum algoritmo.

    O Context usa esta interface para chamar o algoritmo definido por Concrete Strategies.
    """
    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Estratégias Concretas implementam o algoritmo enquanto seguem a Strategy base
interface. A interface os torna intercambiáveis ​​no Contexto.
"""

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List):
        return reversed(sorted(data))


if __name__=="__main__":
    # O código do cliente escolhe uma strategy concreta e a passa para o contexto.
    # O cliente deve estar ciente das diferenças entre as estratégias para
    # para fazer a escolha certa.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy definido para classificação normal.")
    context.do_some_business_logic()
    print()


    print("Client: Strategy definido paa classificação reversa.")
    context.strategy=ConcreteStrategyB()
    context.do_some_business_logic()
