-- Contexto: Sistema de vendas da empresa
-- Objetivo: Análise de dados comerciais


-- Clientes
CREATE TABLE clientes (
	id INT auto_increment primary key,
    nome varchar(100)
);

-- Produtos
CREATE TABLE produtos (
	id INT auto_increment primary key,
    nome VARCHAR(100),
    preco DECIMAL(10, 2)
);

-- Pedidos
CREATE TABLE pedidos (
	id INT auto_increment primary key,
    cliente_id INT,
    produto_id INT,
    valor DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);


-- Valores inseridos para cada tabela: 
INSERT INTO clientes (nome) VALUES
('Vinicius'),
('Camila'),
('Hibrael'),
('Yuri'),
('Otto'),
('Jayme'),
('Felipe'),
('Lucas'),
('Samantha'),
('Gustavo');

INSERT INTO produtos(nome, preco) VALUES
('Notebook', 2500),
('Pão de queijo', 3.50),
('Maça', 10.10),
('X-salada', 25),
('Ifono', 3800),
('Monster', 12.99),
('Tapete', 52);

INSERT INTO pedidos (cliente_id, produto_id, valor) VALUES
(1, 1, 50.00),
(2, 2, 2500.00),
(3, 3, 35.00),
(4, 4, 20.20),
(5, 5, 25),
(6, 6, 3800),
(7, 7, 12.99);

-- Clientes que mais gastaram
SELECT c.nome, SUM(p.valor) AS total_gasto
FROM clientes c
JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.nome
ORDER BY total_gasto DESC;

-- Receita total
SELECT SUM(valor) AS receita_total FROM pedidos;

-- Produtos mais vendidos
SELECT produto_id, COUNT(*) AS total_vendas
FROM pedidos
GROUP BY produto_id
ORDER BY total_vendas DESC;

-- Clientes que nunca compraram
SELECT c.nome
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE p.id IS NULL;