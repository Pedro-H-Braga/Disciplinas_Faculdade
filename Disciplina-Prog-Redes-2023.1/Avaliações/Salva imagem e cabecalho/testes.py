import ssl, os
import socket, sys


# input que pegue as urls e divida a url para cada variavel
url = input('Informe a URL da imagem: ')

# separando url 
list_split = url.split('/')

# Para verificar se é http ou https 
protocolo = list_split[0] 
protocolo = protocolo[:-1]
# IF de, se URL diferente de http|https, saia
if protocolo == 'http' or protocolo == 'https':
    print(f'O protocolo é: {protocolo[:-1]}')

else: 
    print(f'O código para o protocolo {protocolo} ainda está em desenvolvimento, por favor aguarde...')
    sys.exit()

# URL host
url_host      = list_split[2]

# URL imagem
# pegando a url da imagem desde a url do host para depois
tamanho_url_host  = len(url_host)
delimiter_url = url.find(url_host)
url_imagem    = url[delimiter_url+tamanho_url_host:]

# pegando url do arquivo
url_arq       = list_split[-1]
print(f'url_host: {url_host}\nurl_img: {url_imagem}\nurl_arq: {url_arq}')
print('-'*100)

# criando socket tcp
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Criando Socket IPV4, protocolo TCP')


#       BAIXANDO IMAGEM   |   TRANSFORMANDO O CABEÇALHO DA IMAGEM EM ARQUIVO TXT
#  -------------------------------------------------------------------------------

# pegando o caminho do arquivo .py
dir_atual = os.path.dirname(os.path.realpath(__file__))

buffer = 4096

invalidos = [':','/','*','?','"','<','>','|',"'",'.']

# ---------------------------------------------------------------

# HTTPS
def conection_https(url_imagem,url_arq,url_host,sockt):

    # Construir requisição HTTP para obter o feed RSS
    request = f"GET {url_imagem} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n"

    # Iniciar conexão segura com o servidor modelo SSL
    context = ssl.create_default_context()

    # previne o erro de certificação ssl 
    context.check_hostname = False          
    context.verify_mode = ssl.CERT_NONE 

    # Fazendo a conexão com o servidor a partir do socket tcp 
    socket_rss_wrap = context.wrap_socket(sockt, server_hostname=url_host)
    socket_rss_wrap.connect((url_host, 443))

    # Enviar a requisição
    print('Enviando requisição ao Servidor!')
    socket_rss_wrap.send(request.encode())
    print('Recebendo requisição e processando os bytes... Aguarde!')

    # Receber a resposta
    retorno_bin = b''
    while True:
        resposta = socket_rss_wrap.recv(buffer)
        if not resposta: break
        retorno_bin += resposta
        
    # Separando o Cabeçalho dos Dados da imagem
    delimiter_img = '\r\n\r\n'.encode()
    position  = retorno_bin.find(delimiter_img)
    image     = retorno_bin[position+4:]               # DADOS DA REQUEST (imagem em bytes)
    headers   = retorno_bin[:position].decode('utf-8') # CABEÇALHO 
    
    # pegando a extensao do arquivo que vem no header, no seguinte formato 'tipo_arquivo/extensao' (por isso o split[1]), pegando a u
    position_header = headers.find('Content-Type')
    tipo_extensao = headers[position_header:].split()[1] # pegando a extensão e o tipo do arquivo a partir do split
    extensao_str = tipo_extensao.split('/')[-1] # pegando apenas a extensão
    extensao = '.' + extensao_str 

    # quebrando o nome do arquivo para manipulação
    sem_extensao = url_arq.split('.')

    # se não tiver extensão no nome do arquivo, insira e pegue o nome do arquivo sem extensão
    if len(sem_extensao) == 1:
        url_arq = url_arq + extensao
    
    url_arq_txt   = sem_extensao[0]

    #         PEGANDO OS BYTES E ESCREVENDO EM UM ARQUIVO PARA TRANSFORMAR EM IMAGEM
    try:
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')
    except:
        # se erro, troque os caracteres especiais no nome do arquivo por '-' e adicione a extensão, mesmo que já tenha (por precaução)
        delim = url_arq.find(sem_extensao[-1])
        url_arq = url_arq[:delim]
        # laço que percorre a lista com os caracteres inválidos, trocando-os por '-'
        for char_troca in invalidos:
            url_arq = url_arq.replace(char_troca,'-')
        # adicionando a extensão no arquivo
        url_arq = url_arq + extensao
        # criando o arquivo 
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')

    file_output.write(image)
    file_output.close()
    print('Imagem salva com sucesso!')

    #         PEGANDO HEADER DA URL E JOGANDO PARA UM ARQUIVO TXT
    try:
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')
    except:
        # laço que percorre a lista com os caracteres inválidos, trocando-os por '-'
        for char_troca in invalidos:
            url_arq_txt = url_arq_txt.replace(char_troca,'-')
        # criando o arquivo 
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')

    file_header.write(headers)
    file_header.close()
    print('Arquivo texto criado com sucesso!')

#  -------------------------------------------------------------------------------

# HTTP
def conection_http(url_imagem,url_arq,url_host,sockt):

    # pegando header da imagem:
    # connection close já corta conexão quando termina o pacote, sem precisar ficar em loop no while
    url_request = f"GET {url_imagem} HTTP/1.1\r\nHost: {url_host}\r\nConnection: close\r\n\r\n"

    # criando conexão tcp, ipv4 com o servidor 
    sockt.connect((url_host, 80))

    # mandando requisição ao servidor com codificação utf-8
    sockt.sendall(url_request.encode())
    
    # Inicializa a variável para armazenar os dados recebidos
    retorno_bin = b""
    # Recebe os dados em pedaços de 4096 bytes e os adiciona à resposta
    while True:
        data = sockt.recv(buffer)
        if not data:
            break
        retorno_bin += data
   
    # Separando o Cabeçalho dos Dados da imagem
    delimiter_img = '\r\n\r\n'.encode()
    position  = retorno_bin.find(delimiter_img)
    image     = retorno_bin[position+4:] # DADOS DA REQUEST (imagem em bytes)
    headers   = retorno_bin[:position].decode('utf-8') # CABEÇALHO 
    
    # pegando a extensao do arquivo que vem no header, no seguinte formato 'tipo_arquivo/extensao' (por isso o split[1]), pegando a u  
    position_header = headers.find('Content-Type')
    tipo_extensao = headers[position_header:].split()[1] # pegando extensao e tipo do arquivo
    extensao_str = tipo_extensao.split('/')[-1]          # pegando só a extensao
    extensao = '.' + extensao_str
    print(f'EXTENSAO do header: \n{extensao}')

    # quebrando o nome do arquivo para manipulação
    sem_extensao = url_arq.split('.')
    # se não tiver extensão no nome do arquivo, insira e pegue o nome do arquivo sem extensão
    if len(sem_extensao) == 1:
        url_arq = url_arq + extensao
    
    url_arq_txt   = sem_extensao[0]

    #         PEGANDO OS BYTES E ESCREVENDO EM UM ARQUIVO PARA TRANSFORMAR EM IMAGEM
    try:
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')
    except:
        # se erro, troque os caracteres especiais no nome do arquivo por '-' e adicione a extensão, mesmo que já tenha (por precaução)
        delim = url_arq.find(sem_extensao[-1])
        url_arq = url_arq[:delim]
        # laço que percorre a lista com os caracteres inválidos, trocando-os por '-'
        for char_troca in invalidos:
            url_arq = url_arq.replace(char_troca,'-')
        # adicionando a extensão no arquivo
        url_arq = url_arq + extensao
        # criando o arquivo 
        file_output = open(f'{dir_atual}\{url_arq}', 'wb')

    file_output.write(image)
    file_output.close()
    print('Imagem salva com sucesso!')

    #         PEGANDO HEADER DA URL E JOGANDO PARA UM ARQUIVO TXT
    try:
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')
    except:
        # laço que percorre a lista com os caracteres inválidos, trocando-os por '-'
        for char_troca in invalidos:
            url_arq_txt = url_arq_txt.replace(char_troca,'-')
        # criando o arquivo 
        file_header = open(f'{dir_atual}\{url_arq_txt}.txt', 'w')

    file_header.write(headers)
    file_header.close()
    print('Arquivo texto criado com sucesso!')


if protocolo == 'http':
    conection_http(url_imagem,url_arq,url_host,sockt)
elif protocolo == 'https':
    conection_https(url_imagem,url_arq,url_host,sockt)