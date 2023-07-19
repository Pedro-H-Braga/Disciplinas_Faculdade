CREATE TABLE "controle_vacinacao"(
    "id_controle_vacinacao" SERIAL NOT NULL,
    "cpf" CHAR(255) NOT NULL,
    "data_vacinacao" BIGINT NOT NULL,
    "lote" BIGINT NOT NULL,
    "id_fabricante_vacina" BIGINT NOT NULL
);
ALTER TABLE
    "controle_vacinacao" ADD PRIMARY KEY("id_controle_vacinacao");
CREATE TABLE "ceps"(
    "cep" CHAR(255) NOT NULL,
    "logradouro" VARCHAR(255) NOT NULL,
    "bairro" VARCHAR(255) NOT NULL,
    "cidade" VARCHAR(255) NOT NULL,
    "estado" CHAR(255) NOT NULL
);
ALTER TABLE
    "ceps" ADD PRIMARY KEY("cep");
CREATE TABLE "fabricantes"(
    "cnpj_fabricante" CHAR(255) NOT NULL,
    "nome_fabricante" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "fabricantes" ADD PRIMARY KEY("cnpj_fabricante");
CREATE TABLE "clientes"(
    "cpf" CHAR(255) NOT NULL,
    "nome" VARCHAR(255) NOT NULL,
    "telefone" VARCHAR(255) NOT NULL,
    "e_mail" VARCHAR(255) NOT NULL,
    "data_nascimento" DATE NOT NULL,
    "complemento" VARCHAR(255) NOT NULL,
    "numero" VARCHAR(255) NOT NULL,
    "cep" CHAR(255) NOT NULL
);
ALTER TABLE
    "clientes" ADD PRIMARY KEY("cpf");
CREATE TABLE "fabricantes_vacinas"(
    "id_fabricante_vacina" SERIAL NOT NULL,
    "cnpj_fabricante" CHAR(255) NOT NULL,
    "id_tipo_vacina" BIGINT NOT NULL,
    "dosagem" INTEGER NOT NULL,
    "dias_entre_doses" INTEGER NOT NULL
);
ALTER TABLE
    "fabricantes_vacinas" ADD PRIMARY KEY("id_fabricante_vacina");
CREATE TABLE "tipos_vacina"(
    "id_tipo_vacina" SERIAL NOT NULL,
    "tipo_vacina" BIGINT NOT NULL
);
ALTER TABLE
    "tipos_vacina" ADD PRIMARY KEY("id_tipo_vacina");
ALTER TABLE
    "controle_vacinacao" ADD CONSTRAINT "controle_vacinacao_id_fabricante_vacina_foreign" FOREIGN KEY("id_fabricante_vacina") REFERENCES "fabricantes_vacinas"("id_fabricante_vacina");
ALTER TABLE
    "clientes" ADD CONSTRAINT "clientes_cep_foreign" FOREIGN KEY("cep") REFERENCES "ceps"("cep");
ALTER TABLE
    "fabricantes_vacinas" ADD CONSTRAINT "fabricantes_vacinas_id_tipo_vacina_foreign" FOREIGN KEY("id_tipo_vacina") REFERENCES "fabricantes"("cnpj_fabricante");
ALTER TABLE
    "controle_vacinacao" ADD CONSTRAINT "controle_vacinacao_cpf_foreign" FOREIGN KEY("cpf") REFERENCES "clientes"("cpf");
ALTER TABLE
    "fabricantes_vacinas" ADD CONSTRAINT "fabricantes_vacinas_id_tipo_vacina_foreign" FOREIGN KEY("id_tipo_vacina") REFERENCES "tipos_vacina"("id_tipo_vacina");