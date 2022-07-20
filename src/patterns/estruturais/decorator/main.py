from concretes.component import ConcreteComponent
from client_code import client_code
from concretes.decorator import ConcreteDecoratorA, ConcreteDecoratorB


if __name__ == "__main__":
    #Deste jeito o código do cliente consegue suportar ambos componentes simples...
    simple = ConcreteComponent()
    print("\nCliente: Eu tenho um componente simples: ")
    client_code(simple)
    print("\n")

    #..assim como os decoradores

    #Observe como os decoradores podem envolver não apenas componentes simples
    #mas também os outros decoradores
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    print("Cliente: Agora eu tenho um componente decorado. \n")
    client_code(decorator2)

