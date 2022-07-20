class Subsystem1:
    """
    O Subsistema pode aceitar solicitações da fachada ou do cliente diretamente.
     De qualquer forma, para o Subsistema, a Fachada é mais um cliente, e não faz
     parte do Subsistema.
    """

    def operation1(self) -> str:
        return "Subsystem1: Ready"

    def operation_n(self) -> str:
        return "Subsystem1Pala: Go!"

class Subsystem2:
    """
    Algumas fachadas podem funcionar com vários subsistemas ao mesmo tempo
    """

    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


