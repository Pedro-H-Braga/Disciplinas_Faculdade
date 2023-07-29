import socket, threading

# Definindo o ip local e a mesma porta do servidor para se conectar
SERVER = 'localhost'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '


def servInteraction():
    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sock.recv(512)
            # exibindo a mensagem
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode('utf-8'))
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
    sock.connect((SERVER, PORT))

    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except Exception as e:
    print ("Falha ", e)
