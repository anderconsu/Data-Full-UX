# Normalización de bases de datos

La normalización de bases de datos relacionales es una técnica que consiste en organizar la información de una base de datos en estructuras lógicas que eliminan la redundancia y aseguran la integridad de los datos.

[Wikipedia](https://es.wikipedia.org/wiki/Normalizaci%C3%B3n_de_bases_de_datos)

Existen distintos niveles de normalización, pero los más importantes son el primero, segundo y tercero (1NF, 2NF y 3NF respectivamente). A continuación, se describen los conceptos básicos de cada uno de ellos:

- 1NF (Primera Forma Normal): Esta forma normal establece que cada tabla debe tener una clave primaria y que todas las columnas deben contener valores atómicos. Es decir, que los valores de una columna no pueden ser arrays, objetos o cualquier otra estructura compleja.

- 2NF (Segunda Forma Normal): Una tabla está en segunda forma normal si cumple con la 1NF y, además, si cada columna no clave depende completamente de la clave primaria. En otras palabras, que no exista redundancia de datos. Para cumplir con esta forma normal, se pueden separar las tablas en dos o más si es necesario.

- 3NF (Tercera Forma Normal): Una tabla está en tercera forma normal si cumple con la 2FN y, además, no existe ninguna dependencia entre las columnas no clave. Al igual que en la forma normal anterior, si se detecta alguna dependencia se pueden separar las tablas en dos o más para cumplir con esta forma normal.

Veamos ahora un ejemplo de código para definir una base de datos y aplicar la normalización:

```sql
-- Definición de las tablas
CREATE TABLE alumnos (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  edad INT NOT NULL,
  carrera VARCHAR(50) NOT NULL
);

CREATE TABLE materias (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  creditos INT NOT NULL
);

CREATE TABLE inscripciones (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  id_alumno INTEGER NOT NULL,
  id_materia INTEGER NOT NULL,
  semestre INT NOT NULL,
  FOREIGN KEY (id_alumno) REFERENCES alumnos(id),
  FOREIGN KEY (id_materia) REFERENCES materias(id)
);

-- Ejemplo de inserción de datos
INSERT INTO alumnos(nombre, edad, carrera) VALUES ('Juan', 20, 'Informática');
INSERT INTO materias(nombre, creditos) VALUES ('Bases de datos', 6);
INSERT INTO inscripciones(id_alumno, id_materia, semestre) VALUES (1, 1, 2020);

-- Consulta de datos
SELECT alumnos.nombre, materias.nombre, inscripciones.semestre
FROM alumnos INNER JOIN inscripciones ON alumnos.id = inscripciones.id_alumno
INNER JOIN materias ON materias.id = inscripciones.id_materia;
```

En este ejemplo, se definen tres tablas: `alumnos`, `materias` e `inscripciones`. La tabla `alumnos` contiene información sobre los estudiantes como su nombre, edad y carrera. La tabla `materias` contiene información sobre las asignaturas que se ofrecen, incluyendo su nombre y la cantidad de créditos que tienen. Por último, la tabla `inscripciones` asemeja la relación entre ambas tablas.

La tabla `inscripciones` es una tabla de relación y cumple con la 3NF al no existir dependencia entre las columnas no clave.

La consulta de datos muestra cómo se pueden hacer joins entre las tablas para obtener información detallada al respecto.

En conclusión, la normalización de bases de datos es una técnica necesaria para garantizar la integridad y eficiencia de una base de datos. Es importante tener en cuenta los diferentes niveles de normalización y aplicarlos según sea necesario. Además, es importante también tener en cuenta que la normalización no siempre es la mejor opción, ya que en algunos casos puede reducir la eficiencia de las consultas en detrimento de la integridad.