from interface.creator import Creator
from interface.product import Product
from creator.contrete.product import ConcreteProduct1, ConcreteProduct2

"""
Os criadores concretos substituem o método de fábrica para alterar o resultado tipo de produto.
"""

class ConcreteCreator1(Creator):
    """
    A assinatura do método usa o tipo de produto abstrato, mesmo que o produto concreto seja realmente retornado
    do método.
    Dessa forma, o Creator pode ficar independente de classes de produtos concretas.
    """
    def factory_method(self) -> Product:
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()