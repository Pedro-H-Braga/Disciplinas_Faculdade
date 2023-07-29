from constantes import *
from lib_comandos import *
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


