from interface.component import Component

class Decorator(Component):
    """
    A classe base Decorator segue a mesma interface dos outros componentes.
    O objetivo principal dessa classe é definir a interface de encapsulamento
    para todos os decoradores concrete. A implementação padrão do código de encapsulamento
    pode incluir um campo para armazenar um componente encapsulado e os meios para inicializá-los.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        O Decorator delega ao componente encapsulado.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()