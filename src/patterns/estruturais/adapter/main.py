from interface.target import Target
from interface.adaptee import Adaptee
from interface.adapter import Adapter
from client_code import client_code



if __name__ == "__main__":
    print("Client: Eu posso trabalhar muito bem com os objetos Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: A classe Adaptee tem uma interface estranha. \n Veja, não entendi:")
    print(f'Adaptee: {adaptee.specific_request()}', end="\n\n")

    print("Client: Mas eu posso trabalhar com ele através do Adapter: ")
    adapter = Adapter()
    client_code(adapter)
