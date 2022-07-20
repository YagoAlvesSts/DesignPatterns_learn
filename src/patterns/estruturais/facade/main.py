from subsystem.subsystem import Subsystem1, Subsystem2
from client_code import client_code
from facade import Facade

if __name__ == "__main__":
    """
    # O código cliente pode ter alguns objetos do subsistema já criados.

    # Neste caso, pode valer a pena inicializar a Fachada com estes
      objetos em vez de deixar a Fachada criar novas instâncias.
    """

    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)