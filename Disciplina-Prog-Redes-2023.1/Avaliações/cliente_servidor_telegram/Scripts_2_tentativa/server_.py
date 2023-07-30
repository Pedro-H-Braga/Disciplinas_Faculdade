import socket, threading
from constantes import *

# sockConn = objeto de conexão socket do cliente
# addr = address (IP/PORTA) do cliente
def cliInteraction(sockConn, addr):
    # inciando msg binario como vazia
    msg = b''
    # se a mensagem for igual do comando de encerramento, feche a conexão >>
    while msg != b'/q':
        try:
            # >> Receba a mensagem do CLIENTE e envie para todos hosts conectados
            msg = sockConn.recv(BUFFER_MSG)
            # transformando mensagem em string para entrar no match case
            strMsg = msg.decode(CODE_PAGE)
            match strMsg:
                # broadCast
                case '/b':            
                    b(msg, addr)
                case _:
                    print(COMAND_ERROR)

            '''
            # fazer match case para msg, se encaixar em alguma alternativa, execute uma função
            match msg_str:
                case '/q':
                    # envie mensagem de encerramento
                    msg = 'Encerrando conexão...'
                    sockConn.send(msg.encode(CODE_PAGE))
                    # remova o usuario da lista e feche a conexao
                    allSocks.remove ((sockConn, addr))
                    sockConn.close()    
                    # saia do loop                
                    exit()
                case '/l':
                    l(msg, addr)
                case '/b':
                    b(msg, addr)
                case _:
                    # envia mensagem de opções de comandos
                    sock.send(COMAND_ERROR.encode(CODE_PAGE))
            '''                                
        except:
            msg = b'/q'
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
