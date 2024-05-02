CREATE DATABASE tienda;

USE tienda;

CREATE TABLE productos(
	ID_producto INT,
    Nombre VARCHAR (30),
    Precio FLOAT
);

CREATE TABLE clientes(
	ID_cliente INT,
    Nombre VARCHAR (30),
    Direccion VARCHAR (50)
)