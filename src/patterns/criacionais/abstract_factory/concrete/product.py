from interface.abstract_product import AbstractProductA, AbstractProductB

"""
Concrete Product são criados pelos Factory Concrete correspondentes.
"""

class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "the result of the product A1"

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "the result of the product A2"



class ConcreteProductB1(AbstractProductB):
    """
    A variante, ProductB1 só funciona corretamente com a variante ProductA1.
    No entanto, ele aceita qualquer instância de AbstractProductA como argumento.
    """
    
    def useful_function_b(self) -> str:
        return "The result of the product B1"

    def annother_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return "The result of the B1 collaborating with the ({result})"


class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "The result of the product B2"

    def annother_useful_function_b(self, collaborator: AbstractProductA):
        """
        A variante, ProductB2, só funciona corretamente com a variante ProductA2.
        No entanto, ele aceita qualquer instância de AbstractProductA como argumento.
        """
        result = collaborator.useful_function_a()
        return "The result of the B2 collaborating with the ({result})"
