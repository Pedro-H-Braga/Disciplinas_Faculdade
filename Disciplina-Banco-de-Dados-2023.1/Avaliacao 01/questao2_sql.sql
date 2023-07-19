CREATE TABLE componentes_curriculares(
    turma VARCHAR(16) NOT NULL,
    periodo_letivo CHAR(6) NOT NULL,
    periodo_matriz bigserial NOT NULL PRIMARY KEY,
    codigo CHAR(8) NOT NULL,
    descricao VARCHAR(100) NOT NULL,
    carga_horaria SMALLINT NOT NULL,
    nota SMALLINT NOT NULL,
    frequencia VARCHAR(4) NOT NULL,
    situacao VARCHAR(100) NOT NULL
);