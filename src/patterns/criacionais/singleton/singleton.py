from singleton_meta import SingletonMeta

class Singleton(metaclass=SingletonMeta):

    def come_business_logic(self):
        """
        Finalmente, qualquer singleton deve definir a lógica de negócios, que pode ser executada em sua instância.
        """
        #...
