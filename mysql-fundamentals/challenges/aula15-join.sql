-- Contexto: Relatório completo de funcionários 
-- Objetivo: Relacionar dados 

SELECT f.nome, f.salario, d.nome AS departamentos
FROM funcionarios f 
JOIN departamentos d ON f.departamento_id = d.id;