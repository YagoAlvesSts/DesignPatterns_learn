import json

class Flyweight():
    """
    O Flyweight armazena uma parte comum do estado (também chamado de estado intrínseco) que pertence 
    a várias entidades de negócios reais. O Flyweight aceita o restante do estado (estado extrínseco, 
    único para cada entidade) por meio de seus parâmetros de método.
    """

    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


