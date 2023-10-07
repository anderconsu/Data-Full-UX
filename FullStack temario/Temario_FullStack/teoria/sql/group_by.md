# GROUP BY

GROUP BY es una cláusula utilizada para agrupar filas en una tabla en función de una o varias columnas. Se utiliza principalmente junto con funciones de agregado como COUNT(), SUM(), AVG(), MIN(), MAX(), etc. para calcular y resumir datos basados en grupos.

La sintaxis básica de GROUP BY en MySQL es la siguiente:

```
SELECT columna1, columna2, funcion_agregada(columna3)
FROM tabla
GROUP BY columna1, columna2;
```

Aquí, `columna1` y `columna2` son las columnas que se utilizarán para agrupar las filas, y `funcion_agregada(columna3)` es una función de agregado que se utilizará para calcular valores para cada grupo.

Veamos un ejemplo práctico de cómo se utiliza GROUP BY en MySQL. Supongamos que tenemos una tabla llamada "ordenes" que contiene información sobre las órdenes de compra realizadas por los clientes:

```
+----+------------+----------+-------+
| id | fecha      | cliente  | total |
+----+------------+----------+-------+
| 1  | 2021-01-01 | Juan     | 100   |
| 2  | 2021-01-02 | Pedro    | 50    |
| 3  | 2021-01-03 | Juan     | 200   |
| 4  | 2021-01-04 | Carlos   | 75    |
| 5  | 2021-01-05 | Pedro    | 125   |
+----+------------+----------+-------+
```

Podemos utilizar GROUP BY para obtener el total de ventas por cliente:

```
SELECT cliente, SUM(total)
FROM ordenes
GROUP BY cliente;
```

El resultado será el siguiente:

```
+----------+-----------+
| cliente  | SUM(total) |
+----------+-----------+
| Juan     | 300       |
| Pedro    | 175       |
| Carlos   | 75        |
+----------+-----------+
```

En este ejemplo, utilizamos la función de agregado SUM() para calcular el total de ventas por cliente. Los resultados se agruparon por la columna "cliente".

Otro caso de uso común de GROUP BY es el cálculo de datos estadísticos. Por ejemplo, podemos utilizar GROUP BY para calcular la cantidad de órdenes realizadas cada mes:

```
SELECT MONTH(fecha), COUNT(id)
FROM ordenes
GROUP BY MONTH(fecha);
```

El resultado será el siguiente:

```
+------------+-----------+
| MONTH(fecha) | COUNT(id) |
+------------+-----------+
| 1           | 5         |
+------------+-----------+
```

En este ejemplo, utilizamos la función de fecha MONTH() para extraer el mes de la fecha de cada orden. Luego, utilizamos la función de agregado COUNT() para contar la cantidad de órdenes por mes.

En resumen, GROUP BY es una cláusula muy útil en MySQL que se utiliza para agrupar filas por una o varias columnas y realizar cálculos estadísticos en los datos. Se utiliza principalmente junto con funciones de agregado para resumir los datos en función de un criterio de agrupación específico.