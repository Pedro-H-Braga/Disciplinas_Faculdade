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
            # >> Receba a mensagem do CLIENTE
            msg = sockConn.recv(BUFFER_MSG)
            # transformando mensagem em string para entrar no match case
            #strMsg = msg.decode(CODE_PAGE) #BUG 
            # toda mensagem é adicionada na chave dict do client, na lista de mensagem
            message_history[addr].append(msg.decode(CODE_PAGE))
            # pegando da lista do split, o comando e colocando no match case 
            list_msg = split_(msg.decode(CODE_PAGE))
            # pegando da lista splitada da mensagem, apenas o comando dado
            try:
                comando  = list_msg[0]
                msgDest  = list_msg[1]
            except: 
                # comando recebendo o comando da mensagem, após dar out_of_index na lista
                comando = list_msg[0]

            match comando:
                # broadCast
                case '/b':            
                    b(msgDest, addr)
                # mostra comandos
                case '/?':
                    print(COMAND_ERROR)
                # exibe historico de mensagens do client
                case '/h':
                    h(sockConn, addr)
                # caso default do match case (se não for nenhuma das opções, cairá aqui)
                case _:
                    print('Comando não existe! Informe /? para ver as opções de comando...')
                               
        except Exception as e:
            print(e)
            msg = b'/q'
            # retirando host da lista de clientes conectados
            #allSocks.remove ((sockConn, addr))
        finally:
            # # para sair do loop
            # encerrando o socket (encerrando conexão com o cliente)
            sockConn.close()

# ----------------------- COMANDOS ---------------------- 

# pega a mensagem e o IP/PORTA do cliente que enviou   
#                        BROADCAST     
def b(msg, addrSource): # ENVIA MENSAGEM PARA TODOS CONECTADOS MENOS PRA QUEM ENVIOU
    # adicionando na mensagem o IP PORTA do cliente que enviou
    msg = f"From: {addrSource} -> {msg}"
    print(msg)
    # percorrendo todos os clientes da lista e enviando mensagem a todos hosts conectados menos a quem enviou 
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))

#                        HISTORICO
# exibe historico de comandos do client
def h(sockConn, addrSource):
    # history recebe do dict com seu addrSource, a lista com suas mensagens, ex: {localhost[]}
    historico = "\n".join(message_history.get(addrSource, []))
    # Enviando o histórico de mensagens do cliente.
    sockConn.send(historico.encode(CODE_PAGE))    

# ----------------------- FUNÇÕES ---------------------- 

# função para os comandos com argumentos, pegar os dados 
def split_(msg):
    try:
        list_msg = msg.split(':')
        return list_msg
    except Exception as e:
        print(f'Erro no split da mensagem...', e)
        return msg

#                           SERVIDOR: 
try:
    allSocks = []
    sockServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockServer.bind((IP_SERVER, PORT_SERVER))

    print ("Listening in: ", (IP_SERVER, PORT_SERVER))
    sockServer.listen(5)

    # Loop para aguardar conexões com clientes
    while True:
        # quando o cliente se conecta, é guardado na lista de allSock e é criado uma thread >>
        # >> para ele que executa a função de interação com o cliente 
        
        # addr é usado como variavel global, sendo usado em client para pegar quem se conectou ao server
        sockConn, addr = sockServer.accept()
        print ("Connection from: ", addr)

        allSocks.append((sockConn, addr))
        print('allSock: \n',allSocks, end='\n')
        try:
            tClient = threading.Thread(target=cliInteraction, args=(sockConn, addr))
            tClient.start()
        # tratando possivel erro na thread e finalizando o socket
        except Exception as e:
            print ("Fail: ", e)
        finally:
            sockServer.close()
except Exception as e:
    print ("Fail: ", e)
