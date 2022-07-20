from interface.component import Component
from typing import List

class Composite(Component):
    """
    A classe Composite representa os componentes complexos que podem ter filhos.
    Normalmente, os objetos Composite delegam o trabalho real para seus filhos e então
    'soma' o resultado
    """
    def __init__(self) -> None:
        self._children: List[Component] = []
    
    """Um objeto composto pode adicionar ou remover outros componentes (simples ou complexos)
    de ou para sua lista de filhos."""

    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def operation(self) -> str:
        """
        O composite executa sua lógica primária de uma maneira particular.
        Ele percorre recursivamente todos os seus filhos, coletanto e somando seus resultados.
        Como os filhos do composto passam essas chamadas para seus filhos e assim por diante,
        toda a árvore de objetos é percorrida como resultado.
        """
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

        
