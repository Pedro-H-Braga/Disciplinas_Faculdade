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
    # Aceita a conexão com o cliente
    conexao, ip_cliente = tcp_socket.accept()       
    print(f'\nO cliente: <{ip_cliente}> se conectou ao servidor!')
except: print(f'\nERROR ao tentar conecta o servidor!\nERRO: {sys.exc_info()[0]}')

try:
    while True:
        # Recebendo mensagem do cliente
        mensagem = conexao.recv(BUFFER_SIZE).decode()

        if mensagem.upper() == 'EXIT':
            print(f'\nO CIENTE {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
            # Fechando conexoes
            conexao.close()
            tcp_socket.close()   

        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = ATUAL_DIR + '\\img_server\\' + mensagem
            ver_arquivo = os.path.isfile(nome_arquivo)
            if ver_arquivo == True:
                try:
                    tamanho_arquivo = os.path.getsize(nome_arquivo)
                    pacotes = int(tamanho_arquivo/BUFFER_SIZE)
                    msg = f'\nO arquivo tem: {tamanho_arquivo} Bytes\n\nSerão enviados {pacotes+1} pacotes!\n'
                    conexao.send(msg.encode(CODE_PAGE))
                    print(f'Enviando arquivo {mensagem} ...')
                # tratando os possíveis erros
                except: 
                    print('\nProblemas com o arquivo!')
                finally:    
                    # Fechando o socket
                    tcp_socket.close()

                with open(nome_arquivo, 'rb') as arquivo:
                    while True:
                        data_retorno = arquivo.read(BUFFER_SIZE)
                        conexao.send(data_retorno)
                        if not data_retorno: break                                

                print(f'Arquivo {mensagem.lower()} Enviado...')
            else:
                conexao.send('\nO arquivo não existe!'.encode(CODE_PAGE))
                tcp_socket.close()    
                conexao.close()
                break

except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    # Fechando o socket
    tcp_socket.close()    
'''
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    tcp_socket.close()
'''
    
'''
- Quando o cliente solicitar um arquivo, o servidor deverá verificar a existência do arquivo para pode enviá-lo, caso não exista, o servidor deverá informar ao cliente que o arquivo não existe; 
- O arquivo existindo, o servidor deverá informar ao cliente quantos pacotes serão enviados antes de começar a enviá-los;
- O cliente deverá informar qual o pacote que está sendo recebido no formato pacote: atual / total;
- Possíveis exceções deverão ser tratadas;
- Os arquivos da aplicação deverão ser salvos no mesmo diretório;
- Os diretórios img_server e img_client deverão ser criados no mesmo diretório onde estão os arquivos da aplicação
'''