#Creo base y tablas
CREATE DATABASE	gimnasio;

USE gimnasio;

CREATE TABLE socios(
	ID_Socio INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR (50),#A,4,%
    Apellido VARCHAR (50),
    DNI INT,
    Fecha_Nacimiento DATE
);

CREATE TABLE planes(
	ID_Plan INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR (50),
    Descripcion VARCHAR (255),
    Precio DECIMAL (10,2) 
#Hasta 8 dígitos antes del punto decimal y 2 dígitos después del punto decimal.
);

CREATE TABLE inscripciones(
	ID_Inscripcion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ID_Socio INT,
    ID_Plan INT,
    Fecha_inicio DATE,
    Fecha_baja DATE,
    FOREIGN KEY (ID_Socio) REFERENCES socios (ID_Socio),
    FOREIGN KEY (ID_Plan) REFERENCES planes (ID_Plan)
);

#ingreso datos
INSERT INTO socios (Nombre, Apellido, DNI, Fecha_Nacimiento) VALUES("Juan", "Perez", 35421678, '1980-01-02');
INSERT INTO socios (Nombre, Apellido, DNI, Fecha_Nacimiento) VALUES("Maria", "Gomez", 28974563, '1990-03-04');
INSERT INTO socios (Nombre, Apellido, DNI, Fecha_Nacimiento) VALUES("Pedro", "Lopez", 42013856, '2000-05-06');

INSERT INTO planes (Nombre, Descripcion, Precio) VALUES
("Basico", "Acceso a sala de musculación y clases grupales", 5000);
INSERT INTO planes (Nombre, Descripcion, Precio) VALUES
("Full", "Acceso a sala de musculación, clases grupales y natación", 7000);
INSERT INTO planes (Nombre, Descripcion, Precio) VALUES
("Premium", "Acceso a sala de musculación, clases grupales, natación y sauna ", 9000);

INSERT INTO inscripciones (ID_Socio, ID_Plan, Fecha_inicio) VALUES(1, 1, '2024-04-01');
INSERT INTO inscripciones (ID_Socio, ID_Plan, Fecha_inicio) VALUES(2, 2, '2024-05-15');
INSERT INTO inscripciones (ID_Socio, ID_Plan, Fecha_inicio) VALUES(3, 3, '2024-06-01');

SELECT * FROM socios;
SELECT * FROM planes;
SELECT * FROM inscripciones;
