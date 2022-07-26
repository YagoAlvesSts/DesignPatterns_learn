
from flyweight import Flyweight
from typing import Dict

class FlyweightFactory():
    """
    A Flyweight Factory cria e gerencia os objetos Flyweight. Ele garante que os flyweights sejam compartilhados corretamente. 
    Quando o cliente solicita um flyweight, a fábrica retorna uma instância existente ou cria uma nova, caso ainda não exista.
    
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweight: Dict) -> None:
        for state in initial_flyweight:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        Retorna o hash de string de um Flyweight para um determinado estado.
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        Retorna um Flyweight existente com um determinado estado ou cria um novo.
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: não foi possível encontrar um flyweight, criando um novo.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: reusando flyweight existente.")
        
        return self._flyweights[key]

    
    def list_flyweight(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: Eu tenho {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")
