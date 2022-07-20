from interface.component import Component

def client_code(component: Component) -> None:
    """O código do cliente trabalha com todos os componentes via interface base"""
    print(f"RESULT: {component.operation()}", end="")

def client_code2(component1: Component, component2: Component) -> None:
    """Graças ao fato de que as operações de gerenciamento filho são declaradas na classe base
    Component, o código cliente pode trabalhar com qualquer componente,
    simples ou complexo, sem depender de suas classes concretas."""

    if component1.is_composite():
        component1.add(component2)

    print(f"RESULT: {component1.operation()}", end="")