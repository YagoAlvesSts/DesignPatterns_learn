import copy

class SomeComponent:
    """
    Python fornece sua própria interface de Prototype via 'copy.copy' e funções 'copy.deepcopy'. 
    E qualquer classe que queira implementar implementações customizadas precisa subscrever as funções membro
    '__copy__' e '__deepcopy__'. 
    """

    def __init__(self, some_int, some_list_of_objects, some_circular_ref):
        self.some_int = some_int
        self.some_list_of_objects = some_list_of_objects
        self.some_circular_ref = some_circular_ref

    
    def __copy__(self):
        """
        Cria uma cópia superficial. Este método será chamado sempre que alguém chamar 'copy.copy' com este objeto
        e o valor retornado é retornado como a nova cópia superficial.
        """

        """Criando cópia de objetos aninhados"""
        some_list_of_objects = copy.copy(self.some_list_of_objects)
        some_circular_ref = copy.copy(self.some_circular_ref)

        """Clonando o próprio objeto, usando os clones preparados dos objetos aninhados"""
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__.update(self.__dict__)

        return new


    def __deepcopy__(self, memo=None):
        """
        Cria uma cópia profunda.
        Este método será chamado sempre que alguém chamar 'copy.deepcopy' com este objeto e o valor retornado é retornado
        como a nova cópia profunda.
        Memo é o dicionário usado pela biblioteca 'deepcopy' para evitar cópias recursivas infinitas em instâncias de referências
        circulares.
        Passe-o para todas as chamadas 'deepcopy' que você fizer na implementação '__deepcopy__' para evitar recursôes infinitas.
        """

        if memo is None:
            memo = {}

        """Primeiro, cria-se copias de objetos aninhados"""
        some_list_of_objects = copy.deepcopy(self.some_list_of_objects, memo)
        some_circular_ref = copy.deepcopy(self.some_circular_ref, memo)

        """Clonando o próprio objeto, usando os clones preparados dos objetos aninhados"""
        new = self.__class__(self.some_int, some_list_of_objects, some_circular_ref)
        new.__dict__ = copy.deepcopy(self.__dict__, memo)

        return new
