create database livraria;

use livraria;

create table pessoas(

nome varchar(50),
idade int,
cep varchar(20),
cpf varchar(20)

);

create table livro(
nome varchar(100),
genero varchar(50),
preco real

);

create table produtos(

nome varchar(50),
cargo varchar(20),
cpf int primary key 

);

create table materiais(
id int primary key auto_increment,
nome varchar(50),
tamanho varchar(20),
material varchar (50)
);

insert into produtos values ('o produto', 'o cargo', '123321');


insert into pessoas values ('caio', 24, '22760-600', '12345678911');
insert into pessoas values ('Marcio Machado', 28, '22760-800', '98765432100');



