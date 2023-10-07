# Sakila

La base de datos Sakila es una base de datos de ejemplo creada por MySQL que está diseñada para mostrar la funcionalidad del motor de base de datos, así como también para proporcionar una herramienta de aprendizaje para aquellos que están aprendiendo SQL. La base de datos contiene información sobre una empresa de alquiler de películas y está dividida en varias tablas relacionales.

[Link de descarga](https://dev.mysql.com/doc/index-other.html)

Las tablas que componen la base de datos Sakila (con sus nombres en inglés) son:

1. **Actor**: Contiene información sobre los actores que actúan en las películas (actor_id, first_name, last_name, last_update).

2. **Address**: Contiene información sobre las direcciones de los clientes y las tiendas donde se alquilan las películas (address_id, address, address2, district, city_id, postal_code, phone, last_update).

3. **Category**: Contiene información sobre las categorías de las películas (category_id, name, last_update).

4. **City**: Contiene información sobre las ciudades donde se alquilan las películas (city_id, city, country_id, last_update).

5. **Country**: Contiene información sobre los países donde se alquilan las películas (country_id, country, last_update).

6. **Customer**: Contiene información sobre los clientes que alquilan las películas (customer_id, store_id, first_name, last_name, email, address_id, active, create_date, last_update).

7. **Film**: Contiene información sobre las películas disponibles para alquilar (film_id, title, description, release_year, language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update).

8. **FilmActor**: Contiene información sobre los actores que actúan en las películas (actor_id, film_id, last_update).

9. **FilmCategory**: Contiene información sobre las categorías de las películas (film_id, category_id, last_update).

10. **FilmText**: Contiene información sobre los textos de las películas (film_id, title, description).

11. **Inventory**: Contiene información sobre los inventarios disponibles en cada tienda (inventory_id, film_id, store_id, last_update).

12. **Language**: Contiene información sobre los idiomas utilizados en las películas (language_id, name, last_update).

13. **Payment**: Contiene información sobre los pagos realizados por los clientes (payment_id, customer_id, staff_id, rental_id, amount, payment_date, last_update).

14. **Rental**: Contiene información sobre los alquileres de películas realizados por los clientes (rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update).

15. **Staff**: Contiene información sobre el personal que trabaja en las tiendas (staff_id, first_name, last_name, address_id, email, store_id, active, username, password, last_update).

16. **Store**: Contiene información sobre las tiendas donde se alquilan las películas (store_id, manager_staff_id, address_id, last_update).

Las tablas están relacionadas entre sí por medio de claves foráneas. A continuación se describen las relaciones entre las tablas:

- **Actor** y **FilmActor**: Relación uno a muchos. Cada actor puede actuar en varias películas.
- **Film** y **FilmActor**: Relación uno a muchos. Cada película puede tener varios actores que actúen en ella.
- **Category** y **FilmCategory**: Relación uno a muchos. Cada categoría puede tener varias películas.
- **Film** y **FilmCategory**: Relación uno a muchos. Cada película puede tener varias categorías.
- **Film** y **FilmText**: Relación uno a uno. Cada película tiene un texto asociado.
- **Language** y **Film**: Relación uno a muchos. Cada idioma puede estar presente en varias películas.
- **Inventory** y **Film**: Relación uno a muchos. Cada inventario puede contener varias películas.
- **Store** y **Inventory**: Relación uno a muchos. Cada tienda puede tener varios inventarios.
- **Store** y **Staff**: Relación uno a muchos. Cada tienda puede tener varios miembros del personal.
- **Address** y **Customer**: Relación uno a muchos. Cada dirección puede tener varios clientes.
- **Address** y **Staff**: Relación uno a muchos. Cada dirección puede tener varias tiendas.
- **City** y **Address**: Relación uno a muchos. Cada ciudad puede tener varias direcciones.
- **Country** y **City**: Relación uno a muchos. Cada país puede tener varias ciudades.
- **Payment** y **Rental**: Relación uno a muchos. Cada pago puede estar vinculado a varios alquileres.
- **Customer** y **Payment**: Relación uno a muchos. Cada cliente puede tener varios pagos.
- **Staff** y **Payment**: Relación uno a muchos. Cada miembro del personal puede tener varios pagos.
- **Staff** y **Rental**: Relación uno a muchos. Cada miembro del personal puede tener varios alquileres.
- **Inventory**, **Rental** y **Customer**: Relación muchos a muchos. Cada alquiler y cada cliente pueden estar relacionados con varios inventarios. 

En resumen, la base de datos Sakila contiene información sobre actores, películas, clientes, inventarios, pagos, personal y tiendas, y sus relaciones se han diseñado para reflejar la complejidad del negocio de alquiler de películas.