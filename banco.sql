sql

create database banco;
use banco;

create table usuarios (
    id int primary key auto_increment,
    nome varchar(100) not null,
    email varchar(120) not null unique,
    senha varchar(255),
    data_cadastro timestamp default current_timestamp
);

create table movimentacoes (
    id int auto_increment primary key,
    usuario_id int not null,
    tipo_conta enum('entrada', 'saida') not null,
    valor decimal(10,2) not null,
    descricao varchar(255),
    data_criacao timestamp default current_timestamp,
    foreign key (usuario_id) references usuarios(id)
);

insert into usuarios (nome, email, senha) values
('HUgo Romera', 'hromera761@gmail.com', 'senha123'),

insert into movimentacoes (usuario_id, tipo_conta, valor, descricao) values
(1, 'entrada', 1500.00, 'Salário mensal'),

insert into movimentacoes (usuario_id, tipo_conta, valor, descricao) values
(1, 'saida', 200.00, 'Compra de supermercado'),

select
    m.id,
    u.nome as usuario,
    m.tipo_conta, 
    m.valor, 
    m.descricao, 
    m.data_movimentacao
from movimentacoes m
join usuarios u on m.usuario_id = u.id;
order by m.data_movimentacao desc;

 select
    (select coalesce(sum(valor), 0) from movimentacoes where tipo_conta = 'entrada')
    (select coalesce(sum(valor), 0) from movimentacoes where tipo_conta = 'saida')
    as saldo_total;

select
    from movimentacoes
    where usuario_id = 1
    order by data_movimentacao desc;
    