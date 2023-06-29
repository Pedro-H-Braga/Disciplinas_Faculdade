alter table alunos.cotas_mec 
	add constraint un_cota_mec unique (cota_mec);

alter table alunos.cotas_sistec 
	add constraint un_cota_sistec unique (cota_sistec);

alter table alunos.cursos 
	add constraint un_curso unique (curso);

alter table alunos.linhas_pesquisa 
	add constraint un_linha_pesquisa unique (linha_pesquisa);

alter table alunos.situacoes 
	add constraint un_situacao unique (situacao);

alter table alunos.situacoes_sistemicas 
	add constraint un_situacao_sistemica unique (situacao_sistemica);
