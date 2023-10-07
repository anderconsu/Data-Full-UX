# SUBQUERIES

Subqueries (también conocidas como consultas anidadas) en SQL son consultas dentro de otras consultas principales. Se utilizan para extraer datos de una tabla base, y luego usar los resultados de esa consulta para filtrar o limitar los resultados de la consulta principal.

Existen dos tipos de subqueries:
- Correlativas: que dependen de una tabla externa a la subquery.
- No correlativas: que pueden ejecutarse de manera independiente.

Ejemplo de subconsulta correlativa:
```sql
SELECT *
FROM orders
WHERE customer_id IN (SELECT customer_id FROM customers WHERE country = 'Mexico');
```

En este caso, la subconsulta depende de la tabla `customers` y se utiliza para limitar los resultados de la consulta principal en la tabla `orders`.

Ejemplo de subconsulta no correlativa:
```sql
SELECT *
FROM orders
WHERE order_date > (SELECT MAX(order_date) FROM orders) - 7;
```

En este caso, la subconsulta no tiene ninguna dependencia en una tabla externa y se utiliza para calcular una fecha límite que se usa para limitar los resultados de la consulta principal en la tabla `orders`.

Las subqueries son útiles en situaciones como:
- Consultas complejas donde se requiere filtrar en múltiples niveles o aplicar varias restricciones.
- Consultas que involucran cálculos complejos y subconjuntos de datos.
- Consultas que requieren resultados que no se pueden obtener con una simple consulta SELECT.

En resumen, las subqueries son un recurso importante y útil en SQL para procesar datos complejos y proporcionar respuestas incluyendo múltiples niveles de información.