import socket, threading
from constantes import *

def servInteraction():
    # Obtém o endereço do cliente que se conectou no servidor
    #addr_host = sockClient.getpeername()
    #print(addr_host)
    
    # se o cliente não estiver na lista de addr_host do dict, ele será incializado com um historico vazio
    #if addr_host not in message_history:
        # Cria uma lista vazia com a chave do dict sendo o addr do client.   
    #    message_history[addr_host] = []  

    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sockClient.recv(BUFFER_MSG)
            # decodificando a mensagem
            #strMsg = msg.decode(CODE_PAGE)
            # exibindo a mensagem
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
            # Adiciona a mensagem ao histórico do client
            #message_history[addr_host].append(strMsg)  
        except Exception as e:
            print(f'ERROR em servInteraction: {e}')
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            # se msg diferente que comando de saída, envie a mensagem para o servidor
            msg = input(PROMPT)
            if msg != '': sockClient.send(msg.encode(CODE_PAGE))

        except Exception as e:
            print(f'ERROR em userInteraction: {e}')
            msg = '/q'
    closeSocket()

def closeSocket():
    try:
        sockClient.close()
        print('fechando conexão...')
    except Exception as e: print('ERROR:', e)

try:
    sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockClient.connect((IP_CLIENTE, PORT_CLIENT))

    print ("Conectado a: ", (IP_CLIENTE, PORT_CLIENT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
# Se error no client, finalize o socket e exiba o error
except Exception as e:
    print ("Falha ", e)

