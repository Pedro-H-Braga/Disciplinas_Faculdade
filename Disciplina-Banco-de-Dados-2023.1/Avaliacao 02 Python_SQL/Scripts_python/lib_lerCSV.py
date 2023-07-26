import sys
from constantes import *

# ------------------------------------------------------------
def lerArquivo(nomeArquivo: str):
    lido = False
    dados_retorno = dict()
    try:
        arq_ = open(nomeArquivo, 'r', encoding=CODE_PAGE)
    except FileNotFoundError:
        dados_retorno = f'\nERRO: Arquivo Inexistente...'
    except:
        dados_retorno = f'\nERRO: {sys.exc_info()[0]}'
    else:
        while True:
            linha = arq_.readline()[:-1]
            if not linha: break
            cabecalho = linha.split(SEPARATOR)
            while True:
                linha = arq_.readline()[:-1]
                if not linha: break
                linha = linha.split(SEPARATOR)
                dados_retorno[linha[7]] = dict(zip(cabecalho, linha))
            lido = True
        arq_.close()
    finally:
        return lido, dados_retorno
    
# ------------------------------------------------------------
# Lendo arquivo de input
retLeitura = lerArquivo(APP_DIR + '\\alunos_ifrn.csv')

# ------------------------------------------------------------
# Caso dê algum erro na leitura sai do programa
if not retLeitura[0]:
    print(retLeitura[1])
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