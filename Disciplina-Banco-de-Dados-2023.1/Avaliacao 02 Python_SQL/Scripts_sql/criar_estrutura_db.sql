-- ------------------------------
-- criando tabela SETOR
CREATE TABLE setor(
    nome_setor VARCHAR(150) NOT NULL,
    id_setor SERIAL NOT NULL,
    CONSTRAINT pk_setor PRIMARY KEY(id_setor)
);

-- ------------------------------
-- criando tabela FUNCAO
CREATE TABLE funcao(
    funcao_servidor VARCHAR(100) NULL,
    id_funcao SERIAL NOT NULL,
	CONSTRAINT pk_funcao PRIMARY KEY(id_funcao)
);

-- ------------------------------
-- criando tabela DISCIPLINAS
CREATE TABLE disciplina_ingresso(
    disciplina VARCHAR(150) NULL,
    id_disciplina SERIAL NOT NULL,
	CONSTRAINT pk_disciplina_ingresso PRIMARY KEY(id_disciplina)
);

-- ------------------------------
-- criando tabela JORNADA
CREATE TABLE jornada_trabalho(
    jornadaTrabalho VARCHAR(100) NOT NULL,
    id_jornada SERIAL NOT NULL,
	CONSTRAINT pk_jornada_trabalho PRIMARY KEY(id_jornada)
);

-- ------------------------------
-- criando tabela TELEFONES
CREATE TABLE telefones_institucionais(
    telefone CHAR(11) NULL,
    ramal CHAR(4) NOT NULL,
    id_telefones SERIAL NOT NULL,
    CONSTRAINT pk_telefones_institucionais PRIMARY KEY(id_telefones)
);

-- ------------------------------
-- Criando a tabela CAMPI
create table campus(
	campi			varchar(10),
	nome_completo	varchar(50),
	constraint pk_campi primary key (campi)
);

-- ------------------------------
-- criando tabela principal de SERVIDORES
CREATE TABLE servidor(
    matricula INTEGER NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    cargo VARCHAR(150) NULL,
    nome VARCHAR(255) NOT NULL,
    curriculoLattes VARCHAR(200) NULL,
    urlFoto75x100 VARCHAR(100) NOT NULL,
    id_setor SERIAL,
    id_disciplina SERIAL,
    id_funcao SERIAL,
    id_jornada SERIAL,
    id_telefones SERIAL,
    campi varchar(10),
	
	CONSTRAINT pk_servidor PRIMARY KEY(matricula),
	------------------------------------------------------------------
	-- importando as FK das tabelas externas
	CONSTRAINT fk_servidor_id_telefones_foreign FOREIGN KEY(id_telefones) 
				REFERENCES telefones_institucionais(id_telefones),
	
	CONSTRAINT fk_servidor_id_setor_foreign FOREIGN KEY(id_setor) 
				REFERENCES setor(id_setor),
	
	CONSTRAINT fk_servidor_id_disciplina_foreign FOREIGN KEY(id_disciplina) 
				REFERENCES disciplina_ingresso(id_disciplina),
	
	CONSTRAINT fk_servidor_id_campus_foreign FOREIGN KEY(campi) 
				REFERENCES campus(campi),
	
	CONSTRAINT fk_servidor_id_jornada_foreign FOREIGN KEY(id_jornada) 
				REFERENCES jornada_trabalho(id_jornada),
	
	CONSTRAINT fk_servidor_id_funcao_foreign FOREIGN KEY(id_funcao) 
				REFERENCES funcao(id_funcao)
);