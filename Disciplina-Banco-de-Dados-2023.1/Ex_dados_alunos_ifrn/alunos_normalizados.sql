-- criando tabela de linha de pesquisas
CREATE TABLE linha_pesquisas(
    id_linha_pesquisas SERIAL NOT NULL,
    linha_pesquisa VARCHAR(255) NULL,
	-- criando a PK 
	constraint pk_linha_pesquisas primary key (id_linha_pesquisas)
);

-- criando tabela de cotas do mec
CREATE TABLE cotas_mec(
    id_cotas_mec SERIAL NOT NULL,
    cota_mec VARCHAR(255) NULL,
	-- criando a PK 
	constraint pk_cotas_mec primary key (id_cotas_mec)
);
	
-- criando tabela de cursos
CREATE TABLE cursos(
    id_cursos SERIAL NOT NULL,
    curso VARCHAR(255) NOT NULL,
	-- criando a PK 
	constraint pk_cursos primary key (id_cursos)
);

-- criando tabela dos campi
CREATE TABLE campi(
    campus VARCHAR(4) NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
	-- criando a PK 
	constraint pk_campi primary key (campus)
);

-- criando tabela de situacoes sistemicas 
CREATE TABLE situacoes_sistemicas(
    id_situacoes_sistemicas SERIAL NOT NULL,
    situacao_sistemica VARCHAR(80) NOT NULL,
	-- criando a PK 
	constraint pk_situacoes_sistemicas primary key (id_situacoes_sistemicas)
);

-- criando tabela de situacoes
CREATE TABLE situacoes(
    id_situacoes SERIAL NOT NULL,
    situacoes VARCHAR(50) NOT NULL,
	-- criando a PK 
	constraint pk_situacoes primary key (id_situacoes)
);

-- criando tabela de cotas_sistec
CREATE TABLE cotas_sistec(
    id_cotas_sistec SERIAL NOT NULL,
    cota_sistec VARCHAR(50) NULL,
	-- criando a PK 
	constraint pk_cotas_sistec primary key (id_cotas_sistec)
);
	
-- criando a tabela central, alunos
CREATE TABLE alunos(
    matricula VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    curriculo_lattes VARCHAR(255) NULL,
    matricula_regular BOOLEAN NOT NULL,
    id_situacoes SERIAL NOT NULL,
    id_situacoes_sistemicas SERIAL NOT NULL,
    id_linha_pesquisas SERIAL NOT NULL,
    id_cota_sistec SERIAL NOT NULL,
    id_cotas_mec SERIAL NOT NULL,
    id_cursos SERIAL NOT NULL,
    campus VARCHAR(4) NOT NULL,
	-- criando a PK 
	constraint pk_alunos primary key (matricula),	

	-- criando as referencias de alunos
	
	-- referencia situacoes
    constraint fk_situacoes foreign key (id_situacoes)
    	references situacoes (id_situacoes),
	-- referencia situacao_sistemica
    constraint fk_situacoes_sistemicas foreign key (id_situacoes_sistemicas)
    	references situacoes_sistemicas (id_situacoes_sistemicas),
	-- referencia linha_pesquisa
    constraint fk_linha_pesquisas foreign key (id_linha_pesquisas) 
    	references linha_pesquisas (id_linha_pesquisas),
	-- referencia cota_mec
    constraint fk_cotas_mec foreign key (id_cotas_mec) 
    	references cotas_mec (id_cotas_mec),
	-- referencia curso
    constraint fk_cursos foreign key (id_cursos) 
    	references cursos (id_cursos),
	-- referencia campus
    constraint fk_campi foreign key (campus) 
    	references campi (campus)	
);