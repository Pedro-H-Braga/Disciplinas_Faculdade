-- --------------------------------------------------------------------------------
-- Definindo restrição de DATA_NASCIMENTO na tabela CLIENTES
alter table clientes
	add constraint ck_clientes_data_nascimento
	check (data_nascimento <= current_date);


-- --------------------------------------------------------------------------------
-- Definindo restrição de DIAS_ENTRE_DOSES na tabela FABRICANTES_VACINAS
alter table fabricantes_vacinas 
	add constraint ck_fabricantes_vacinas_dias_entre_doses
	check (dias_entre_doses >= 0);
	

-- --------------------------------------------------------------------------------
-- Definindo restrição de DATA_VACINACAO na tabela CONTROLE_VACINACAO
alter table controle_vacinacao 
	add constraint ck_controle_vacinacao_data_vacinacao
	check (data_vacinacao <= current_date);
	

-- --------------------------------------------------------------------------------
-- Definindo restrição de DOSAGEM na tabela FABRICANTES_VACINAS
alter table fabricantes_vacinas 
	add constraint ck_fabricantes_vacinas_dosagem
	check (dosagem >= 0);