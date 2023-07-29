# ----------------- FUNÇÕES FUNCIONALIDADES -----------------
# Funções das opções do servidor em clientInterection
from const import *

# listar o IP:porta dos clientes conectados no servidor;
def l(msg, addrSource):
    msg = f"IP | PORTA: -> {addrSource}"
    print (msg)
    # laço que percorre IP | PORTA  de todos os clientes e envia para todos
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))


# /b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor
def b(msg, addrSource):
    # addrSource = ip do cliente que mandou
    msg = f"{addrSource} -> {msg.decode(CODE_PAGE)}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE_PAGE))
