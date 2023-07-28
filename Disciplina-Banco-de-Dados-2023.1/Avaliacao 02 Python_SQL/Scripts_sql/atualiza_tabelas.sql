-- ---------------------------------------------------------------
-- Transformando tabelas que foram inseridos os dados como unique para a não repetição dos dados

-- TABELA CAMPUS, campo campi
alter table  campus 
	add constraint un_campi unique (campi);

-- 					NÃO CONSEGUI INSERIR OS DADOS
-- TABELA SERVIDOR, campo categoria
-- alter table  campus 
--	add constraint un_campi unique (campi);
-- Tirando o NOT NULL do campo categoria da tabela campos
ALTER TABLE servidor ALTER COLUMN categoria DROP NOT NULL;

INSERT INTO servidor.categoria (categoria) VALUES ('T E S TANDO');