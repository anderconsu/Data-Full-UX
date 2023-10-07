# JOIN

En MySQL, el comando JOIN se utiliza para combinar filas de dos o más tablas basadas en una condición común. Puedes usar JOIN para unir dos o más tablas y recuperar datos de ambas tablas al mismo tiempo.

Existen cuatro tipos de JOIN en MySQL:

- INNER JOIN: muestra solo los registros que tienen una coincidencia en ambas tablas que están siendo unidas.
- LEFT JOIN: muestra todos los registros de la tabla izquierda y los registros coincidentes de la tabla derecha.
- RIGHT JOIN: muestra todos los registros de la tabla derecha y los registros coincidentes de la tabla izquierda.
- FULL OUTER JOIN: incluye todos los registros de ambas tablas, coincidentes o no coincidentes.

A continuación, se muestran algunos ejemplos de código para cada tipo de JOIN:

INNER JOIN:
```
SELECT *
FROM tabla1
INNER JOIN tabla2
ON tabla1.columna = tabla2.columna
```

LEFT JOIN:
```
SELECT *
FROM tabla1
LEFT JOIN tabla2
ON tabla1.columna = tabla2.columna
```

RIGHT JOIN:
```
SELECT *
FROM tabla1
RIGHT JOIN tabla2
ON tabla1.columna = tabla2.columna
```

FULL OUTER JOIN:
```
SELECT *
FROM tabla1
FULL OUTER JOIN tabla2
ON tabla1.columna = tabla2.columna
```

Un caso de uso común para JOIN es cuando tienes dos tablas que contienen información relacionada pero no quieres unir la información en una sola tabla debido a la redundancia de datos. En cambio, puedes unir las tablas utilizando una condición común para obtener información correlacionada de ambas tablas. Por ejemplo, podrías tener una tabla de pedidos y una tabla de productos, y unir las dos tablas basándose en el identificador del producto para obtener información de pedidos y productos juntos en una sola consulta.

Es importante recordar que JOIN puede ser costoso en términos de rendimiento, especialmente cuando se unen tablas con grandes cantidades de datos. Es necesario optimizar las consultas y utilizar índices para mejorar el rendimiento.