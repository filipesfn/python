create database livraria;
use livraria;

create table autores(
id int primary key auto_increment,
nome nvarchaR(255)
);

CREATE TABLE livros(
id int primary key auto_increment,
nome_livro nvarchar (255),
id_autor int,
foreign key (id_autor) references autores (id)  
);

insert into autores values (default, "Abelardo Fondue"), 
(default, "Sulamita Duduvier"), 
(default, "Gustavo Davidson"), 
(default, "Henrique Helios"),
(default, "Fabian Cluster");

select * from autores;

insert into livros values
(default, "Ruinas de um Império", 2),
(default, "Vida que Segue", 3),
(default, "Foi o que não deveria ter sido", 2),
(default, "Perseguição", 1),
(default, "Escute agora", 3),
(default, "Seja forte, mesmo assim", 4),
(default, "Guia-me", 5),
(default, "Forte como ferro", 4),
(default, "Hoje em dia é assim", 5),
(default, "Criaturas da minha vida", 1);

select autores.nome as Nome_do_autor,
nome_livro as Nome_dos_livros
from autores
inner join livros
on autores.id = livros.id_autor