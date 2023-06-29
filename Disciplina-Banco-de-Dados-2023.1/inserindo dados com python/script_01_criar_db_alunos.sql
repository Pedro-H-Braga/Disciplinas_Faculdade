-- ----------------------------------------------------------------------
-- Criando o banco IFRN
create database ifrn;

-- ----------------------------------------------------------------------
-- Criando o Schema ALUNOS
create schema alunos;


-- ----------------------------------------------------------------------
-- Criando a tabela CURSOS
create table alunos.cursos (
	id_curso 	serial,
	curso 		varchar(200),
	constraint pk_cursos primary key (id_curso)
);


-- ----------------------------------------------------------------------
-- Criando a tabela SITUACOES
create table alunos.situacoes (
	id_situacao serial,
	situacao	varchar(50),
	constraint pk_situacoes primary key (id_situacao)
);


-- ----------------------------------------------------------------------
-- Criando a tabela SITUACOES_SISTEMICAS
create table alunos.situacoes_sistemicas (
	id_situacao_sistemica	serial,
	situacao_sistemica		varchar(50),
	constraint pk_situacoes_sistemicas primary key (id_situacao_sistemica)
);


-- ----------------------------------------------------------------------
-- Criando a tabela LINHAS_PESQUISA
create table alunos.linhas_pesquisa (
	id_linha_pesquisa	serial,
	linha_pesquisa		varchar(100),
	constraint pk_linhas_pesquisa primary key (id_linha_pesquisa)
);


-- ----------------------------------------------------------------------
-- Criando a tabela COTAS_MEC
create table alunos.cotas_mec (
	id_cota_mec	serial,
	cota_mec	varchar(50),
	constraint pk_cotas_mec primary key (id_cota_mec)
);


-- ----------------------------------------------------------------------
-- Criando a tabela COTAS_SISTEC
create table alunos.cotas_sistec (
	id_cota_sistec	serial,
	cota_sistec		varchar(50),
	constraint pk_cotas_sistec primary key (id_cota_sistec)
);


-- ----------------------------------------------------------------------
-- Criando a tabela CAMPI
create table alunos.campi (
	campus			varchar(10),
	nome_completo	varchar(50),
	constraint pk_campi primary key (campus)
);


-- ----------------------------------------------------------------------
-- Criando a tabela ALUNOS
create table alunos.alunos (
	matricula				bigint,
	nome					varchar(100),
	curriculo_lattes		varchar(100),
	matricula_regular		boolean default TRUE,
	id_curso				integer,
	id_situacao				integer,
	id_situacao_sistemica	integer,
	id_linha_pesquisa		integer,
	id_cota_mec				integer,
	id_cota_sistec			integer,
	campus					varchar(10),
	
	constraint pk_alunos primary key (matricula),
	constraint fk_alunos_id_curso foreign key (id_curso) 						
				references alunos.cursos (id_curso),
	constraint fk_alunos_id_situacao foreign key (id_situacao)
				references alunos.situacoes (id_situacao),
	constraint fk_alunos_id_situacao_sistemica foreign key (id_situacao_sistemica)
				references alunos.situacoes_sistemicas (id_situacao_sistemica),
	constraint fk_alunos_id_linha_pesquisa foreign key (id_linha_pesquisa)
				references alunos.linhas_pesquisa (id_linha_pesquisa),
	constraint fk_alunos_id_cota_mec foreign key (id_cota_mec)
				references alunos.cotas_mec (id_cota_mec),
	constraint fk_alunos_id_cota_sistec foreign key (id_cota_sistec)
				references alunos.cotas_sistec (id_cota_sistec),
	constraint fk_alunos_campus foreign key (campus) 
				references alunos.campi (campus)	
);


