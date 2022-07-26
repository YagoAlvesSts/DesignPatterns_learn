from interface.subject import Subject
from realsubject import RealSubject

class Proxy(Subject):
    """
    O proxy tem uma interface identica a RealSubject.
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        As aplicações mais comuns do padrão Proxy são carregamento lento, armazenamento em cache,
         controle de acesso, log, etc. Um Proxy pode realizar uma dessas coisas e então, dependendo 
         do resultado, passar a execução para o mesmo método em um objeto RealSubject vinculado .
        """

        if self.check_acess():
            self._real_subject.request()
            self.log_acess()

    def check_acess(self) -> bool:
        print("Proxy: Verificando o acesso antes de disparar uma solicitação real.")
        return True

    def log_acess(self) -> None:
        print("Proxy: Registrando a hora da solicitação.")
