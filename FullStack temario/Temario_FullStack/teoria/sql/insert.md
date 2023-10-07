# INSERT

El comando INSERT en MySQL se utiliza para insertar datos en una tabla existente en una base de datos. Para insertar datos, debemos especificar la tabla y los valores que deseamos agregar. A continuación, se muestra la sintaxis básica del comando INSERT en MySQL:

```
INSERT INTO nombre_de_la_tabla (columna1, columna2, columna3, ...) VALUES (valor1, valor2, valor3, ...);
```

Donde "nombre_de_la_tabla" es el nombre de la tabla en la que deseamos insertar los datos, y "columna1", "columna2", "columna3", ... son los nombres de las columnas a las que deseamos agregar valores. Los valores que deseamos agregar se proporcionan en el orden correspondiente de las columnas.

A continuación se muestran algunos ejemplos de cómo utilizar el comando INSERT en MySQL:

1. Insertar un solo registro en una tabla

```
INSERT INTO estudiantes (nombre, edad, email) VALUES ('Juan Pérez', 20, 'juan.perez@ejemplo.com');
```

2. Insertar varios registros en una tabla

```
INSERT INTO estudiantes (nombre, edad, email) VALUES ('Pedro López', 22, 'pedro.lopez@ejemplo.com'), ('Ana García', 21, 'ana.garcia@ejemplo.com'), ('María Hernández', 20, 'maria.hernandez@ejemplo.com');
```

3. Insertar un registro en una tabla con campos NULL

```
INSERT INTO estudiantes (id, nombre, edad, email) VALUES (1, 'Luisa Torres', NULL, 'luisa.torres@ejemplo.com');
```

En este caso, estamos insertando un registro en la tabla "estudiantes" con un valor NULL en la columna "edad".

El comando INSERT se utiliza principalmente para agregar nuevos registros a una tabla. Por ejemplo, podemos utilizar INSERT para agregar datos de nuevos estudiantes a una tabla de estudiantes. Además, también es posible utilizar el comando INSERT para agregar registros a una tabla de seguimiento de cambios, donde se registran los cambios realizados en una tabla principal.