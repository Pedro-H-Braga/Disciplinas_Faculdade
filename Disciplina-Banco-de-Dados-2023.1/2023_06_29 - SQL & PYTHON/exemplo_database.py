import sys, platform

from lib_exemplo import *
from lib_database import *

from constantes import *
from conexao_db import *

# ------------------------------------------------------------
# Limpando a tela
if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')


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
# Obtendo a estrutura do DataBase
print('\nObtendo a estrutura do DataBase...')
retorno = estruturaDB(connDB)

if not retorno[0]:
    print(retorno[1])
    sys.exit()

for k, v in retorno[1].items():
    print(f'{k}: {v}\n')


# ------------------------------------------------------------
# Fechando a conexão com o Database Server
connDB.close()