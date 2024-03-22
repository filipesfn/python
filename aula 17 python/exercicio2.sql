create database cadastro;
use cadastro;CREATE DATABASE cadastro;
USE cadastro;

CREATE TABLE pessoas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(255),
    cargo NVARCHAR(255),
    idade INT,
    CHECK(idade > 18)
);

INSERT INTO pessoas (nome, cargo, idade) VALUES 
('João', 'Engenheiro', 30),
('Maria', 'Analista', 25),
('Pedro', 'Desenvolvedor', 28),
('Ana', 'Gerente', 35),
('Carlos', 'Designer', 26),
('Juliana', 'Consultora', 29),
('Fernanda', 'Contadora', 40),
('Ricardo', 'Arquiteto', 45),
('Camila', 'Estudante', 20),
('Luiz', 'Advogado', 33);


SELECT
 nome AS Nome_do_Funcionario,
 cargo AS Cargo_do_Funcioario
 FROM pessoas;
 
SELECT * FROM pessoas ORDER BY idade;
SELECT * FROM pessoas ORDER BY idade DESC;