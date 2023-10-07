# Funciones de agregación en MySQL

En MySQL podemos utilizar las siguientes funciones de agregación para obtener resúmenes de los datos almacenados en nuestras tablas: COUNT(), SUM(), AVG(), MIN() y MAX(). 

1. COUNT() : Se utiliza para contar el número de filas que existe en una tabla. Es muy útil para saber la cantidad de registros que se tienen en una tabla.

Ejemplo de consulta COUNT(): 

```
SELECT COUNT(*) FROM ventas;
```

Este ejemplo devuelve el número total de registros que se tienen en la tabla de ventas. 

2. SUM() : Se utiliza para sumar los valores de una columna especificada en una tabla. 

Ejemplo de consulta SUM():

```
SELECT SUM(cantidad) FROM ventas;
```

Este ejemplo devuelve la suma total de la cantidad vendida en la tabla de ventas.

3. AVG() : Se utiliza para obtener el promedio de los valores de una columna especificada en una tabla.

Ejemplo de consulta AVG():

```
SELECT AVG(precio) FROM productos;
```

Este ejemplo devuelve el promedio de precio de todos los productos que se tienen en la tabla de productos.

4. MIN() : Se utiliza para obtener el valor mínimo de una columna especificada en una tabla.

Ejemplo de consulta MIN():

```
SELECT MIN(precio) FROM productos;
```

Este ejemplo devuelve el precio mínimo de un producto almacenado en la tabla de productos.

5. MAX() : Se utiliza para obtener el valor máximo de una columna especificada en una tabla.

Ejemplo de consulta MAX():

```
SELECT MAX(precio) FROM productos;
```

Este ejemplo devuelve el precio máximo de un producto almacenado en la tabla de productos.

Estas funciones son muy útiles en el ámbito empresarial, para hacer reportes de ventas, control de inventarios, análisis de estadísticas de una empresa, entre otros.