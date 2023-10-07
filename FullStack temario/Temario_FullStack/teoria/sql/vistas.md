# Vistas

En MySQL, las vistas son objetos que contienen una consulta SQL en sí mismas y se utilizan para simplificar el acceso a datos complejos a través de una consulta más simple y con un nombre asignado. Básicamente, una vista es una tabla virtual que representa los resultados de una consulta SQL.

Las vistas pueden ser utilizadas para:

- Simplificar consultas complejas: las consultas SQL que involucran múltiples tablas y condiciones pueden ser difíciles de entender y de mantener. Las vistas pueden simplificar estas consultas al permitir que el usuario final pueda acceder a un conjunto más reducido y lógicamente estructurado de datos.
- Establecer niveles de seguridad: Las vistas pueden utilizarse para restringir el acceso a determinados datos sensibles. Por ejemplo, se podría crear una vista sobre una tabla que sólo muestre los datos relevantes, dejando fuera los datos confidenciales. De esta forma, las personas tienen acceso a los datos necesarios sin exponer información delicada.
- Compartir datos: Las vistas pueden ser utilizadas para compartir conjuntos de datos complejos con diversos usuarios que no necesariamente tienen conocimientos técnicos para crear y ejecutar consultas complejas en SQL.

Para crear una vista en MySQL, se utiliza la sintaxis `CREATE VIEW`. Por ejemplo, si quisieramos crear una vista para mostrar los artículos de una tienda en línea que tienen una cantidad mayor o igual a 10, se escribiría una consulta SQL que filtre los productos que cumplan la condición y se crearía una vista con esa consulta:

```mysql
CREATE VIEW tienda_view AS
    SELECT * FROM articulos WHERE cantidad >= 10;
```

Una vez creada la vista, podemos utilizarla en cualquier consulta SQL como si se tratara de una tabla virtual normal:

```mysql
SELECT * FROM tienda_view WHERE precio > 100;
```

Es importante notar que las vistas no almacenan datos, sino que son simplemente una "vista virtual" de los datos reales que se encuentran en las tablas subyacentes. Cada vez que se hace una consulta a la vista, se ejecuta la consulta SQL que la definió.

Es posible modificar una vista existente utilizando la sintaxis `ALTER VIEW`, así como también se puede eliminar utilizando `DROP VIEW`.