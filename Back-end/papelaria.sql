CREATE DATABASE Papelaria;

USE Papelaria;

CREATE TABLE Produto (
    idProduto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL
);

SELECT * FROM Produto;

-- Apagar o conteúdo da tabela
TRUNCATE TABLE produto;