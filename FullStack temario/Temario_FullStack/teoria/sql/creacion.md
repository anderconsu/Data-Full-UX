# Creación de una base de datos

Para crear bases de datos SQL se necesita utilizar un Sistema Gestor de Bases de Datos (SGBD) que permita crear, gestionar y manipular las bases de datos. Algunos de los SGBD más utilizados son MySQL, Oracle, PostgreSQL y Microsoft SQL Server.

Para crear una base de datos SQL se siguen los siguientes pasos:

1. Abrir el SGBD y conectarse al servidor o motor de bases de datos.
2. Crear una nueva base de datos y asignarle un nombre. Ejemplo:

```
CREATE DATABASE nombre_de_la_base_de_datos;
```

3. Definir la estructura de la base de datos creando tablas con campos y tipos de datos específicos. Ejemplo:

```
CREATE TABLE nombre_de_la_tabla (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT,
    email VARCHAR(100)
);
```

4. Ingresar los datos en las tablas mediante sentencias INSERT. Ejemplo:

```
INSERT INTO nombre_de_la_tabla (id, nombre, edad, email)
VALUES (1, 'Juan', 25, 'juan@mail.com'),
       (2, 'Ana', 30, 'ana@mail.com');
```

5. Consultar la información de la base de datos mediante sentencias SELECT. Ejemplo:

```
SELECT * FROM nombre_de_la_tabla;
```

Estos son solo algunos de los pasos básicos para crear una base de datos SQL. Sin embargo, pueden variar dependiendo del SGBD utilizado y del tipo de proyecto en el que se esté trabajando. Es importante tener en cuenta la normalización de la base de datos y la seguridad de la misma para garantizar su óptimo funcionamiento.