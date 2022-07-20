from interface.product import Product



class ConcreteProduct1(Product):
    """
    Os Concrete Product fornecem várias implementações da interface Product.
    """
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"