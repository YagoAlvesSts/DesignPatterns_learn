from interface.subject import Subject

def client_code(subject: Subject) -> None:
    """
    O código do cliente deve funcionar com todos os objetos (tanto subjects quanto proxies)
     por meio da interface Subject para oferecer suporte a assuntos reais e proxies. Na vida
     real, no entanto, os clientes geralmente trabalham diretamente com seus assuntos reais.
     Nesse caso, para implementar o padrão com mais facilmente, você pode estender seu proxy da classe do real subject's.
    """

    #...

    subject.request()

    #...