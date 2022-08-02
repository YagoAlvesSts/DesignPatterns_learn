from abc import ABC, abstractmethod

class AbstractClass(ABC):
    """
    A classe abstrata define um método de modelo que contém um esqueleto de algum algoritmo,
     composto de chamadas para (geralmente) operações primitivas abstratas.

    As subclasses concretas devem implementar essas operações, mas deixar o próprio método de modelo intacto.
    """

    def template_method(self) -> None:
        """
        O método template define o esqueleto de um algoritmo
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    #Essas operações já possuem implementações.

    def base_operation1(self) -> None:
        print("AbstractClass diz: eu estou fazendo a maior parte do trabalho")

    def base_operation2(self) -> None:
        print("AbstractClass diz: Mas eu deixo subclasses substituir algumas operações")

    def base_operation3(self) -> None:
        print("AbstractClass diz: Mas estou fazendo a maior parte do trabalho de qualquer maneira")

    #Essas operações devem ser implementadas em subclasses.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # Estes são "ganchos". As subclasses podem substituí-las, mas não é obrigatório
    # já que os hooks já possuem implementação padrão (mas vazia). Ganchos
    # fornece pontos de extensão adicionais em alguns lugares cruciais do algoritmo

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    As classes concretas precisam implementar todas as operações abstratas da classe base.
     Eles também podem substituir algumas operações com uma implementação padrão.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 diz: Implementado Operation1")


    def required_operations2(self) -> None:
        print("ConcreteClass1 diz: Implementado Operation2")


class ConcreteClass2(AbstractClass):
    """
    Normalmente, as classes concretas substituem apenas uma fração das operações da classe base.
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 diz: Implementado Operation2")

    def required_operations2(self) -> None:
        print("ConcreteClass2 diz: Implementado Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 diz: sobscrevendo Hook1")
        

def client_code(abstract_class: AbstractClass) -> None:
    """
    O código do cliente chama o método de modelo para executar o algoritmo.
     O código cliente não precisa conhecer a classe concreta de um objeto com 
     o qual trabalha, desde que trabalhe com objetos por meio da interface de sua classe base.
    """

    #...
    abstract_class.template_method()
    #...


if __name__=="__main__":
    print("O mesmo código cliente pode funcionar com diferentes subclasses: ")
    client_code(ConcreteClass1())

    print("O mesmo código cliente pode funcionar com diferentes subclasses: ")
    client_code(ConcreteClass2())
