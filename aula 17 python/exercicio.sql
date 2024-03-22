create database agencia;
use agencia;

CREATE TABLE clientes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(255) NOT NULL,
    cpf CHAR(11) UNIQUE NOT NULL,
    data_nasc DATE,
    salario float
    );
    
create table contas( 
    id INT PRIMARY KEY AUTO_INCREMENT,
    saldo float,
    tipo VARCHAR(11),
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
    );
    
create table emprestimos(
id INT PRIMARY KEY AUTO_INCREMENT,
id_cliente int,
FOREIGN KEY (id_cliente) REFERENCES clientes(id),
valor float not null, data_emprestimo datetime
);

INSERT INTO clientes (id, nome, cpf, data_nasc, salario)
VALUES
    (default, 'Maria Silva', '12345678901', '1990-05-15', 5000.00),
    (default, 'João Santos', '98765432109', '1985-08-20', 6000.00),
    (default, 'Abel Cortes', '12395678901', '1993-05-15', 5000.00),
    (default, 'Sid Campos', '98765432100', '1986-08-20', 6000.00),
    (default, 'Vanessa Lord', '11345678788', '1981-05-15', 5000.00),
    (default, 'Gustavo Abreu', '98765436109', '1989-08-20', 6000.00),
    (default, 'Fabricio Almada', '12315678901', '1997-05-15', 5000.00),
    (default, 'Tadeu Barcelos', '98700432109', '1961-08-20', 6000.00),
    (default, 'Helio Nalbert', '12345666901', '1998-05-15', 5000.00),
    (default, 'Rafael Pereira', '98765494309', '1993-08-20', 6000.00);
    
INSERT INTO contas (id, saldo, tipo, id_cliente)
VALUES
    (default, 11000.00, 'Corrente',11),
    (default, 5000.00, 'Poupança',12),
    (default, 6000.00, 'Poupança',13),
    (default, 4000.00, 'Poupança',14),
    (default, 10000.00, 'Poupança',15),
    (default, 6500.00, 'Poupança',16),
    (default, 7400.00, 'Poupança',17),
    (default, 56.00, 'Poupança',18);
    
    select * from contas;
    
    truncate table contas;
 
 

INSERT INTO emprestimos (valor, id_cliente, data_emprestimo) VALUES 
(2000.00, 11, '2024-03-22 10:30:00'),
(3000.00, 12, '2024-03-21 09:45:00'),
(4000.00, 13, '2024-03-20 15:20:00'),
(2500.00, 14, '2024-03-19 14:10:00'),
(3500.00, 15, '2024-03-18 11:55:00'),
(4500.00, 16, '2024-03-17 08:40:00');
    
    
UPDATE clientes
SET nome = 'Abel Cortes', cpf = '12395678901'
WHERE id = 3;

UPDATE contas
SET tipo = 'Poupança', saldo =9000.00
WHERE id = 6;

UPDATE emprestimos
SET valor = 3000.00
WHERE id = 22;

DELETE FROM clientes WHERE id = 9 OR id = 10;
DELETE FROM contas WHERE id = 4;

SELECT * FROM clientes;
SELECT * FROM contas;
SELECT * FROM emprestimos;

SELECT * FROM contas WHERE tipo = "Poupança" AND saldo > 6000;   