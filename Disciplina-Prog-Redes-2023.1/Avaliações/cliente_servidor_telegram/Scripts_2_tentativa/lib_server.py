from constantes import *

# ----------------- FUNÇÕES SERVIDOR -----------------

def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'!q':
        try:
            msg = sockConn.recv(512)
            broadCast (msg, addr)
        except:
            msg = b'!q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

# ----------------- COMANDOS DO SERVIDOR -----------------

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))