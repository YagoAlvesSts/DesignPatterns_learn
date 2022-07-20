from facade import Facade

def client_code(facade: Facade) -> None:
    """
    O código cliente trabalha com subsistemas complexos através de uma interface
     simples fornecida pela Fachada. Quando uma fachada gerencia o ciclo de vida
     do subsistema, o cliente pode nem saber da existência do subsistema. Essa 
     abordagem permite manter a complexidade sob controle.
    """

    print(facade.operation(), end="")

