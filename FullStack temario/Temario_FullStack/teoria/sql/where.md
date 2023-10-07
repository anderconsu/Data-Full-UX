# WHERE

WHERE es una cláusula en SQL que se utiliza para filtrar registros en una consulta SELECT. Con WHERE puedes especificar una condición para seleccionar los registros que cumplan con esa condición.

Por ejemplo, si tienes una tabla 'users':

| id | name     | age |
|----|----------|-----|
| 1  | John Doe | 25  |
| 2  | Jane Doe | 30  |
| 3  | Bob Smith| 35  |

Puedes usar WHERE para seleccionar solo los usuarios que tengan una edad de 30 años, ejecutando la siguiente consulta:

```sql
SELECT * FROM users WHERE age = 30;
```

El resultado de la consulta sería este:

| id | name     | age |
|----|----------|-----|
| 2  | Jane Doe | 30  |

Puedes combinar WHERE con otras cláusulas como SELECT, ORDER BY y GROUP BY para hacer consultas más complejas. Por ejemplo:

```sql
SELECT name FROM users WHERE age > 30 ORDER BY age DESC;
```

En este caso, solo se selecciona el campo 'name' de los usuarios que tengan una edad mayor a 30, y se ordena el resultado por edad de forma descendente. El resultado de la consulta sería:

| name     |
|----------|
| Bob Smith|

Otros operadores que se pueden utilizar con WHERE son:

- = (igual a)
- <> (diferente a)
- > (mayor que)
- < (menor que)
- >= (mayor o igual que)
- <= (menor o igual que)
- BETWEEN (entre un rango de valores)
- LIKE (para hacer coincidencias parciales)
- IN (para buscar valores en una lista)

Por ejemplo, para seleccionar los usuarios que se llamen John o Jane:

```sql
SELECT * FROM users WHERE name IN ('John Doe', 'Jane Doe');
```

El resultado sería:

| id | name     | age |
|----|----------|-----|
| 1  | John Doe | 25  |
| 2  | Jane Doe | 30  |

En resumen, WHERE es una cláusula importante en SQL que te permite filtrar y seleccionar registros basados en diferentes condiciones.