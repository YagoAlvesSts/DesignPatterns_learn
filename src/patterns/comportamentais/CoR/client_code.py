from handler.interface.handler import Handler

def client_code(handler: Handler) -> None:
    """
    O código do cliente geralmente é adequado para trabalhar com um único manipulador.
     Na maioria dos casos, nem sequer está ciente de que o manipulador faz parte de uma cadeia.
    """
    for food in ["Nut", "Banana", "Cup of coffe"]:
        print(f"\nClient: quem quer um {food}?")
        result = handler.handle(food)
        if result:
            print(f"    {result}", end="")
        else: 
            print(f"    {food} não foi tocada.", end="")