from interface.component import Component

class ConcreteComponent(Component):
    """
    Os componentes concretos fornecem implementações padrão das operações. 
    Pode haver várias variações dessas classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"
        