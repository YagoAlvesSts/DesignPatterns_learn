from .abstraction import Abstraction

class ExtendedAbstraction(Abstraction):
    """Você pode estender a abstração sem alterar as classes de implementação."""
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Operação extendida de: \n"
        f"{self.implementation.operation_implementation()}")

