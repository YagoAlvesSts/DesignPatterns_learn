from interface.abstract_factory import AbstractFactory
from interface.abstract_product import AbstractProductA, AbstractProductB
from .product import ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factory produzem uma família de produtos que pertencem a um único variante.
    O factory garante que os produtos resultantes são compatíveis.
    Observe que as assinaturas dos métodos da Concrete Factory retornam um produto abstrato,
    enquanto dentro do método um produto concreto é instanciado. 
    
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Outra variante de Product gerado através do Concrete Factory.
    """
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


