# ORDER BY y LIMIT

`ORDER BY` y `LIMIT` son cláusulas muy útiles en MySQL para ordenar y limitar la cantidad de resultados arrojados por una consulta.

La cláusula `ORDER BY` se utiliza para ordenar el resultado de una consulta por una o más columnas según el criterio especificado. Por ejemplo, si queremos ordenar una lista de estudiantes por su nombre de forma alfabética, utilizaríamos la siguiente consulta:

```sql
SELECT * FROM estudiantes ORDER BY nombre;
```

El resultado sería una lista de estudiantes ordenada alfabéticamente por su nombre.

Por otro lado, la cláusula `LIMIT` se utiliza para limitar la cantidad de resultados de una consulta. Por ejemplo, si queremos obtener solamente los 5 primeros estudiantes en la lista ordenada alfabéticamente por su nombre, utilizaríamos la siguiente consulta:

```sql
SELECT * FROM estudiantes ORDER BY nombre LIMIT 5;
```

El resultado sería una lista con los primeros 5 estudiantes ordenados alfabéticamente por su nombre.

En resumen, la cláusula `ORDER BY` permite ordenar el resultado de una consulta según una o varias columnas, mientras que `LIMIT` permite limitar la cantidad de resultados obtenidos.

Casos de uso comunes para estas cláusulas son, por ejemplo, para paginación de resultados (utilizando `LIMIT` y `OFFSET`), o para obtener los resultados más recientes o más antiguos (utilizando `ORDER BY` y las funciones de fecha y hora de MySQL).