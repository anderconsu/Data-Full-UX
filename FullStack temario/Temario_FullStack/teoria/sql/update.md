# UPDATE

La cláusula `UPDATE` se utiliza en MySQL para modificar datos en una tabla. La sintaxis básica es la siguiente:

```
UPDATE nombre_tabla
SET columna1 = valor1, columna2 = valor2, ...
WHERE condicion;
```

- `nombre_tabla`: el nombre de la tabla que se va a actualizar.
- `columna1`, `columna2`, ...: las columnas que se van a actualizar.
- `valor1`, `valor2`, ...: los nuevos valores que se van a asignar a las columnas.
- `condicion`: una cláusula WHERE opcional que especifica qué filas deben actualizarse.

Ejemplo de código:

Supongamos que tenemos la siguiente tabla llamada `usuarios`:

```
+----+-------+--------+-----------+
| id | nombre| apellido| email     |
+----+-------+--------+-----------+
|  1 | Juan  | Perez  | jp@ejemplo.com    |
|  2 | Maria | Garcia | mg@ejemplo.com    |
|  3 | Pedro | Ramirez| pr@ejemplo.com    |
+----+-------+--------+-----------+
```

Si queremos cambiar el email de Maria a `maria@ejemplo.com`, podemos hacerlo de la siguiente manera:

```sql
UPDATE usuarios
SET email = 'maria@ejemplo.com'
WHERE nombre = 'Maria';
```

Después de ejecutar esta sentencia, la tabla `usuarios` se verá así:

```
+----+-------+--------+-----------------+
| id | nombre| apellido| email           |
+----+-------+--------+-----------------+
|  1 | Juan  | Perez  | jp@ejemplo.com  |
|  2 | Maria | Garcia | maria@ejemplo.com|
|  3 | Pedro | Ramirez| pr@ejemplo.com  |
+----+-------+--------+-----------------+
```

La cláusula WHERE es opcional, pero si no se utiliza, se actualizarán todas las filas de la tabla.

Otro ejemplo de uso de la cláusula UPDATE es actualizar varias columnas al mismo tiempo. Por ejemplo, si queremos cambiar el nombre y el apellido de Pedro a Juan Perez, lo hacemos así:

```sql
UPDATE usuarios
SET nombre = 'Juan', apellido = 'Perez'
WHERE id = 3;
```

Y la tabla quedará:

```
+----+-------+--------+-----------------+
| id | nombre| apellido| email           |
+----+-------+--------+-----------------+
|  1 | Juan  | Perez  | jp@ejemplo.com  |
|  2 | Maria | Garcia | mg@ejemplo.com  |
|  3 | Juan  | Perez  | pr@ejemplo.com  |
+----+-------+--------+-----------------+
```

En resumen, la sentencia UPDATE se usa en MySQL para modificar los datos existentes en una tabla. La cláusula SET establece los nuevos valores para las columnas y se usa la cláusula WHERE para especificar qué filas se deben actualizar.