import socket, sys, os

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from socket_constants import *

# Criando o socket UDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

while True:
    # Solicitar o arquivo
    nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair): ')
    
    # Enviando o nome do arquivo para o servidor
    print(f'\nSolicitando o arquivo {nome_arquivo}')
    nome_arquivo = nome_arquivo.lower() # tratando possivel erro de nome maiusculo
    tcp_socket.send(nome_arquivo.encode())
    
    if nome_arquivo.upper() == 'EXIT': break

    dado_recebido = tcp_socket.recv(BUFFER_SIZE)

    
    if dado_recebido.decode(CODE_PAGE) != 'O arquivo não existe!':
        
        print(dado_recebido.decode(CODE_PAGE))

        # Gravar o dado recebido em arquivo
        print(f'Gravando o arquivo {nome_arquivo}\n')
        nome_arquivo_ = ATUAL_DIR + '\\img_client\\' + nome_arquivo
        
        pct = 1
        with open(nome_arquivo_, 'wb') as arquivo:
            while True:
                # Recebendo o conteúdo do servidor
                dado_retorno = tcp_socket.recv(BUFFER_SIZE)          
                print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
                arquivo.write(dado_retorno)
                pct += 1
                if len(dado_retorno) < BUFFER_SIZE: break
    else: 
        print(dado_recebido.decode(CODE_PAGE))
        sys.exit()
# Fechando o socket
tcp_socket.close()