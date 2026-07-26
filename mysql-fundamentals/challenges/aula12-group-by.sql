-- Contexto: Diretoria quer saber quantidade de funcionarios por cargo 
-- Objetivo: Agrupar dados 

SELECT cargo, COUNT(*) AS total
FROM funcionarios 
GROUP BY cargo; 