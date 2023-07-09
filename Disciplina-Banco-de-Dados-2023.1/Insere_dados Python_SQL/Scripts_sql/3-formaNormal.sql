CREATE TABLE campus 
( 
 campi VARCHAR(n) NOT NULL,  
 id_campus INT PRIMARY KEY DEFAULT 'serial',  
); 

CREATE TABLE telefones_institucionais 
( 
 telefone CHAR(n),  
 ramal CHAR(n) NOT NULL,  
 id_telefones INT PRIMARY KEY,  
 CHECK (ramal = 'undefined')
); 

CREATE TABLE funcao 
( 
 funcao_servidor VARCHAR(n),  
 id_funcao INT PRIMARY KEY,  
); 

CREATE TABLE disciplina_ingresso 
( 
 disciplina VARCHAR(n),  
 id_disciplina INT PRIMARY KEY,  
); 

CREATE TABLE setor 
( 
 nome_setor VARCHAR(n) NOT NULL,  
 id_setor INT PRIMARY KEY,  
); 

CREATE TABLE jornada_trabalho 
( 
 jornadaTrabalho VARCHAR(n) NOT NULL,  
 id_jornada INT PRIMARY KEY,  
); 

CREATE TABLE servidor 
( 
 matricula INT PRIMARY KEY,  
 categoria VARCHAR(n) NOT NULL,  
 cargo VARCHAR(n),  
 nome VARCHAR(n) NOT NULL,  
 curriculoLattes VARCHAR(n),  
 urlFoto75x100 VARCHAR(n) NOT NULL,  
 id_setor INT,  
 id_disciplina INT,  
 id_funcao INT,  
 id_jornada INT,  
 id_telefones INT,  
 id_campus INT,  
 UNIQUE (nome,curriculoLattes,urlFoto75x100)
); 

ALTER TABLE servidor ADD FOREIGN KEY(id_setor) REFERENCES setor (id_setor)
ALTER TABLE servidor ADD FOREIGN KEY(id_disciplina) REFERENCES disciplina_ingresso (id_disciplina)
ALTER TABLE servidor ADD FOREIGN KEY(id_funcao) REFERENCES funcao (id_funcao)
ALTER TABLE servidor ADD FOREIGN KEY(id_jornada) REFERENCES jornada_trabalho (id_jornada)
ALTER TABLE servidor ADD FOREIGN KEY(id_telefones) REFERENCES telefones_institucionais (id_telefones)
ALTER TABLE servidor ADD FOREIGN KEY(id_campus) REFERENCES campus (id_campus)
