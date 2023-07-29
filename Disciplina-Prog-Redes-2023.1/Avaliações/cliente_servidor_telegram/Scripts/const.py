# --------- CONSTANTES -----------------
import socket

PORT         = 5678
SERVER       = 'localhost'
PROMPT       = 'Digite sua msg (/q para terminar) > '
CODE_PAGE    = 'utf-8'
BUFFER_MSG   = 512
COMAND_ERROR = '\
----------------------------------------------------------------------------------------------------------\
\tCOMANDOS DISPONÍVEIS:\
----------------------------------------------------------------------------------------------------------\
i. /q → sair do cliente;\n \
ii. /l → listar o IP:porta dos clientes conectados no servidor;\n \
iii. /m:ip_destino:porta:mensagem → Enviar uma mensagem a um determinado cliente conectado no servidor\n \
iv. /b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor\n \
v. /h → listar as mensagens já enviadas ao servidor pelo usuário (histórico);\n \
vi. /f → listar os arquivos (nome e tamanho) contidos na pasta /server_files (do servidor);\n \
vii. /d:nome_arquivo → efetuar o “download” do arquivo especificado para a pasta /download (do cliente);'
# --------- VARIAVEIS SOCKET -----------------
allSocks = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
