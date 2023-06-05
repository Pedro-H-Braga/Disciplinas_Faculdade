CREATE TABLE questao(
	-- id's para conexões com a tabela
    id SMALLINT NOT NULL, 
    id_tipo_questao SMALLINT NOT NULL,
    id_resposta SMALLINT NOT NULL,
    id_assunto SMALLINT NOT NULL,
    id_origem SMALLINT NOT NULL,
    enunciado TEXT NOT NULL,
    grau_diff CHAR(1) NOT NULL
);
ALTER TABLE
    questao ADD PRIMARY KEY(id);
CREATE TABLE origem_questao(
    id SMALLINT NOT NULL,
    autoria CHAR(1) NOT NULL, -- P (Professor), C (curso), L (livro)
    nome_curso VARCHAR(100) NOT NULL,
    nome_autor VARCHAR(100) NOT NULL,
    nome_livro VARCHAR(100) NOT NULL,
    ano_concurso INTEGER NOT NULL,
    banca_concurso VARCHAR(100) NOT NULL,
    orgao_concurso VARCHAR(100) NOT NULL
);
ALTER TABLE
    origem_questao ADD PRIMARY KEY(id);
CREATE TABLE respostas(
    id SMALLINT NOT NULL,
    id_questao SMALLINT NOT NULL, -- pega id da questao para saber a referencia da resposta
    resposta_subjetiva TEXT NOT NULL,
    resposta_objetiva BOOLEAN NOT NULL
);
ALTER TABLE
    respostas ADD PRIMARY KEY(id);
CREATE TABLE assunto(
    id SMALLINT NOT NULL,
    area_questao_id SMALLINT NOT NULL, -- pega a area para saber o assunto
    assunto_questao VARCHAR(100) NOT NULL
);
ALTER TABLE
    assunto ADD PRIMARY KEY(id);
CREATE TABLE tipo_questao(
    id SMALLINT NOT NULL,
    subjetiva TEXT NULL,
    objetiva BOOLEAN NULL
);
ALTER TABLE
    tipo_questao ADD PRIMARY KEY(id);
ALTER TABLE
    questao ADD CONSTRAINT questao_id_resposta_foreign FOREIGN KEY(id_resposta) REFERENCES respostas(id); -- questão se relacionando com resposta
ALTER TABLE
    questao ADD CONSTRAINT questao_id_origem_foreign FOREIGN KEY(id_origem) REFERENCES origem_questao(id); -- origem da questão se relacionando com a questão
ALTER TABLE
    questao ADD CONSTRAINT questao_id_assunto_foreign FOREIGN KEY(id_assunto) REFERENCES assunto(id); -- assunto se relacionando com a questão
ALTER TABLE
    questao ADD CONSTRAINT questao_id_tipo_questao_foreign FOREIGN KEY(id_tipo_questao) REFERENCES tipo_questao(id); -- tipo da questão se relacionando com a questão