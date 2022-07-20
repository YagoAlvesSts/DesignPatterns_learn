from composite.leaf import Leaf
from client_code import client_code, client_code2
from composite.composite import Composite


if __name__ == "__main__":
    #Deste jeito o código cliente consegue dar suporte a componentes simples leaf
    simple = Leaf()
    print("Cliente: Eu tenho um componente simples: ")
    client_code(simple)
    print("\n")

    #... bem como os composites complexos
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    print("Client: Agora eu tenho uma árvore composite: ")
    client_code(tree)
    print("\n")

    print("Client: Eu não preciso checar as classes de componentes quando gerencio a árvore: ")
    client_code2(tree, simple)
