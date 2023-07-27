-- ---------------------------------------------------------------
-- Transformando tabelas que foram inseridos os dados como unique para a não repetição dos dados

alter table  campus 
	add constraint un_campi unique (campi);
