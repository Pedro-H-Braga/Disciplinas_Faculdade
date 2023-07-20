-- ---------------------------------------------------------------
-- Deixando as colunas das tabelas sem adições acidentais com o unique

alter table setor 
	add constraint un_setor unique (nome_setor);

alter table funcao 
	add constraint un_funcao unique (funcao_servidor);

alter table disciplina_ingresso 
	add constraint un_disciplina_ingresso unique (disciplina);

alter table jornada_trabalho 
	add constraint un_jornada_trabalho unique (jornadatrabalho);

alter table telefones_institucionais 
	drop constraint un_telefones_institucionais;
	
-- Nâo precisa colocar a unique de servidores, pois é uma primary key, sendo assim, já é 'unique'
