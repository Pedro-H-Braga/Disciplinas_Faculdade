import sys

from lib_exemplo import *
from lib_database import *

from constantes import *
from conexao_db import *

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

# Gerando SETS com os dados a serem inseridos nas tabelas 
# exceto na tabela ALUNOS
setCampi               = set(map(lambda c: c['campus'], dados_lidos.values()))
setCotasMEC            = set(map(lambda c: c['cota_mec'], dados_lidos.values()))
setCotasSISTEC         = set(map(lambda c: c['cota_sistec'], dados_lidos.values()))
setCursos              = set(map(lambda c: c['curso'], dados_lidos.values()))
setLinhasPesquisa      = set(map(lambda c: c['linha_pesquisa'], dados_lidos.values()))
setSituacoes           = set(map(lambda c: c['situacao'], dados_lidos.values()))
setSituacoesSistemicas = set(map(lambda c: c['situacao_sistemica'], dados_lidos.values()))

# ------------------------------------------------------------
# Estabelecendo conexão com Database Server
retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

# ------------------------------------------------------------
# Caso dê algum erro na conexão sai do programa
if not retConexao[0]:
    print(retConexao[1])
    sys.exit()

# Guarda o objeto da conexão 
connDB = retConexao[1]

# ------------------------------------------------------------
# Inserindo os CAMPI
print('\nInserindo os dados na tabela CAMPI...')
dictCampus = dict()
for campus in setCampi:
    if not campus: continue
    retorno = insereCampus(campus, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCampus[campus] = retorno[1]
print(dictCampus) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os COTAS_MEC
print('\nInserindo os dados na tabela COTAS_MEC...')
dictCotasMEC = dict()
for cotaMEC in setCotasMEC:
    if not cotaMEC: continue
    retorno = insereCotasMEC(cotaMEC, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCotasMEC[cotaMEC] = retorno[1]
print(dictCotasMEC) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os COTAS_SISTEC
print('\nInserindo os dados na tabela COTAS_SISTEC...')
dictCotasSISTEC = dict()
for cotaSISTEC in setCotasSISTEC:
    if not cotaSISTEC: continue
    retorno = insereCotasSISTEC(cotaSISTEC, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCotasSISTEC[cotaSISTEC] = retorno[1]
print(dictCotasSISTEC) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os CURSOS
print('\nInserindo os dados na tabela CURSOS...')
dictCursos = dict()
for curso in setCursos:
    if not curso: continue
    retorno = insereCursos(curso, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCursos[curso] = retorno[1]
print(dictCursos) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os LINHAS_PESQUISA
print('\nInserindo os dados na tabela LINHAS_PESQUISA...')
dictLinhasPesquisa = dict()
for linhaPesquisa in setLinhasPesquisa:
    if not linhaPesquisa: continue
    retorno = insereLinhasPesquisa(linhaPesquisa, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictLinhasPesquisa[linhaPesquisa] = retorno[1]
print(dictLinhasPesquisa) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os SITUACOES
print('\nInserindo os dados na tabela SITUACOES...')
dictSituacoes = dict()
for situacao in setSituacoes:
    if not situacao: continue
    retorno = insereSituacoes(situacao, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSituacoes[situacao] = retorno[1]
print(dictSituacoes) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Inserindo os SITUACOES_SISTEMICAS
print('\nInserindo os dados na tabela SITUACOES_SISTEMICAS...')
dictSituacoesSistemicas = dict()
for situacaoSistemica in setSituacoesSistemicas:
    if not situacaoSistemica: continue
    retorno = insereSituacoesSistemicas(situacaoSistemica, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSituacoesSistemicas[situacaoSistemica] = retorno[1]
print(dictSituacoesSistemicas) # TODO: PODE APAGAR DEPOIS

# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()