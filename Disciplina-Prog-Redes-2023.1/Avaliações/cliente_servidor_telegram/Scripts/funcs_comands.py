# ----------------- FUNÇÕES FUNCIONALIDADES -----------------
# Funções das opções do servidor em clientInterection

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
    print (f"Enviando -> {msg_dest}\npara: {ip_dest} | {port}")
    sock.bind((ip_dest, port))
    sock.listen(1)
    sockConn, addres = sock.accept()
    addrSource = ((sockConn, addres))
    print('Connect a: ', addrSource)

    # verificar se existe em allSocks
    if addrSource in allSocks:
        # envia a mensagem
        sockConn.send(msg_dest.encode(CODE_PAGE))
    else:
        msg_error = 'Cliente NÃO está conectado ao servidor! Tente outro ip | porta'
        sockConn.send(msg_error.encode(CODE_PAGE))


# /b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor
def b(msg, addrSource):
    # addrSource = ip do cliente que mandou
    msg = f"{addrSource} -> {msg.decode(CODE_PAGE)}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))
