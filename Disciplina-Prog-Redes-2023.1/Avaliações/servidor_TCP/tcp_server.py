import socket, sys, os, time

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from socket_constants import *

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular o socket a tupla (host, port)
tcp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

print(f'\nSERVIDOR ATIVO: {tcp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

try:
    while True:
        # Aceita a conexão com o cliente
        conexao, ip_cliente = tcp_socket.accept()       
        print(f'\nO cliente: <{ip_cliente}> se conectou ao servidor!')

        while True:
            mensagem_cod = conexao.recv(BUFFER_SIZE)
            mensagem = mensagem_cod.decode(CODE_PAGE)
            if mensagem.upper() == 'EXIT':
                print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
            else:
                # Nome do arquivo a ser enviado
                nome_arquivo = ATUAL_DIR + '\\img_server\\' + mensagem
                print(f'Enviando arquivo {mensagem.lower()} ...')
                try:
                    tamanho_arquivo = os.path.getsize(nome_arquivo)
                    msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
                    conexao.send(msg.encode(CODE_PAGE))
                # tratando os possíveis erros
                except FileNotFoundError:
                    print('Nâo foi possível encontrar o arquivo!')
                except: 
                    print(f'\nERRO: {sys.exc_info()[0]}')
                finally:    
                    # Fechando o socket
                    tcp_socket.close()

                arquivo = open(nome_arquivo, 'rb')
                while True:
                    data_retorno = arquivo.read(BUFFER_SIZE)
                    if not data_retorno: break                                
                    conexao.send(data_retorno)
                    time.sleep(0.02)
                print(f'Arquivo {mensagem.upper()} Enviado...')
                arquivo.close()
except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    # Fechando o socket
    tcp_socket.close()    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    tcp_socket.close()

'''
- Quando o cliente solicitar um arquivo, o servidor deverá verificar a existência do arquivo para pode enviá-lo, caso não exista, o servidor deverá informar ao cliente que o arquivo não existe; 
- O arquivo existindo, o servidor deverá informar ao cliente quantos pacotes serão enviados antes de começar a enviá-los;
- O cliente deverá informar qual o pacote que está sendo recebido no formato pacote: atual / total;
- Possíveis exceções deverão ser tratadas;
- Os arquivos da aplicação deverão ser salvos no mesmo diretório;
- Os diretórios img_server e img_client deverão ser criados no mesmo diretório onde estão os arquivos da aplicação
'''