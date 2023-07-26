import sys
from constantes import *

# ------------------------------------------------------------
def lerArquivo(nomeArquivo: str):
    lido = False
    dados_retorno = dict()
    try:
        with open(nomeArquivo, 'r', encoding=CODE_PAGE) as arq_:
            print('abrindo o arquivo!')
            while True:
                linha = arq_.readline()[:-1]
                print(f'arq_.readline: {linha}')
                if not linha: break
                cabecalho = linha.split(SEPARATOR)
                while True:
                    linha = arq_.readline()[:-1]
                    if not linha: break
                    linha = linha.split(SEPARATOR)
                    # dados_retorno[linha[]] -> é para pegar a chave de cada cabeçalho (indicar a posição de onde o campo matrícula (9))
                    dados_retorno[linha[9]] = dict(zip(cabecalho, linha)) 
                lido = True

    except FileNotFoundError:
        dados_retorno = f'\nERRO: Arquivo Inexistente...'
        print(dados_retorno)
    except:
        dados_retorno = f'\nERRO: {sys.exc_info()[0]}'
        print(dados_retorno)
    finally:
        return lido, dados_retorno
    
'''
#                                        TESTANDO LEITURA
# ------------------------------------------------------------
# Lendo arquivo de input
retLeitura = lerArquivo(APP_DIR + '\\dados_extraidos_recursos_servidores_2.csv')

# ------------------------------------------------------------
# Caso dê algum erro na leitura sai do programa
if not retLeitura[0]:
    print(f'Deu error: {retLeitura[1]}')
    sys.exit()

# ------------------------------------------------------------
# Tratando os dados lidos 
dados_lidos = retLeitura[1]

# para exibir 30 primeiros dados de dados_lidos
cont = 0
for chave, valor in dados_lidos.items():
    print(f'{chave}: {valor}')
    cont += 1
    if cont > 30:
        break
'''