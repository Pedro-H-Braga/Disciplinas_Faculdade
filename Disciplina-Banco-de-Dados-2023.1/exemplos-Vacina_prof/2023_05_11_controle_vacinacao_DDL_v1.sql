-- --------------------------------------------------------------------------------
-- Criando a tabela CONTROLE_VACINACAO
create table controle_vacinacao (
    id_controle_vacinacao SERIAL   not null,
    cpf 				  CHAR(11) not null,
    data_vacinacao 		  DATE     not null,
    lote 				  BIGINT   not null,
    id_fabricante_vacina  BIGINT   not null,
    constraint pk_controle_vacinacao primary key (id_controle_vacinacao)
);


-- --------------------------------------------------------------------------------
-- Criando a tabela CEPS
CREATE TABLE ceps(
    cep 		CHAR(9) 	 not null,
    logradouro 	VARCHAR(100) not null,
    bairro 		VARCHAR(50)  not null,
    cidade 		VARCHAR(50)  not null,
    estado 		CHAR(2) 	 not null,
    constraint pk_ceps primary key (cep)
);

   
-- --------------------------------------------------------------------------------
-- Criando a tabela FABRICANTES
CREATE TABLE fabricantes(
    cnpj_fabricante CHAR(14)     not null,
    nome_fabricante VARCHAR(100) not null,
    constraint pk_fabricantes primary key (cnpj_fabricante)
);


-- --------------------------------------------------------------------------------
-- Criando a tabela CLIENTES
CREATE TABLE clientes(
    cpf 			CHAR(11) 	 not null,
    nome 			VARCHAR(100) not null,
    telefone 		VARCHAR(13)  not null,
    e_mail 			VARCHAR(150) not null,
    data_nascimento DATE 		 not null,
    complemento 	VARCHAR(100) not null,
    numero 			VARCHAR(10)  not null,
    cep 			CHAR(9) 	 not null,
    constraint pk_clientes primary key (cpf)    
);


-- --------------------------------------------------------------------------------
-- Criando a tabela FABRICANTES_VACINAS
CREATE TABLE fabricantes_vacinas(
    id_fabricante_vacina SERIAL    not null,
    cnpj_fabricante 	 CHAR(14)  not null,
    id_tipo_vacina 		 INTEGER   not null,
    dosagem 			 SMALLINT  not null,
    dias_entre_doses 	 SMALLINT  not null,
    constraint pk_fabricantes_vacinas primary key (id_fabricante_vacina)
);

   
-- --------------------------------------------------------------------------------
-- Criando a tabela TIPOS_VACINA
CREATE TABLE tipos_vacina(
    id_tipo_vacina SERIAL       not null,
    tipo_vacina    VARCHAR(100) not null,
    constraint pk_tipos_vacina primary key (id_tipo_vacina)
);

   
-- --------------------------------------------------------------------------------
-- Criando a chave estrangeira entre as tabelas CONTROLE_VACINACAO - FABRICANTES_VACINAS
alter table controle_vacinacao 
	add constraint fk_controle_vacinacao_id_fabricante 
    foreign key (id_fabricante_vacina) references fabricantes_vacinas (id_fabricante_vacina);

   
-- --------------------------------------------------------------------------------
-- Criando a chave estrangeira entre as tabelas CLIENTES - CEPS
alter table clientes 
	add constraint fk_clientes_cep 
    foreign key (cep) references ceps (cep);

   
-- --------------------------------------------------------------------------------
-- Criando a chave estrangeira entre as tabelas FABRICANTES_VACINAS - FABRICANTES
alter table fabricantes_vacinas 
	add constraint fk_fabricantes_vacinas_id_tipo 
	foreign key (id_tipo_vacina) references tipos_vacina (id_tipo_vacina);
   

-- --------------------------------------------------------------------------------
-- Criando a chave estrangeira entre as tabelas CONTROLE_VACINACAO - CLIENTES
alter table controle_vacinacao 
	add constraint fk_controle_vacinacao_cpf 
	foreign key (cpf) references clientes (cpf);


-- --------------------------------------------------------------------------------
-- Criando a chave estrangeira entre as tabelas FABRICANTES_VACINAS - TIPOS_VACINA
alter table fabricantes_vacinas 
	add constraint fk_fabricantes_vacinas
	foreign key (cnpj_fabricante) references fabricantes (cnpj_fabricante);
	
