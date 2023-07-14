from const import *

# ----------------- FUNÇÕES SERVIDOR -----------------

def cliInteraction(sockConn, addr):
    msg = b''
    while msg != b'!q':
        try:
            msg = sockConn.recv(BUFFER_MSG)
            broadCast (msg, addr)
        except:
            msg = b'!q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()

def broadCast(msg, addrSource):
    msg = f"{addrSource} -> {msg.decode('utf-8')}"
    print (msg)
    for sockConn, addr in allSocks:
        if addr != addrSource:
            sockConn.send(msg.encode('utf-8'))

# ----------------- FUNÇÕES CLIENTE  -----------------

def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(BUFFER_MSG)
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode('utf-8'))
        except:
            msg = '!q'
    closeSocket()

def closeSocket():
    try:
        sock.close()
    except:
        None
