import socket, threading
from constantes import *


def cliInteraction(sockConn, addr):
    # inciando msg binario como vazia
    msg = b''
    # se a mensagem for igual do comando de encerramento, feche a conexão >>
    while msg != b'!q':
        try:
            # >> Receba a mensagem do CLIENTE e envie para todos hosts conectados
            msg = sockConn.recv(BUFFER_MSG)
            b(msg, addr)
        except:
            msg = b'!q'
    # retirando host da lista de clientes conectados
    allSocks.remove ((sockConn, addr))
    # encerrando o socket (encerrando conexão com o cliente)
    sockConn.close()

# ----------------------------- FUNÇÕES COMANDOS

# pega a mensagem e o IP/PORTA do cliente que enviou        
def b(msg, addrSource):
    # adicionando na mensagem o IP PORTA do cliente que enviou
    msg = f"{addrSource} -> {msg.decode(CODE_PAGE)}"
    print (msg)
    # percorrendo todos os clientes da lista e enviando mensagem a todos hosts conectados menos a quem enviou 
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))


# função para os comandos com argumentos, pegar os dados 
'''
def split_(msg):
    try:
        comunicacao = msg.split(':')
        return comunicacao
    except:
        print(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')
'''
try:
    allSocks = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((IP_SERVER, PORT))

    print ("Listening in: ", (IP_SERVER, PORT))
    sock.listen(5)

    # Loop para aguardar conexões com clientes
    while True:
        # quando o cliente se conecta, é guardado na lista de allSock e é criado uma thread >>
        # >> para ele que executa a função de interação com o cliente 
        sockConn, addr = sock.accept()
        print ("Connection from: ", addr)
        allSocks.append((sockConn, addr))
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        tClient.start()
except Exception as e:
    print ("Fail: ", e)
