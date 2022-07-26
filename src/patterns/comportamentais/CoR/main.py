from handler.concrete_handler import MonkeyHandler, DogHandler, SquirrelHandler
from client_code import client_code

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # O cliente deve ser capaz de enviar uma solicitação para qualquer manipulador,
    # não apenas para o primeiro na cadeira
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
