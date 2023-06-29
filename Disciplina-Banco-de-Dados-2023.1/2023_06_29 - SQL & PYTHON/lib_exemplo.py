import sys
from constantes import *
from lib_exemplo import *


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