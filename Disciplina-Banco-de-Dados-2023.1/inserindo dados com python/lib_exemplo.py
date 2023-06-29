import sys
from constantes import *
from lib_exemplo import *


# ------------------------------------------------------------
# transformando o caminho do arquivo em string
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
            # fazendo a variavel linha receber a ultima linha do arquivo
            linha = arq_.readline()[:-1]
            if not linha: break # se nada pare
            cabecalho = linha.split(SEPARATOR) # separando a ultima linha em uma lista pelo separador ;
            while True:
                linha = arq_.readline()[:-1]
                if not linha: break
                linha = linha.split(SEPARATOR)
                # a cada ultimo valor de cada linha que tem 7 valores
                dados_retorno[linha[7]] = dict(zip(cabecalho, linha)) # para cada valor, junte o cabeçalho com a linha
            lido = True
        arq_.close()
    finally:
        return lido, dados_retorno