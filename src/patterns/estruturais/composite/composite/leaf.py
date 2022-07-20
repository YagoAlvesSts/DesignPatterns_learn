from interface.component import Component

class Leaf(Component):
    """
    A classe Leaf representa os objetos finais de uma composição.
    Uma folha não pode ter filhos.
    Normalmente são os objetos Leaf que fazem o trabalho real, enquanto os objetos Composite
    apenas delegam seus subcomponentes.
    """
    def operation(self) -> str:
        return "Leaf"