from .adaptee import Adaptee
from .target import Target

class Adapter(Target, Adaptee):
    """ O Adapter torna a interface do Adaptee compatíivel com a interface do Target por meio de herança múltipla."""
    def request(self) -> str:
        return f'Adapter: (TRANSLATED) {self.specific_request()[::-1]}'
