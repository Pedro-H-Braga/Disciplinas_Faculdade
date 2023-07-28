import sys

from lib_lerCSV import *
from lib_ConnBD import *

from constantes import *
from conexao_db import *

# ------------------------------------------------------------
# Lendo arquivo de input
retLeitura = lerArquivo(APP_DIR + '\\dados_servidores.csv')

# ------------------------------------------------------------
# Caso dê algum erro na leitura sai do programa
if not retLeitura[0]:
    print(retLeitura[1])
    sys.exit()

# ------------------------------------------------------------
# Tratando os dados lidos 
dados_lidos = retLeitura[1]

# Gerando SETS com os dados a serem inseridos nas tabelas 
# exceto na tabela servidores
setCategoria            = set(map(lambda c: c['categoria'], dados_lidos.values()))
setCargo                = set(map(lambda c: c['cargo'], dados_lidos.values()))
setSetorSiape           = set(map(lambda c: c['setor_siape'], dados_lidos.values()))
setDisciplinaIngresso   = set(map(lambda c: c['disciplina_ingresso'], dados_lidos.values()))
setSetorSuap            = set(map(lambda c: c['setor_suap'], dados_lidos.values()))
setNome                 = set(map(lambda c: c['nome'], dados_lidos.values()))
setFuncao               = set(map(lambda c: c['funcao'], dados_lidos.values()))
setJornadaTrabalho      = set(map(lambda c: c['jornada_trabalho'], dados_lidos.values()))
setTelefones            = set(map(lambda c: c['telefones_institucionais'], dados_lidos.values()))
setMatricula            = set(map(lambda c: c['matricula'], dados_lidos.values()))
setCurriculo            = set(map(lambda c: c['curriculo_lattes'], dados_lidos.values()))
setCampi                = set(map(lambda c: c['campus'], dados_lidos.values()))
setUrlFoto              = set(map(lambda c: c['url_foto_75x100'], dados_lidos.values()))

# exibindo o tamanho de cada variavel

print(f'TAMANHO de cada SET: \nsetCategoria: {(setCategoria)}\n\
setCargo: {len(setCargo)}\n\
setSetorSiape: {len(setSetorSiape)}\n\
setDisciplinaIngresso: {len(setDisciplinaIngresso)}\n\
setSetorSuap: {len(setSetorSuap)}\n\
setNome: {len(setNome)}\n\
setFuncao: {len(setFuncao)}\n\
setJornadaTrabalho: {len(setJornadaTrabalho)}\n\
setTelefones: {len(setTelefones)}\n\
setMatricula: {len(setMatricula)}\n\
setCurriculo: {len(setCurriculo)}\n\
setCampi: {len(setCampi)}\n\
setUrlFoto: {len(setUrlFoto)}')
# BUG quando tenta preencher uma tabela com dados

# ------------------------------------------------------------
# Estabelecendo conexão com Database Server
try:
    retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)
except Exception as error:
    print('Conexão com o banco falhou!')
else:
    print('Conexão com o banco bem sucessida!')
# ------------------------------------------------------------
# Caso dê algum erro na conexão sai do programa
if not retConexao[0]:
    print(retConexao[1])
    sys.exit()

# Guarda o objeto da conexão 
connDB = retConexao[1]

'''
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
 '''

# ------------------------------------------------------------
# Inserindo os Servidor
print('\nInserindo os dados na tabela Servidor...')
# Juntando os dados para desempacotar no for
zipServidor = zip(setMatricula, setCategoria, setCargo, setNome, setCurriculo, setUrlFoto) # Combine os conjuntos usando zip()

dictServidor = dict()
# desempacotando zipServidor para as variaveis
for matricula, categoria, cargo, nome, curriculoLattes, urlFoto75x100 in zipServidor:
    if not matricula: continue
    retorno = insereServidor(matricula, categoria, cargo, nome, curriculoLattes, urlFoto75x100, connDB)
    if not retorno[0]:
        print(retorno[1])
        continue
    dictServidor[matricula] = retorno[1]

cont = 0
for chave, valor in dictServidor.items():    
    print(f'{chave}: {valor}') # TODO: PODE APAGAR DEPOIS
    cont += 1
    if cont > 30: break

# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()

#                                             TESTAGENS
sys.exit()


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