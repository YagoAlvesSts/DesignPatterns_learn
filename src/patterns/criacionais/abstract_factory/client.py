from interface.abstract_factory import AbstractFactory

def client_code(factory: AbstractFactory) -> None:
    """
    O código cliente trabalha com factories apenas por meio de tipos abstratos: AbstractFactory e AbstractProduct.
    Isso permite que você passe qualquer subclasse de factory ou product para o código do cliente sem quebrá-lo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.annother_useful_function_b(product_a)}", end="")

