# --------- CONSTANTES -----------------
import socket

PORT        = 5678
SERVER      = 'localhost'
PROMPT      = 'Digite sua msg (!q para terminar) > '
CODE_PAGE   = 'utf-8'
BUFFER_MSG  = 512

# --------- VARIAVEIS SOCKET -----------------
allSocks = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
