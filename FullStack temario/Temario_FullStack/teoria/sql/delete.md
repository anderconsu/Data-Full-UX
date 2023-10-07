# DELETE

La instrucción DELETE en MySQL se utiliza para eliminar uno o varios registros de una tabla en una base de datos. La sintaxis básica es la siguiente:

```
DELETE FROM nombre_tabla WHERE condicion;
```

Donde `nombre_tabla` es el nombre de la tabla de la que se desean eliminar los registros y `condicion` es la condición que deben cumplir los registros para ser eliminados. Si no se especifica una condición, se eliminarán todos los registros de la tabla.

Ejemplo de código:

Supongamos que tenemos la siguiente tabla llamada `usuarios`:

```
+----+----------+-----------+
| id | nombre   | correo    |
+----+----------+-----------+
| 1  | Juan     | juan@ej.com   |
| 2  | Roberto  | robert@ej.com |
| 3  | Ana      | ana@ej.com    |
| 4  | Maria    | maria@ej.com  |
+----+----------+-----------+
```

Si quisieramos eliminar el registro de la usuaria Ana podríamos hacerlo de la siguiente manera:

```
DELETE FROM usuarios WHERE nombre = 'Ana';
```

La tabla resultante sería:

```
+----+----------+-----------+
| id | nombre   | correo    |
+----+----------+-----------+
| 1  | Juan     | juan@ej.com   |
| 2  | Roberto  | robert@ej.com |
| 4  | Maria    | maria@ej.com  |
+----+----------+-----------+
```

Caso de uso:

La instrucción DELETE suele ser utilizada en aplicaciones web para eliminar registros de una tabla de usuarios o cualquier otro tipo de tabla que contenga datos de la aplicación. También es común utilizarla en scripts automatizados para borrar información antigua y mantener la base de datos actualizada. Es importante tener en cuenta que la instrucción DELETE elimina información de manera permanente, así que es necesario tener precaución al utilizarla y siempre realizar copias de seguridad previas.