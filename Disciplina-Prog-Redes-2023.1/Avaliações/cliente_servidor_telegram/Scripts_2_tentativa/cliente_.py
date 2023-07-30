import socket, threading
from constantes import *

def servInteraction():
    # Obtém o endereço do cliente que se conectou no servidor
    addr_host = sock.getpeername()
    # se o cliente não estiver na lista de addr_host do dict, ele será incializado com um historico vazio
    if addr_host not in message_history:
        # Cria uma lista vazia com a chave do dict sendo o addr do client.   
        message_history[addr_host] = []  

    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sock.recv(BUFFER_MSG)
            # decodificando a mensagem
            strMsg = msg.decode(CODE_PAGE)
            # exibindo a mensagem
            print ("\n"+strMsg+"\n"+PROMPT)
            # Adiciona a mensagem ao histórico do client
            message_history[addr_host].append(strMsg)  
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            # se msg diferente que comando de saída, envie a mensagem para o servidor
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE_PAGE))

        except:
            msg = '/q'
    closeSocket()

def closeSocket():
    try:
        sock.close()
    except:
        None

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP_CLIENTE, PORT))

    print ("Conectado a: ", (IP_CLIENTE, PORT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except Exception as e:
    print ("Falha ", e)
