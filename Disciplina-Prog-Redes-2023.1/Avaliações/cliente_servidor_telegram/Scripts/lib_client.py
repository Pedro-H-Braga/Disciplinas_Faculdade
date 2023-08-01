from constantes import *

# ----------------- FUNÇÕES CLIENTE -----------------

def servInteraction():
    msg = b' '
    while msg != b'':
        try:
            msg = SOCK.recv(BUFFER_MSG)
            print ("\n"+msg.decode(CODE_PAGE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': SOCK.send(msg.encode(CODE_PAGE))
        except:
            msg = '/q'
    closeSocket()

def closeSocket():
    try:
        SOCK.close()
    except:
        None
