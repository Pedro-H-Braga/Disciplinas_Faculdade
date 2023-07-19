CREATE TABLE "setor"(
    "nome_setor" VARCHAR(n) NOT NULL,
    "id_setor" SERIAL NOT NULL
);
ALTER TABLE
    "setor" ADD PRIMARY KEY("id_setor");
CREATE TABLE "campus"(
    "campi" VARCHAR(10) NOT NULL,
    "id_campus" SERIAL NOT NULL
);
ALTER TABLE
    "campus" ADD PRIMARY KEY("id_campus");
CREATE TABLE "funcao"(
    "funcao_servidor" VARCHAR(n) NULL,
    "id_funcao" SERIAL NOT NULL
);
ALTER TABLE
    "funcao" ADD PRIMARY KEY("id_funcao");
CREATE TABLE "disciplina_ingresso"(
    "disciplina" VARCHAR(n) NULL,
    "id_disciplina" SERIAL NOT NULL
);
ALTER TABLE
    "disciplina_ingresso" ADD PRIMARY KEY("id_disciplina");
CREATE TABLE "jornada_trabalho"(
    "jornadaTrabalho" VARCHAR(n) NOT NULL,
    "id_jornada" SERIAL NOT NULL
);
ALTER TABLE
    "jornada_trabalho" ADD PRIMARY KEY("id_jornada");
CREATE TABLE "telefones_institucionais"(
    "telefone" CHAR(11) NULL,
    "ramal" CHAR(n) NOT NULL,
    "id_telefones" SERIAL NOT NULL
);
ALTER TABLE
    "telefones_institucionais" ADD PRIMARY KEY("id_telefones");
CREATE TABLE "servidor"(
    "matricula" INTEGER NOT NULL,
    "categoria" VARCHAR(n) NOT NULL,
    "cargo" VARCHAR(n) NULL,
    "nome" VARCHAR(n) NOT NULL,
    "curriculoLattes" VARCHAR(n) NULL,
    "urlFoto75x100" VARCHAR(n) NOT NULL,
    "id_setor" SERIAL NULL,
    "id_disciplina" SERIAL NULL,
    "id_funcao" SERIAL NULL,
    "id_jornada" SERIAL NULL,
    "id_telefones" SERIAL NULL,
    "id_campus" SERIAL NULL
);
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_nome_curriculolattes_urlfoto75x100_unique" UNIQUE(
        "nome",
        "curriculoLattes",
        "urlFoto75x100"
    );
ALTER TABLE
    "servidor" ADD PRIMARY KEY("matricula");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_telefones_foreign" FOREIGN KEY("id_telefones") REFERENCES "telefones_institucionais"("id_telefones");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_setor_foreign" FOREIGN KEY("id_setor") REFERENCES "setor"("id_setor");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_disciplina_foreign" FOREIGN KEY("id_disciplina") REFERENCES "disciplina_ingresso"("id_disciplina");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_campus_foreign" FOREIGN KEY("id_campus") REFERENCES "campus"("id_campus");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_jornada_foreign" FOREIGN KEY("id_jornada") REFERENCES "jornada_trabalho"("id_jornada");
ALTER TABLE
    "servidor" ADD CONSTRAINT "servidor_id_funcao_foreign" FOREIGN KEY("id_funcao") REFERENCES "funcao"("id_funcao");