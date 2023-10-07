# Procedimientos almacenados en MySQL

Un procedimiento almacenado en MySQL es un conjunto de instrucciones SQL que se almacenan en el servidor de bases de datos y se pueden invocar y ejecutar posteriormente utilizando un nombre específico. Entre los beneficios de los procedimientos almacenados están la reutilización del código, la encapsulación de la lógica de la base de datos y la mejora del rendimiento, ya que los procedimientos almacenados son compilados y optimizados de forma interna por el servidor antes de su ejecución.

Para crear un procedimiento almacenado en MySQL se utiliza la siguiente sintaxis:

```
CREATE PROCEDURE nombre_procedimiento ([parámetro1 tipo_dato, parámetro2 tipo_dato, ...])
BEGIN
    -- Instrucciones SQL aquí
END;
```

Donde `nombre_procedimiento` es el nombre que se le quiere dar al procedimiento almacenado, y los parámetros son opcionales y se utilizan para pasar datos al procedimiento. Dentro del cuerpo del procedimiento almacenado se pueden utilizar cualquier instrucción SQL, como SELECT, INSERT, UPDATE, DELETE, entre otras. A continuación se muestran algunos ejemplos de casos de uso de procedimientos almacenados en MySQL:

### Ejemplo 1: Procedimiento almacenado para insertar un registro en una tabla

En este ejemplo, se crea un procedimiento almacenado que recibe como parámetros los valores de una tabla `users` y se encarga de insertar un nuevo registro en dicha tabla.

```mysql
CREATE PROCEDURE insert_user(IN p_name VARCHAR(50), IN p_email VARCHAR(50))
BEGIN
    INSERT INTO users(name, email) VALUES(p_name, p_email);
END;
```

Luego, para invocar el procedimiento almacenado e insertar un nuevo usuario en la tabla, se puede utilizar la siguiente sintaxis:

```mysql
CALL insert_user('Juan', 'juan@example.com');
```

### Ejemplo 2: Procedimiento almacenado para actualizar un registro en una tabla

En este ejemplo, se crea un procedimiento almacenado que recibe como parámetros los valores de una tabla `users` y se encarga de actualizar un registro existente en dicha tabla.

```mysql
CREATE PROCEDURE update_user(IN p_id INT, IN p_name VARCHAR(50), IN p_email VARCHAR(50))
BEGIN
    UPDATE users SET name = p_name, email = p_email WHERE id = p_id;
END;
```

Luego, para actualizar un usuario existente en la tabla, se puede utilizar la siguiente sintaxis:

```mysql
CALL update_user(1, 'Pedro', 'pedro@example.com');
```

### Ejemplo 3: Procedimiento almacenado para obtener el promedio de una columna en una tabla

En este ejemplo, se crea un procedimiento almacenado que recibe como parámetros el nombre de una tabla y el nombre de una columna de dicha tabla, y se encarga de calcular el promedio de los valores de dicha columna.

```mysql
CREATE PROCEDURE get_average(IN p_table VARCHAR(50), IN p_column VARCHAR(50), OUT average DECIMAL(10,2))
BEGIN
    SET @query = CONCAT('SELECT AVG(', p_column, ') INTO @average FROM ', p_table);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    SET average = @average;
    DEALLOCATE PREPARE stmt;
END;
```

Para obtener el promedio de la columna `age` de la tabla `users`, por ejemplo, se puede utilizar la siguiente sintaxis:

```mysql
CALL get_average('users', 'age', @avg);
SELECT @avg;
```

En este caso, se utiliza una variable `@avg` para almacenar el resultado del procedimiento almacenado, y se muestra el resultado utilizando la instrucción SELECT. Además, este procedimiento almacenado utiliza la función PREPARE para crear dinámicamente una consulta SQL y la función EXECUTE para ejecutar dicha consulta.

---

Un procedimiento almacenado es una función que se guarda en la base de datos y puede ser llamado desde otra función o desde una aplicación. Los procedimientos almacenados pueden recibir parámetros y devolver resultados, y pueden ser una forma útil de encapsular lógica compleja en la base de datos.

Un caso de uso común para los procedimientos almacenados es para realizar operaciones en la base de datos que involucren varias tablas, como actualizar un registro en una tabla y luego insertar un registro relacionado en otra tabla.

Para crear un procedimiento almacenado en MySQL, se utiliza la sintaxis `CREATE PROCEDURE`. Por ejemplo, el siguiente procedimiento almacenado toma un parámetro `employee_id` y devuelve el nombre del empleado correspondiente:

```sql
CREATE PROCEDURE get_employee_name(IN employee_id INT)
BEGIN
  SELECT first_name, last_name FROM employees WHERE employee_id = employee_id;
END;
```

Para llamar a este procedimiento almacenado desde MySQL, se utiliza la sintaxis `CALL` seguida del nombre del procedimiento almacenado y cualquier parámetro requerido. Por ejemplo:

```sql
CALL get_employee_name(123);
```

Este procedimiento almacenado también podría ser llamado desde una aplicación que utiliza una biblioteca de acceso a bases de datos que admite procedimientos almacenados.

Otro ejemplo de uso de un procedimiento almacenado podría ser para actualizar varias tablas a la vez. Por ejemplo, el siguiente procedimiento almacenado toma dos parámetros, `product_id` y `new_price`, y actualiza la tabla de productos y la tabla de ventas para reflejar el nuevo precio:

```sql
CREATE PROCEDURE update_product_price(IN product_id INT, IN new_price DECIMAL(10,2))
BEGIN
  UPDATE products SET price = new_price WHERE id = product_id;
  UPDATE sales SET price = new_price WHERE product_id = product_id;
END;
```

En resumen, los procedimientos almacenados son una poderosa herramienta disponible en MySQL que se pueden utilizar para encapsular la lógica de base de datos compleja en una función. Esto puede hacer que las aplicaciones sean más eficientes y escalables, y permitir que los desarrolladores de aplicaciones se centren en la lógica empresarial en lugar de la lógica de la base de datos.