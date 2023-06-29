# pip install psycopg2 --user
import psycopg2, sys

# ------------------------------------------------------------
def conectaDB(server: str, database: str, dbuser: str, userpwd: str):
    conectado = False
    conexao   = None
    try:
        conexao = psycopg2.connect(f'dbname={database} user={dbuser} host={server} password={userpwd}')
    except:
        conexao = f'ERRO: {sys.exc_info()[0]}'
    else:
        conectado = True
    finally:
        return conectado, conexao

# ------------------------------------------------------------
def insereCampus(descricao: str, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = f'INSERT INTO alunos.campi (campus) VALUES (\'{descricao}\') '
    strSQL    += 'RETURNING campus;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT campus FROM alunos.campi '
        strSQL    += f'WHERE campus = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CAMPI): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
        
# ------------------------------------------------------------
def insereCotasMEC(descricao: str, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = f'INSERT INTO alunos.cotas_mec (cota_mec) VALUES (\'{descricao}\') '
    strSQL    += 'RETURNING id_cota_mec;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_cota_mec FROM alunos.cotas_mec '
        strSQL    += f'WHERE cota_mec = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela COTAS_MEC): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
        
# ------------------------------------------------------------
def insereCotasSISTEC(descricao: str, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = f'INSERT INTO alunos.cotas_sistec (cota_sistec) VALUES '
    strSQL    += f'(\'{descricao}\') RETURNING id_cota_sistec;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_cota_sistec FROM alunos.cotas_sistec '
        strSQL    += f'WHERE cota_sistec = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela COTAS_SISTEC): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

# ------------------------------------------------------------
def insereCursos(descricao: str, conexao):
    inserido    = False
    idRetorno   = None
    strSQL      = f'INSERT INTO alunos.cursos (curso) VALUES (\'{descricao}\') '
    strSQL     += 'RETURNING id_curso;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_curso FROM alunos.cursos '
        strSQL    += f'WHERE curso = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CURSOS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

# ------------------------------------------------------------
def insereLinhasPesquisa(descricao: str, conexao):
    inserido  = False
    idRetorno = None
    strSQL    = f'INSERT INTO alunos.linhas_pesquisa (linha_pesquisa) VALUES '
    strSQL   += f'(\'{descricao}\') RETURNING id_linha_pesquisa;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_linha_pesquisa FROM alunos.linhas_pesquisa '
        strSQL    += f'WHERE linha_pesquisa = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela LINHAS_PESQUISA): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

# ------------------------------------------------------------
def insereSituacoes(descricao: str, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = f'INSERT INTO alunos.situacoes (situacao) VALUES '
    strSQL    += f'(\'{descricao}\') RETURNING id_situacao;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_situacao FROM alunos.situacoes '
        strSQL    += f'WHERE situacao = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SITUACOES): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

# ------------------------------------------------------------
def insereSituacoesSistemicas(descricao: str, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = f'INSERT INTO alunos.situacoes_sistemicas (situacao_sistemica) '
    strSQL    += f'VALUES (\'{descricao}\') RETURNING id_situacao_sistemica;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.errors.UniqueViolation:
        conexao.rollback()
        strSQL     = f'SELECT id_situacao_sistemica FROM alunos.situacoes_sistemicas '
        strSQL    += f'WHERE situacao_sistemica = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
    except: 
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SITUACOES_SISTEMICAS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno

# ------------------------------------------------------------
def insereAlunos(campos: tuple, valores: tuple, conexao):
    inserido   = False
    idRetorno  = None
    strSQL     = 'INSERT INTO alunos.alunos ('
    for c in campos: strSQL += c + ', '
    strSQL     = strSQL[:-2]
    strSQL    += f') VALUES {valores} RETURNING matricula;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n{valores}\n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno