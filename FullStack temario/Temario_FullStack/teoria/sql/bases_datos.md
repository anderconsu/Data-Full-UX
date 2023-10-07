# Bases de datos y SQL

Una base de datos es un conjunto organizado de datos que se almacenan de manera persistente en un disco duro u otro medio de almacenamiento digital. Se utiliza para almacenar, organizar y acceder a grandes cantidades de datos de manera eficiente y segura. Las bases de datos se utilizan en una amplia gama de aplicaciones, desde tiendas en línea y sistemas bancarios hasta administración de registros médicos y científicos.

Las bases de datos se estructuran en tablas, que contienen filas y columnas. Las filas representan entradas individuales en la base de datos, mientras que las columnas representan los diferentes tipos de datos que se almacenan en la tabla. Cada fila en la tabla se identifica de forma única mediante una clave primaria, que es un valor que no se repite y que identifica de manera exclusiva esa fila.

En la mayoría de los sistemas de gestión de bases de datos (DBMS), se utilizan lenguajes de consulta estructurados (SQL) para crear, consultar y modificar tablas de bases de datos. Algunos ejemplos de comandos SQL incluyen:

- **SELECT**: el comando SELECT se utiliza para recuperar datos de una tabla. Por ejemplo, la siguiente consulta devolverá todos los datos en la tabla "clientes" con una dirección en Nueva York:

```
SELECT * FROM clientes WHERE direccion = 'Nueva York';
```

- **INSERT**: el comando INSERT se utiliza para agregar nuevas filas a una tabla. Por ejemplo, la siguiente consulta agregará un nuevo cliente a la tabla "clientes":

```
INSERT INTO clientes (nombre, direccion, telefono) VALUES ('Juan', 'Chicago', '555-1234');
```

- **UPDATE**: el comando UPDATE se utiliza para actualizar datos en una tabla. Por ejemplo, la siguiente consulta actualizará el teléfono del cliente con ID 1234 a '555-5678':

```
UPDATE clientes SET telefono = '555-5678' WHERE id = 1234;
```

- **DELETE**: el comando DELETE se utiliza para eliminar filas de una tabla. Por ejemplo, la siguiente consulta eliminará todos los clientes con una dirección en Nueva York:

```
DELETE FROM clientes WHERE direccion = 'Nueva York';
```

En resumen, las bases de datos se utilizan para almacenar grandes cantidades de información de manera organizada y eficiente. SQL es un lenguaje utilizado para consultar, modificar y manipular datos en bases de datos. Los ejemplos anteriores son solo algunos de los comandos que se pueden utilizar para trabajar con bases de datos en SQL.