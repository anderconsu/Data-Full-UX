
1. Listar el nombre y apellido de todos los actores en orden alfabético ascendente, primero por apellido y luego por nombre.
```sql
SELECT first_name, last_name
FROM actor
ORDER BY last_name ASC, first_name ASC;
```

2. Listar el nombre y dirección de los clientes que viven en Barcelona.
```sql
SELECT customer.first_name, customer.last_name, address.address, city.city
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city = 'Barcelona';
```

3. Mostrar el título, descripción y duración de todas las películas ordenadas por duración de mayor a menor.
```sql
SELECT title, description, length
FROM film
ORDER BY length DESC;
```

4. Mostrar el título, año de lanzamiento, costo y precio de alquiler de todas las películas que tengan un costo mayor a 20 y un precio de alquiler mayor a 2.
```sql
SELECT title, release_year, rental_rate, rental_price
FROM film
WHERE rental_price > 2 AND replacement_cost > 20;
```

5. Mostrar el nombre del actor, título de la película y categorías de todas las películas en las que una actriz llamada "Penelope" ha actuado.
```sql
SELECT actor.first_name, actor.last_name, film.title, category.name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
JOIN film_category ON film_actor.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'Penelope';

```

6. Mostrar el número de veces que cada película ha sido alquilada y ordenarlos de mayor a menor.
```sql
SELECT film.title, COUNT(rental.rental_id) AS num_rentals
FROM film
JOIN inventory ON film.film_id = inventory.film_id
JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title
ORDER BY num_rentals DESC;
```

7. Mostrar la cantidad total de ingresos generados por cada tienda de alquiler de películas.
```sql

SELECT staff.first_name, staff.last_name, SUM(payment.amount) AS total_income
FROM staff
JOIN store ON staff.store_id = store.store_id
JOIN customer ON store.store_id = customer.store_id
JOIN rental ON customer.customer_id = rental.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
GROUP BY staff.first_name, staff.last_name;
```

8. Mostrar los cinco actores que más han aparecido en películas y su número de apariciones.
```sql
SELECT actor.first_name, actor.last_name, COUNT(film_actor.film_id) AS num_films
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
GROUP BY actor.first_name, actor.last_name
ORDER BY num_films DESC
LIMIT 5;
```

9. Mostrar la cantidad total de dinero gastado por cada cliente en alquiler de películas.
```sql
SELECT customer.first_name, customer.last_name, SUM(payment.amount) AS total_amount
FROM customer
JOIN rental ON customer.customer_id = rental.customer_id
JOIN payment ON rental.rental_id = payment.rental_id
GROUP BY customer.first_name, customer.last_name;
```

10. Listar el título de las cinco películas menos alquiladas.
```sql
SELECT film.title, COUNT(rental.rental_id) AS num_rentals
FROM film
LEFT JOIN inventory ON film.film_id = inventory.film_id
LEFT JOIN rental ON inventory.inventory_id = rental.inventory_id
GROUP BY film.title
ORDER BY num_rentals ASC
LIMIT 5;
```

11. Listado de los actores que más han actuado en películas de acción ordenados de mayor a menor cantidad de películas.

```sql
SELECT actor.actor_id, actor.first_name, actor.last_name, COUNT(*) as cantidad_peliculas
FROM actor
INNER JOIN film_actor ON actor.actor_id = film_actor.actor_id
INNER JOIN film ON film.film_id = film_actor.film_id
INNER JOIN film_category ON film_category.film_id = film.film_id
INNER JOIN category ON category.category_id = film_category.category_id
WHERE category.name = "Action"
GROUP BY actor.actor_id
ORDER BY cantidad_peliculas DESC;
```
12. Lista de películas cuya duración sea mayor a 2 horas (120 minutos) y que su clasificación sea igual a "PG-13" o "R".


```sql
SELECT film.title, film.description, film.length, film.rating
FROM film
WHERE film.length > 120 AND film.rating IN ("PG-13", "R");

```

13. Obtener el nombre de los actores que han trabajado en una película con un actor de apellido "Cruz".

```sql
SELECT DISTINCT a2.first_name, a2.last_name
FROM actor a1
INNER JOIN film_actor fa1 ON a1.actor_id = fa1.actor_id
INNER JOIN film f1 ON f1.film_id = fa1.film_id
INNER JOIN film_actor fa2 ON f1.film_id = fa2.film_id
INNER JOIN actor a2 ON a2.actor_id = fa2.actor_id
WHERE a1.last_name = "Cruz";
```