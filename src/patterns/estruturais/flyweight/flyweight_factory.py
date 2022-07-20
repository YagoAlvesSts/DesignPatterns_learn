
from flyweight import Flyweight
from typing import Dict

class FlyweightFactory():
    """
    
    """

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweight: Dict) -> None:
        for state in initial_flyweight:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state: Dict) -> str:
        """
        
        """
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        """
        
        """

        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        
        return self._flyweights[key]

    
    def list_flyweight(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self._flyweights.keys())), end="")
