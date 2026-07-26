-- Contexto: RH precisa armazenar dados de funcionários
-- Objetivo: Criar tabela estruturada

-- Criar tabela
CREATE TABLE funcionarios (
    id int auto_increment primary key,
    nome VARCHAR (100),
    cargo VARCHAR (50),
    salario DECIMAL(10,2),
    data_contratacao DATE
);
-- Arrumado o nome dos dados das tabelas, seus tipos e suas especficações 

-- Seleciona todos os dados de funcionarios e mostra eles
SELECT * FROM funcionarios
