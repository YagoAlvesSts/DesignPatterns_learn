from realsubject import RealSubject
from client_code import client_code
from proxy import Proxy

if __name__ == "__main__":
    print("Client: executando o código do cliente com um assunto real:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("Client: Executando o mesmo código de cliente com um proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)