from interface.builder import Builder
from .product.product import Product1



class ConcreteBuilder1(Builder):

    """
    Concrete Builder seguem a interface Builder e fornecem implementações específicas das etapas de construção.
    Seu programa pode ter diversas variações de Builders, implementadas de forma diferente.
    """
    def __init__(self) -> None:
        self.reset()
        """
        Uma nova instância do construtor deve conter um objeto de produto em branco, que é usado em outras montagens.
        """


    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Construtores de Concrete devem fornecer seus próprios métodos para recuperar resultados. 
        O motivo é pelos vários tipos de construtores que podem criar produtos totalmente diferentes
        que não seguem a mesma interface.
        Portanto, tais métodos não podem ser declarados na interface base do Builder (pelo menos em uma
        linguagem de programação com tipagem estática).

        Normalmente, após devolver o resultado final ao cliente, espera-se que uma instância do construtor
        esteja pronta para produzir outro produto.
        É por isso que é uma pratica comum chamar o método reset no final do corpo do método 'getProduct'.
        No entanto, esse comportamento não é obrigatório e você pode fazer seus construtores aguardarem uma 
        chamada de redefinição explícita do código do cliente antes de destacar o resultado anterior.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")