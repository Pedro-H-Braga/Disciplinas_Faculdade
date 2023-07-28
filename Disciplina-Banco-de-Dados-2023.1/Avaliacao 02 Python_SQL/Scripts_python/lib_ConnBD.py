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
    strSQL     = f'INSERT INTO campus (campi) VALUES (\'{descricao}\') '
    strSQL    += 'RETURNING campi;'
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
def insereDisciplina(descricao: str, conexao):
    inserido    = False
    idRetorno   = None
    strSQL      = f'INSERT INTO disciplina_ingresso (disciplina) VALUES (\'{descricao}\') '
    strSQL     += 'RETURNING id_disciplina;'
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
def insereFuncao(descricao: str, conexao):
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
    
# ------------------------------------------------------------
def insereServidor(matricula: int, categoria: str, cargo: str, nome: str, curriculoLattes: str, urlFoto75x100: str, conexao):
    inserido   = False
    idRetorno  = None
    
    if matricula is None or matricula == '': matricula = 0
    if categoria is None or categoria == '': categoria = 'Vazio'
    if cargo is None or cargo == '': cargo = 'Vazio'
    if nome is None or cargo == '': nome = 'Vazio'
    if curriculoLattes is None or curriculoLattes == '': curriculoLattes = 'Vazio'
    if urlFoto75x100 is None or urlFoto75x100 == '': urlFoto75x100 = 'Vazio'

    # utilizando placeholders da biblioteca psycopg2
    strSQL     = f"INSERT INTO servidor (matricula, categoria, cargo, nome, curriculolattes, urlfoto75x100) " \
    f"VALUES ({matricula}, '{categoria}', '{cargo}', '{nome}', '{curriculoLattes}', '{urlFoto75x100}') " \
    "RETURNING matricula;"
    print(strSQL)
    try:
        cursorTable = conexao.cursor()
        # descricao dentro da tupla cursorTable.execute, para rodar o placeholder
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{matricula} \n\n'
    else:
        inserido  = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
        