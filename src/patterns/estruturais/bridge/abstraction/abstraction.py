from interface.implementation import Implementation

class Abstraction:
    """A abstração define a interface para a parte "controle" das duas hierarquias de classes.
    Ele mantém uma referência a um objeto da hierarquia implementação e delega todo o trabalho real a esse objeto."""

    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with: \n"
        f"{self.implementation.operation_implementation()}")
