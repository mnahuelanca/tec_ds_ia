USE tienda;

DROP TABLE productos;

CREATE TABLE productos(
	ID_PRODUCTOS INT PRIMARY KEY  AUTO_INCREMENT NOT NULL,
    NOMBRE VARCHAR (50) NOT NULL,
    PRECIO FLOAT
);

INSERT INTO productos (Nombre,Precio) VALUES("Coca cola","10.23");
INSERT INTO productos (Nombre,Precio) VALUES("Agua","2");
INSERT INTO productos (Nombre,Precio) VALUES("Caramelos","0.25");
INSERT INTO productos (Nombre,Precio) VALUES("Alfajor","1.20");
INSERT INTO productos (Nombre,Precio) VALUES("Pan","1.10");
SELECT * FROM productos;

SELECT * FROM productos WHERE PRECIO > 2;