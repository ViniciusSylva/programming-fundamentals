-- Contexto: Organização por departamentos 
-- Objetivo: Criar relacionamentos entre tabelas 

CREATE TABLE departamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome varchar(100)
);

ALTER TABLE funcionarios
ADD departamento_id INT, 
ADD FOREIGN KEY (departamento_id) REFERENCES departamentos(id);
