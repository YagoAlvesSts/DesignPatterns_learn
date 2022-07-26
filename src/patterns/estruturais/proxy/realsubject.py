from interface.subject import Subject

class RealSubject(Subject):
    """
    O RealSubject contém alguma lógica de negócios principal. Normalmente, RealSubjects são capazes
     de fazer algum trabalho útil que também pode ser muito lento ou sensível - por exemplo, 
     corrigindo os dados de entrada. Um Proxy pode resolver esses problemas sem nenhuma alteração no código do RealSubject.
    """

    def request(self) -> None:
        print("RealSubject: Solicitação de tratamento.")

