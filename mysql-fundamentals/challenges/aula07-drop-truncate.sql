-- Contexto: Ambiente de testes precisa ser resetado 
-- Objetivo: Limpar e remover tabelas 

CREATE DATABASE teste (
    id int AUTOINCREMENT PRIMARY KEY
);

TRUNCATE TABLE;

DROP TABLE teste;
DROP DATABASE teste;