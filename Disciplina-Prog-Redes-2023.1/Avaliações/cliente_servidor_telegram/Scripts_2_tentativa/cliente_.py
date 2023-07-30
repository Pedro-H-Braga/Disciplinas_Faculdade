import socket, threading
from constantes import *

def servInteraction():
    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sock.recv(BUFFER_MSG)
            # exibindo a mensagem
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            # se msg diferente que comando de saída, envie a mensagem para o servidor
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE_PAGE))
        except:
            msg = '!q'
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
