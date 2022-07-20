from decorator.decorator import Decorator


class ConcreteDecoratorA(Decorator):
    """
    Os Decorators Concrete chamam o objeto encapsulado e alteram seu resultado de alguma forma.
    """

    def operation(self) -> str:
        """
        Os decorators podem chamar a implementação pai da operação, em vez de chamar o objeto 
        encapsulado diretamente.
        Essa abordagem simplifica a extensão das classes do decorator.
        """

        return f'ConcreteDecoratorA({self.component.operation()})'

class ConcreteDecoratorB(Decorator):
    """
    Decorators podem executar seu comportamento antes ou depois da chamada para um objeto encapsulado.
    """
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"
