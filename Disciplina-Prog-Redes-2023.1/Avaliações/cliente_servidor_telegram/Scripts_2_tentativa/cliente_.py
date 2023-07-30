import socket, threading

# Definindo o ip local e a mesma porta do servidor para se conectar
SERVER = 'localhost'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '

CODE_PAGE    = 'utf-8'
BUFFER_MSG   = 512
COMAND_LIST  = [
'/q','/l','/m','/b','/h','/f','/d','/u','/w','/rss','/?']

COMANDOS = '\
\n---------------------------------------------------------------------------------------------------------- \n\
\tCOMANDOS DISPONÍVEIS:\t\
\n---------------------------------------------------------------------------------------------------------- \n\
/q → sair do cliente;\n \
/l → listar o IP:porta dos clientes conectados no servidor;\n \
/m:ip_destino:porta:mensagem → Enviar uma mensagem a um determinado cliente conectado no servidor\n \
/b:mensagem → Enviar uma mensagem para todos os clientes conectados no servidor\n \
/h → listar as mensagens já enviadas ao servidor pelo usuário (histórico);\n \
/f → listar os arquivos (nome e tamanho) contidos na pasta /server_files (do servidor);\n \
/d:nome_arquivo → efetuar o “download” do arquivo especificado para a pasta /download (do cliente);\n \
/u:nome_arquivo →efetuar o “upload” de um arquivo para a pasta /server_files (do servidor);\n \
/w:url →efetuar o download do arquivo fornecido na url para a pasta /server_files (do servidor);\n \
/rss:palavra_chave →listar as 10 notícias mais recentes que contenham a palavra_chave. Deverá ser habilitado pelo menos 10 URLs que forneçam conteúdo em formato RSS;\n \
/? → exibir uma ajuda (listar as opções contidas nesse roteiro).'

def servInteraction():
    # mensagem com espaço para entrar no loop enquanto a mensagem não for vazia
    msg = b' '
    while msg != b'':
        try:
            # recebendo dados do servidor
            msg = sock.recv(512)
            # exibindo a mensagem
            print ("\n"+msg.decode('utf-8')+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def userInteraction():
    msg = ''
    while msg != '!q':
        try:
            # se msg diferente que comando de saída, envie a mensagem para o servidor
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

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))

    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=servInteraction)
    tUser = threading.Thread(target=userInteraction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
except Exception as e:
    print ("Falha ", e)
