import threading
from const import *
from funcs_client_server import *

try:
    # Conectando o cliente pelo IP/PORTA ao servidor
    sock.connect((SERVER, PORT))

    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()


except Exception as e:
    print ("ERROR: ", e)
