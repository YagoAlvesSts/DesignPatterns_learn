from interface.component import Component
def client_code(component: Component) -> None:
    """
    O código do cliente funciona com todos os objetos usando a interface Component.
    Dessa forma, ele pode ficar independentes das classes concretas de componentes com os quais trabalha.
    """


    #...

    print(f"RESULT: {component.operation}", end="")

    #...
