from abc import ABC, abstractmethod


class Creator(ABC):
    """
    Declara métodos de fábrica que deve retornar um objeto de uma classe Product.
    As subclasses do Creator geralmente fornece a implementação deste método.
    """

    def factory_method(self):
        """
        Observe que o Criator tmb pode fornecer alguma implementação padrão do factory method.
        """
        pass

    def some_operation(self) -> str:
        """
        Apesar do nome, o Creator não cria necessariamente os produtos. 
        Normalmente, ele contém alguma lógica de negócios principal que depende de objetos
        retornados pelo factory method.
        As subclasses podem alterar indiretamente essa lógica de negócios substituindo o 
        factory method e retornando um tipo diferente de produto dele.
        """
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result