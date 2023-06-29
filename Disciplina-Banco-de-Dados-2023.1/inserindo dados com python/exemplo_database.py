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
print('\nTratando os Dados Lidos...')
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
# Inserindo os dados na tabela CAMPI
print('\nInserindo os dados na tabela CAMPI...')
dictCampi = dict()
for campus in setCampi:
    if not campus: campus = '-----'
    retorno = insereCampus(campus, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCampi[campus] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela COTAS_MEC
print('\nInserindo os dados na tabela COTAS_MEC...')
dictCotasMEC = dict()
for cotaMEC in setCotasMEC:
    if not cotaMEC: cotaMEC = '-----'

    retorno = insereCotasMEC(cotaMEC, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCotasMEC[cotaMEC] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela COTAS_SISTEC
print('\nInserindo os dados na tabela COTAS_SISTEC...')
dictCotasSISTEC = dict()
for cotaSISTEC in setCotasSISTEC:
    if not cotaSISTEC: cotaSISTEC = '-----'
    retorno = insereCotasSISTEC(cotaSISTEC, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCotasSISTEC[cotaSISTEC] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela CURSOS
print('\nInserindo os dados na tabela CURSOS...')
dictCursos = dict()
for curso in setCursos:
    if not curso: curso = '-----'
    retorno = insereCursos(curso, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictCursos[curso] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela LINHAS_PESQUISA
print('\nInserindo os dados na tabela LINHAS_PESQUISA...')
dictLinhasPesquisa = dict()
for linhaPesquisa in setLinhasPesquisa:
    if not linhaPesquisa: linhaPesquisa = '-----'
    retorno = insereLinhasPesquisa(linhaPesquisa, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictLinhasPesquisa[linhaPesquisa] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela SITUACOES
print('\nInserindo os dados na tabela SITUACOES...')
dictSituacoes = dict()
for situacao in setSituacoes:
    if not situacao: situacao = '-----'
    retorno = insereSituacoes(situacao, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSituacoes[situacao] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela SITUACOES_SISTEMICAS
print('\nInserindo os dados na tabela SITUACOES_SISTEMICAS...')
dictSituacoesSistemicas = dict()
for situacaoSistemica in setSituacoesSistemicas:
    if not situacaoSistemica: situacaoSistemica = '-----'
    retorno = insereSituacoesSistemicas(situacaoSistemica, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictSituacoesSistemicas[situacaoSistemica] = retorno[1]

# ------------------------------------------------------------
# Inserindo os dados na tabela ALUNOS
print('\nInserindo os dados na tabela ALUNOS...')
tupleCampos = tuple(['curriculo_lattes'    , 'id_cota_mec', 'matricula_regular', 
                     'id_situacao'          , 'nome'       , 'id_curso'         , 
                     'id_situacao_sistemica', 'matricula'  , 'id_linha_pesquisa', 
                     'id_cota_sistec'       , 'campus'])
for k,v in dados_lidos.items():
    if dados_lidos[k]['cota_mec']           == '': dados_lidos[k]['cota_mec']           = '-----'
    if dados_lidos[k]['cota_sistec']        == '': dados_lidos[k]['cota_sistec']        = '-----'
    if dados_lidos[k]['curso']              == '': dados_lidos[k]['curso']              = '-----'
    if dados_lidos[k]['linha_pesquisa']     == '': dados_lidos[k]['linha_pesquisa']     = '-----'
    if dados_lidos[k]['situacao']           == '': dados_lidos[k]['situacao']           = '-----'
    if dados_lidos[k]['situacao_sistemica'] == '': dados_lidos[k]['situacao_sistemica'] = '-----'

    dados_lidos[k]['cota_mec']           = dictCotasMEC[dados_lidos[k]['cota_mec']]
    dados_lidos[k]['situacao']           = dictSituacoes[dados_lidos[k]['situacao']]
    dados_lidos[k]['curso']              = dictCursos[dados_lidos[k]['curso']]
    dados_lidos[k]['situacao_sistemica'] = dictSituacoesSistemicas[dados_lidos[k]['situacao_sistemica']]
    dados_lidos[k]['matricula_regular']  = bool(dados_lidos[k]['matricula_regular'])
    dados_lidos[k]['linha_pesquisa']     = dictLinhasPesquisa[dados_lidos[k]['linha_pesquisa']]
    dados_lidos[k]['cota_sistec']        = dictCotasSISTEC[dados_lidos[k]['cota_sistec']]

    tupleValores = tuple(v.values())

    retorno = insereAlunos(tupleCampos, tupleValores, connDB)

    if not retorno[0]: print(retorno[1])

# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()