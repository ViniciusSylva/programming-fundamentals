-- Contexto: Funcionário recebeu aumento e outro foi desligado 
-- Objetivo: Atualizar e remover dados 

UPDATE funcionarios
SET salario 15200.00
WHERE cargo = 'Coordenadora de projetos';

DELETE FROM funcionarios 
WHERE data_contratacao = '2022-09-05'