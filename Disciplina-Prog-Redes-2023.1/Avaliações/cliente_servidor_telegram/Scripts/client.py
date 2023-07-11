import socket, threading
from const import *

# funcao que pega os dados enviados pelo servidor e decodifica
def servInteraction():
    msg = b' '
    # enquanto tiver mensagem
    while msg != b'':
        try:
            # receba a mensagem e guarda na variavel msg
            msg = sock.recv(BUFFER_MSG)
            # exiba a mensagem que chegou do servidor
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except:
            # não deixe a mensagem vazia
            msg = b''
    # fechando conexão
    closeSocket()

# funcao que envia dados para o servidor
def userInteraction():
    msg = ''
    # enquanto tiver dados para enviar, diferente de !q
    while msg != '!q':
        try:
            # pegando input com mensagem padrão 
            msg = input(PROMPT)
            # se a mensagem nao for vazia, envie para o servidor
            if msg != '': sock.send(msg.encode(CODE_PAGE))
        except:
            msg = '!q'
    closeSocket()

# Fecha conexão com o servidor
def closeSocket():
    try:
        sock.close()
    except:
        None

try:
    # criando o socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))
    # exibindo as portas em que foram conectadas
    print ("Conectado a: ", (SERVER, PORT))
    # isolando em uma thread a funcao que recebe dados do servidor 
    tServer = threading.Thread(target=servInteraction)
    # isolando em uma thread a funcao que envia dados para o servidor 
    tUser = threading.Thread(target=userInteraction)

    # colocando as threads para rodar (inciando as threads) 
    tServer.start()
    tUser.start()
    # Fazendo com que uma thread acabe para que a outra possa rodar (para garantir que todas as threads tenha executado para prosseguir)
    tServer.join()
    tUser.join()

except Exception as e:
    print ("Falha ", e)

