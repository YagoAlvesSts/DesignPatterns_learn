from subsystem.subsystem import Subsystem1, Subsystem2

class Facade:
    """
    A classe Facade fornece uma interface simples para a lógica complexa de um ou vários 
    subsistemas. A Fachada delega as solicitações do cliente aos objetos apropriados dentro 
    do subsistema. A Fachada também é responsável por gerenciar seu ciclo de vida. Tudo isso
    protege o cliente da complexidade indesejada do subsistema.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
        Dependendo das necessidades do seu aplicativo, você pode fornecer à Fachada objetos de
         subsistema existentes ou forçar a Fachada a criá-los por conta própria.
        """

        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()


    def operation(self) -> str:
        """
        Os métodos do Facade são atalhos convenientes para a funcionalidade sofisticada dos
         subsistemas. No entanto, os clientes obtêm apenas uma fração dos recursos de um
         subsistema.
        """

        results = []
        results.append("Fachada de subsistemas inicializada: ")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("A fachada ordena que os subsistemas executem a ação: ")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)
