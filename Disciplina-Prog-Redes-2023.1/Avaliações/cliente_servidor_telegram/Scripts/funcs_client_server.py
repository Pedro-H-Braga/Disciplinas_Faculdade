from const import *
from funcs_comands import *

# ----------------- FUNÇÕES SERVIDOR -----------------
# analisa mensagem do cliente, se diferente de !q, continua recebendo, senão remove o socket da lista
def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'/q':
        try:
            msg = sockConn.recv(BUFFER_MSG)

            # decodificando para entrar no match case
            msg_str = msg.decode(CODE_PAGE)

            # fazer match case para msg, se encaixar em alguma alternativa, execute uma função
            match msg_str:
                case '/l':
                    l(msg, addr)
                case '/m':
                    m(msg, sock)
                case '/b':
                    b(msg, addr)
                case other:
                    print('Este comando não existe!')
        
        except:
            msg = b'/q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

# ----------------- FUNÇÕES CLIENTE  -----------------
# função que recebe os dados do servidor
def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(BUFFER_MSG)
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

# função que pega input do cliente e manda pro servidor
def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE_PAGE))
        except:
            msg = '/q'
    closeSocket()

# função que fecha a conexã do socket
def closeSocket():
    try:
        sock.close()
    except:
        None

