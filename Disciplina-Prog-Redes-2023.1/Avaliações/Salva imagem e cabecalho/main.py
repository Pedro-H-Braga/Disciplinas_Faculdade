# PADRÃO DOS DOIS EXEMPLOS (6 e 4)
import socket, sys
from functions import conection_http, conection_https

# input que pegue as urls e divida a url para cada variavel
url = input('Informe a URL da imagem: ')

# separando url 
list_split = url.split('/')

# Para verificar se é http ou https 
protocolo = list_split[0] 
protocolo = protocolo[:-1] # tirando os dois pontos do final do protocolo

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

    # Se http:
if protocolo == 'http':
        conection_http(url_imagem,url_arq,url_host,sockt)
    # Se HTTPS
if protocolo == 'https':
        conection_https(url_imagem,url_arq,url_host,sockt)
'''
try:
    # Se http:
    if protocolo == 'http':
        conection_http(url_imagem,url_arq,url_host,sockt)
    # Se HTTPS
    if protocolo == 'https':
        conection_https(url_imagem,url_arq,url_host,sockt)
except: 
    print(f'Error!...\n{sys.exc_info()[0]}')
    sys.exit()
'''