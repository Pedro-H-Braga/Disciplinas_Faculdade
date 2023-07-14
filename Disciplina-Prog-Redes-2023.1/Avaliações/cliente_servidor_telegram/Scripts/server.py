import socket, threading, sys
from const import *

def cliInteraction(sockConn, addr):
    # recebe os bytes do cliente enquanto tiver quadro
    msg = b''
    while msg != b'!q':
        try:            
            msg = sockConn.recv(BUFFER_MSG)
            # função que faz o decode da mensagem e exibe o cliente e a mensagem
            broadCast (msg, addr)
        except:
            # se erro, saia a partir da mensagem reservada !q
            msg = b'!q'
    # tirando o cliente da lista dos sockets conectados
    allSocks.remove ((sockConn, addr))
    # fechando conexão
    sockConn.close()

def broadCast(msg, addrSource): # addrSource = ip cliente
    # msg recebe os dados do cliente e a mensagem
    msg = f"{addrSource} -> {msg.decode(CODE_PAGE)}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))

try:
    # lista que guardará todas as conexoes (ip-porta)
    allSocks = []
    # criando socket e ouvindo nas portas indicadas
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # sock_type recebe se é UDP ou TCP e exibe uma mensagem de acordo com o protocolo
    #if sock.type == 1: print('\nProtocolo utilizado na conexão: TCP\n')
    #else: print('\nProtocolo utilizado na conexão: UDP\n')

    # escutando em localhost e na porta 5000
    sock.bind((SERVER_SERV, PORT))
    print ("Escutando em: ", (SERVER_SERV, PORT))

    # Aguenta até 5 clientes
    sock.listen(5)      
        
    while True:
        # sock e addr recebem os dados da coneão aceita
        sockConn, addr = sock.accept()
        print (f"Connection from: ", addr)
        # adicionando a conexão na lista de todas conexões
        allSocks.append((sockConn, addr))
        # criando uma thread para cada conexão
        tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
        # iniciando essa thread
        tClient.start()
               
except Exception as e:
    print ("ERROR: ", e)
    sys.exit()
