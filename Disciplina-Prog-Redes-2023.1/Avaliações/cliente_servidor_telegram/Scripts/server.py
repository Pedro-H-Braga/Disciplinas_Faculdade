import threading
from const import *
from funcoes import *

try:
    sock.bind((SERVER, PORT))

    # sock_type recebe se é UDP ou TCP e exibe uma mensagem de acordo com o protocolo
    if sock.type == 1: print('\nProtocolo utilizado na conexão: TCP\n')
    else: print('\nProtocolo utilizado na conexão: UDP\n')

    print ("Listening in: ", (SERVER, PORT))
    sock.listen(5)

    while True:
        sockConn, addr = sock.accept()
        print ("Connection from: ", addr)
        allSocks.append((sockConn, addr))
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        tClient.start()
except Exception as e:
    print ("Fail: ", e)
