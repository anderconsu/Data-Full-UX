# Tablas

Para crear tablas en MySQL se utiliza el comando `CREATE TABLE`. Este comando requiere de la definición detallada de las columnas y sus respectivos tipos de datos.

La sintaxis básica para crear una tabla es la siguiente:

```sql
CREATE TABLE nombre_tabla (
    nombre_columna1 tipo_dato_requerido,
    nombre_columna2 tipo_dato_requerido,
    ...
    nombre_columnaN tipo_dato_requerido
);
```

A continuación, se presenta un ejemplo de cómo crear una tabla simple con cuatro columnas.

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);
```

En este ejemplo, se crea una tabla llamada `usuarios` con cuatro columnas: 

- `id` de tipo `INT` y definido como `PRIMARY KEY`.
- `nombre` de tipo `VARCHAR` con una longitud máxima de 50 caracteres y marcado como `NOT NULL`.
- `email` de tipo `VARCHAR` con una longitud máxima de 100 caracteres y marcado como `NOT NULL`.
- `telefono` de tipo `VARCHAR` con una longitud máxima de 20 caracteres.

## Ejemplos de casos de uso

- Un sitio web que almacena información de usuarios, podría crear una tabla llamada `usuarios` que contenga su información personal como el nombre, correo electrónico y número de teléfono. Por ejemplo: 

```sql
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);
```

- Una aplicación de compras en línea podría crear una tabla llamada `productos` que contenga información sobre los productos que se venden, como su nombre, descripción, precio y disponibilidad. Por ejemplo:

```sql
CREATE TABLE productos (
    id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    disponible BOOLEAN DEFAULT true
);
```

- Una aplicación de seguimiento de citas médicas puede usar una tabla de `citas` que contenga información sobre las citas programadas de los pacientes, como la fecha, la hora y los datos del paciente. Por ejemplo:

```sql
CREATE TABLE citas (
    id INT PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    paciente_id INT NOT NULL,
    motivo VARCHAR(100)
);
```

Es importante tener en cuenta que existen muchos tipos de datos diferentes en MySQL, y que elegir el tipo de dato adecuado para cada columna es fundamental para el correcto funcionamiento de la aplicación y la eficiencia del almacenamiento de datos.


Para crear una tabla en MySQL debemos seguir los siguientes pasos:

1. Conectar a MySQL: podemos utilizar la consola de MySQL o alguna herramienta de gestión visual como MySQL Workbench.

2. Crear una base de datos: Si no tenemos una base de datos creada, debemos crearla mediante la sentencia `CREATE DATABASE`.

```sql
CREATE DATABASE mi_base_de_datos;
```

3. Seleccionar la base de datos: Una vez creada la base de datos, debemos seleccionarla mediante la sentencia `USE`.

```sql
USE mi_base_de_datos;
```

4. Crear la tabla: Podemos crear una tabla utilizando la sentencia `CREATE TABLE`. A la hora de crear la tabla debemos especificar su nombre, los nombres y tipos de datos de las columnas y las claves primarias y/o foráneas.

```sql
CREATE TABLE estudiantes (
  codigo INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  edad INT,
  carrera VARCHAR(50) DEFAULT 'Ingeniería'
);
```

En el ejemplo anterior hemos creado una tabla llamada `estudiantes`, con cuatro columnas: `codigo`, `nombre`, `apellido` y `edad`. 

- En la columna `codigo` hemos especificado que es un número entero que se autoincrementa y que es su clave primaria.
- En las columnas `nombre`y `apellido`  hemos especificado que son de tipo cadena de caracteres y número entero respectivamente y que no pueden admitir valores nulos.
- En la columna `edad` hemos especificado que es de tipo número entero y que admite valores nulos.
- En la columna `carrera` hemos especificado que es de tipo cadena de caracteres y que su valor por defecto es "Ingeniería".

5. Crear relaciones: Para crear relaciones entre tablas debemos especificar una clave foránea en una tabla que haga referencia a la clave primaria de otra tabla. Para ello podemos utilizar la sentencia `FOREIGN KEY`. A la hora de crear la clave foránea debemos especificar la columna en la tabla actual que será la clave foránea y a qué tabla y columna hace referencia.

```sql
CREATE TABLE matriculas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  codigo_estudiante INT,
  codigo_asignatura INT,
  FOREIGN KEY (codigo_estudiante) REFERENCES estudiantes(codigo),
  FOREIGN KEY (codigo_asignatura) REFERENCES asignaturas(codigo)
);
```

En el ejemplo anterior hemos creado una tabla llamada `matriculas`, con tres columnas: `id`, `codigo_estudiante` y `codigo_asignatura`.

- En la columna `id` hemos especificado que es un número entero que se autoincrementa y que es su clave primaria.
- En las columnas `codigo_estudiante` y `codigo_asignatura` hemos especificado que son de tipo número entero y que admiten valores nulos.
- En las claves foráneas hemos especificado que `codigo_estudiante` hace referencia a la columna `codigo` de la tabla `estudiantes` y `codigo_asignatura` hace referencia a la columna `codigo` de la tabla `asignaturas`.

Es importante resaltar que una tabla debe tener una clave primaria que la identifique única y claramente. El valor autoincremental permite que cada registro tenga un valor único y consecutivo, asegurando que no haya duplicidad en las claves primarias. Los valores por defecto o nulos permiten definir valores predeterminados para una columna o permitir que se dejen vacías en determinados casos. En cuanto a las claves foráneas, son útiles en el momento de relacionar tablas y para mantener la integridad referencial de los datos almacenados.

Un caso de uso de estas tablas y relaciones podría ser para una aplicación de matriculación de estudiantes en asignaturas de una universidad. La tabla `estudiantes` contendría los datos de los estudiantes matriculados, con su nombre, apellido, edad y carrera. La tabla `asignaturas` contendría información sobre las asignaturas ofertadas, como su nombre y su carga académica. La tabla `matriculas` actuaría como una tabla de relación entre ambas, indicando qué estudiante se ha matriculado en qué asignatura.