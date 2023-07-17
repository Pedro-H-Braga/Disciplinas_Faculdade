from const import *

# ----------------- FUNÇÕES SERVIDOR -----------------
# analisa mensagem do cliente, se diferente de !q, continua recebendo, senão remove o socket da lista 
def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'/q':
        try:
            msg = sockConn.recv(BUFFER_MSG)
            
            # decodificando para entrar no match case
            msg_str = msg.decode(CODE_PAGE)
            
            # fazer match case para msg, se encaixar em alguma alternativa, execute uma função
            match msg_str:
                case '/l':
                    l(msg, addr)
                case '/m':
                    m(msg, sock)                    
                
            # criar funções para cada funcionalidade
            
            broadCast (msg, addr)
        except:
            msg = b'/q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

# função que exibe: ipa mensagem que o cliente enviou  
def broadCast(msg, addrSource):
    # addrSource = ip do cliente que mandou
    msg = f"{addrSource} -> {msg.decode(CODE_PAGE)}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))

# ----------------- FUNÇÕES CLIENTE  -----------------
# função que recebe os dados do servidor
def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(BUFFER_MSG)
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

# função que pega input do cliente e manda pro servidor
def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE_PAGE))
        except:
            msg = '!q'
    closeSocket()

# função que fecha a conexã do socket
def closeSocket():
    try:
        sock.close()
    except:
        None

# ----------------- FUNÇÕES FUNCIONALIDADES -----------------

# listar o IP:porta dos clientes conectados no servidor;
def l(msg, addrSource):
    msg = f"IP | PORTA: -> {addrSource}"
    print (msg)
    # laço que percorre IP | PORTA  de todos os clientes e envia para todos
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))

# Enviar uma mensagem a um determinado cliente conectado no servidor
def m(msg, sock):
    # /m:ip_destino:porta:mensagem
    msg_str = msg.decode(CODE_PAGE)

    try:
        # pegando os dados do /m
        split_list = msg_str.split(':')
        ip_dest = split_list[1]
        port = split_list[2]
        msg_dest = split_list[3]
    except Exception as e:
        msg = 'O comando deve estar no seguinte formato: /m:ip_destino:porta:mensagem'
        sockConn.send(msg.encode(CODE_PAGE))
        print(f'ERROR: {e}')
    
    # enviar msg_dest para o ip/port informado
    # verificar se existe em allSocks
    sock.bind((ip_dest, port))
    print (f"Enviando -> {msg_dest}\npara: {ip_dest} | {port}")
    sock.listen(1)
    sockConn, addres = sock.accept()
    addrSource = ((sockConn, addres))
    print('Connect a: ', addrSource)
    if addrSource in allSocks:
        # envia a mensagem
        sockConn.send(msg_dest.encode(CODE_PAGE))
    else: 
        msg_error = 'Cliente não está conectado a rede! Tente outro ip | porta'
        sockConn.send(msg_error.encode(CODE_PAGE))
