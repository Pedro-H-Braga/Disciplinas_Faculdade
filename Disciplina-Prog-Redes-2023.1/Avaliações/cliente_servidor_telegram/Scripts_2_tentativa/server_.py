import socket, threading

# O IP do servidor tem que ficar em 0.0.0.0 para poder receber conexão de vários hosts
SERVER = '0.0.0.0'
PORT = 5678


def cliInteraction(sockConn, addr):
    # inciando msg binario como vazia
    msg = b''
    # se a mensagem for igual do comando de encerramento, feche a conexão >>
    while msg != b'!q':
        try:
            # >> Receba a mensagem do CLIENTE e envie para todos hosts conectados
            msg = sockConn.recv(512)
            broadCast (msg, addr)
        except:
            msg = b'!q'
    # retirando host da lista de clientes conectados
    allSocks.remove ((sockConn, addr))
    # encerrando o socket (encerrando conexão com o cliente)
    sockConn.close()

# pega a mensagem e o IP/PORTA do cliente que enviou        
def broadCast(msg, addrSource):
    # adicionando na mensagem o IP PORTA do cliente que enviou
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    # percorrendo todos os clientes da lista e enviando mensagem a todos hosts conectados menos a quem enviou 
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))

try:
    allSocks = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((SERVER, PORT))

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
