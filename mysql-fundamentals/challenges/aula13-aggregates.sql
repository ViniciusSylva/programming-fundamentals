-- Contexto: Diretoria quer análise salarial 
-- Objetivo: Calcular métricas 

SELECT
    AVG(salario) AS media_salarial,
    MAX(salario) AS maior_salario,
    SUM(salario) AS folha_total
FROM funcionarios; 

-- AVG Calcula o salário médio dos colaboradores (patamar salarial)
-- MAX Identifica o teto salárial atual da empresa 
-- SUM Soma o custo total bruto com salários (orçamento da folha)