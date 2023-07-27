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
    strSQL     = f'INSERT INTO campi (campus) VALUES (\'{descricao}\') '
    strSQL    += 'RETURNING campus;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL     = f'INSERT INTO cotas_mec (cota_mec) VALUES (\'{descricao}\') '
    strSQL    += 'RETURNING id_cota_mec;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL     = f'INSERT INTO cotas_sistec (cota_sistec) VALUES '
    strSQL    += f'(\'{descricao}\') RETURNING id_cota_sistec;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL      = f'INSERT INTO cursos (curso) VALUES (\'{descricao}\') '
    strSQL     += 'RETURNING id_curso;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL    = f'INSERT INTO linhas_pesquisa (linha_pesquisa) VALUES '
    strSQL   += f'(\'{descricao}\') RETURNING id_linha_pesquisa;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL     = f'INSERT INTO situacoes (situacao) VALUES '
    strSQL    += f'(\'{descricao}\') RETURNING id_situacao;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
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
    strSQL     = f'INSERT INTO situacoes_sistemicas (situacao_sistemica) '
    strSQL    += f'VALUES (\'{descricao}\') RETURNING id_situacao_sistemica;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno