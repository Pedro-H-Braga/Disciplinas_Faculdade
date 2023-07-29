from const import *
from funcs_comands import *

# ----------------- FUNÇÕES SERVIDOR -----------------
# analisa mensagem do cliente, se diferente de !q, continua recebendo, senão remove o socket da lista
def cliInteraction(sockConn, addr):
    msg = b''
    while True:
        try:
            msg = sockConn.recv(BUFFER_MSG)

            # decodificando para entrar no match case
            msg_str = msg.decode(CODE_PAGE)

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
        
        except Exception as e:
            print('ERROR: ', e)
            break
    closeSocket()
    
# ----------------- FUNÇÕES CLIENTE  -----------------
# função que recebe os dados do servidor
def servInteraction():
    while True:
        try:
            msg = sock.recv(BUFFER_MSG)
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except Exception as e:
            # exiba o error e saia do loop
            print('ERROR: ', e)
            exit()

# função que pega input do cliente e manda pro servidor
def userInteraction():
    msg = ''
    while True:
        try:
            msg = input(PROMPT)   
            # Se a mensagem não for vazia, envie ao servidor
            if msg != '':
                sock.send(msg.encode(CODE_PAGE))  
        except:
            msg = '/q'

# função que fecha a conexã do socket
def closeSocket():
    try:
        sock.close()
    except:
        None

