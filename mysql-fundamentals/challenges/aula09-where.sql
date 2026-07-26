-- Contexto: Análise de salários e cargos 
-- Objetivo: Filtrar dados relevantes 

-- Funcionário com salário acima de 3000
SELECT * FROM funcionarios 
WHERE salario > 3000; 

-- Apenas desenvolvedores 
SELECT * FROM funcionarios
WHERE cargo = 'Desenvolvedor'; 