-- Creo la base de datos
CREATE DATABASE db_empresa;

-- Pongo en uso la base de datos
USE db_empresa;

-- Creo tabla departamentos
CREATE TABLE departamentos(
	ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR (100) NOT NULL
);


-- Creo tabla empleados
CREATE TABLE empleados(
	ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    NOMBRE VARCHAR (100) NOT NULL,
    APELLIDO VARCHAR (100) NOT NULL,
    DEPARTAMENTO_ID INT NOT NULL,
    FOREIGN KEY (DEPARTAMENTO_ID) REFERENCES departamentos (ID)
);

-- Agrego valores a departamentos
INSERT INTO departamentos (ID, NOMBRE) VALUES 
							(101, "Ventas"),
                            (102, "Marketing"),
							(103, "Recursos Humanos");
                            
-- Agrego valores a empleados
INSERT INTO empleados (ID, NOMBRE, APELLIDO, DEPARTAMENTO_ID) VALUES
    (1, 'Juan', 'Pérez', 101),
    (2, 'María', 'Rodríguez', 102),
    (3, 'Carlos', 'García', 101),
    (4, 'Laura', 'López', 103),
    (5, 'Ana', 'Martínez', 102),
    (6, 'Diego', 'Fernández', 103),
    (7, 'Sofia', 'González', 101),
    (8, 'Javier', 'Ramírez', 102),
    (9, 'Valentina', 'Díaz', 103),
    (10, 'Pedro', 'Sánchez', 101),
    (11, 'Martín', 'Torres', 102),
    (12, 'Isabel', 'Ramírez', 101),
    (13, 'Alejandro', 'González', 103),
    (14, 'Gabriela', 'López', 102),
    (15, 'Luis', 'Martínez', 101);

-- Join entre empleados y departamentos
SELECT * FROM empleados JOIN departamentos ON empleados.departamento_id = departamentos.id;