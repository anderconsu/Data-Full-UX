# Funciones en MySQL

En MySQL, las funciones son subrutinas que pueden recibir parámetros y realizar operaciones compactas y repetitivas. Estas se crean utilizando la sentencia `CREATE FUNCTION`, que además permite especificar tanto el nombre y los tipos de datos de los parámetros, como el tipo de dato que retornará la función.

Aquí tienes un ejemplo básico de la sintaxis que se utiliza para crear una función en MySQL:

```mysql
CREATE FUNCTION nombre_funcion (parametros)
RETURNS tipo_dato_retorno
BEGIN
  -- cuerpo de la función
END;
```

A continuación, se describen los componentes principales de esta sintaxis:

- `nombre_funcion`: Es el nombre que se le dará a la función que se está creando.

- `(parametros)`: Es la lista de parámetros que recibirá la función. Cada parámetro se especifica como `nombre_parametro tipo_dato_parametro` y se separan por comas. Estos parámetros son opcionales y la función también puede ser definida sin ellos.

- `RETURNS tipo_dato_retorno`: Es el tipo de dato que retornará la función. Si la función no retorna ningún valor, se debe utilizar `RETURNS VOID`.

- `BEGIN`: Es el inicio del bloque de código que conforma el cuerpo de la función.

- `END`: Es el final del bloque de código que conforma el cuerpo de la función.

En MySQL, podemos crear funciones que realicen diversas operaciones, como por ejemplo:

- Cálculo de valores
- Concatenación de cadenas
- Manipulación de fechas
- Agregación de datos
- Validación de datos, entre otros

Veamos un ejemplo de una función que calcule el promedio de tres números:

```mysql
CREATE FUNCTION calcular_promedio(num1 INT, num2 INT, num3 INT)
RETURNS FLOAT
BEGIN
  DECLARE promedio FLOAT;
  SET promedio = (num1 + num2 + num3) / 3;
  RETURN promedio;
END;
```

En este caso, la función recibe tres parámetros enteros (`num1`, `num2`, `num3`) y retorna el resultado de la operación `(num1 + num2 + num3) / 3` como un valor de punto flotante.

Una vez que hemos creado la función, podemos llamarla de la siguiente manera:

```mysql
SELECT calcular_promedio(5, 10, 15); -- Devuelve 10
```

En resumen, las funciones en MySQL nos permiten crear código reutilizable que puede ser utilizado en distintas partes de nuestro sistema, lo que nos ayuda a tener un código más limpio, fácil de entender y mantener.