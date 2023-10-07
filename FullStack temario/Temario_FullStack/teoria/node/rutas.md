# Rutas


Las rutas en Express.js son las URL que nuestros usuarios utilizarán para acceder a nuestra aplicación o API. La gestión de rutas se encarga de asociar una función o un controlador a una URL determinada. Una vez que el usuario accede a esa URL, la función o controlador correspondiente será ejecutado.

Para gestionar rutas en Express.js, utilizamos el método `app.get()` o uno de los siguientes métodos: `app.post()`, `app.put()`, `app.patch()`, `app.delete()`.

El método `app.get()` gestiona una petición HTTP GET y la función asociada se ejecutará cuando un usuario accede a la URL correspondiente.

```javascript
app.get('/ruta', function(req, res) {
  res.send('Hola mundo!');
});
```

En el ejemplo anterior, cuando un usuario acceda a la URL `/ruta` se ejecutará la función y se devolverá la respuesta `Hola mundo!`.

El método `app.post()` gestiona una petición HTTP POST y la función asociada se ejecutará cuando un usuario envíe un formulario o una petición fetch con el método POST.

```javascript
app.post('/ruta', function(req, res) {
  console.log('Datos enviados:', req.body);
  res.send('Datos recibidos!');
});
```

En el ejemplo anterior, cuando un usuario envíe un formulario o una petición fetch con el método POST a la URL `/ruta`, se ejecutará la función y se imprimirán los datos recibidos en la consola del servidor.

El método `app.put()` gestiona una petición HTTP PUT y la función asociada se ejecutará cuando un usuario envíe una petición con el método PUT.

```javascript
app.put('/ruta/:id', function(req, res) {
  console.log('ID:', req.params.id);
  console.log('Datos enviados:', req.body);
  res.send('Datos actualizados!');
});
```

En el ejemplo anterior, cuando un usuario envíe una petición con el método PUT a la URL `/ruta/:id`, se ejecutará la función y se imprimirán el ID y los datos recibidos en la consola del servidor.

El método `app.patch()` gestiona una petición HTTP PATCH y la función asociada se ejecutará cuando un usuario envíe una petición con el método PATCH.

```javascript
app.patch('/ruta/:id', function(req, res) {
  console.log('ID:', req.params.id);
  console.log('Datos enviados:', req.body);
  res.send('Datos actualizados!');
});
```

El método `app.delete()` gestiona una petición HTTP DELETE y la función asociada se ejecutará cuando un usuario envíe una petición con el método DELETE.

```javascript
app.delete('/ruta/:id', function(req, res) {
  console.log('ID:', req.params.id);
  res.send('Datos eliminados!');
});
```

En el ejemplo anterior, cuando un usuario envíe una petición con el método DELETE a la URL `/ruta/:id`, se ejecutará la función y se imprimirá el ID en la consola del servidor.

En resumen, la gestión de rutas con Express.js es muy sencilla y permite asociar funciones o controladores a las URLs de nuestra aplicación o API. Con los métodos `app.get()`, `app.post()`, `app.put()`, `app.patch()` y `app.delete()`, podemos manejar diferentes tipos de peticiones y generar respuestas personalizadas para cada una de ellas.


## Parámetros de ruta

Los parámetros de ruta son valores que se pasan a través de la URL. Por ejemplo, si tenemos una ruta `/ruta/:id`, el valor de `id` se puede pasar a través de la URL. Por ejemplo, si accedemos a la URL `/ruta/123`, el valor de `id` será `123`.

Para acceder a los parámetros de ruta, utilizamos el objeto `req.params` que se pasa como parámetro a la función asociada a la ruta.

```javascript
app.get('/ruta/:id', function(req, res) {
  console.log('ID:', req.params.id);
  res.send('Hola mundo!');
});
```

En el ejemplo anterior, cuando un usuario acceda a la URL `/ruta/123`, se ejecutará la función y se imprimirá el ID en la consola del servidor.

## Parámetros de consulta

Los parámetros de consulta son valores que se pasan a través de la URL. Por ejemplo, si tenemos una ruta `/ruta`, podemos pasar un parámetro de consulta a través de la URL. Por ejemplo, si accedemos a la URL `/ruta?nombre=John`, el valor de `nombre` será `John`.

Para acceder a los parámetros de consulta, utilizamos el objeto `req.query` que se pasa como parámetro a la función asociada a la ruta.

```javascript
app.get('/ruta', function(req, res) {
  console.log('Nombre:', req.query.nombre);
  res.send('Hola mundo!');
});
```

En el ejemplo anterior, cuando un usuario acceda a la URL `/ruta?nombre=John`, se ejecutará la función y se imprimirá el nombre en la consola del servidor.

## Parámetros de cuerpo

Los parámetros de cuerpo son valores que se pasan a través de la petición HTTP. Por ejemplo, si tenemos una ruta `/ruta` y enviamos un formulario con el método POST, los datos del formulario se enviarán como parámetros de cuerpo.

Para acceder a los parámetros de cuerpo, utilizamos el objeto `req.body` que se pasa como parámetro a la función asociada a la ruta.

```javascript
app.post('/ruta', function(req, res) {
  console.log('Datos enviados:', req.body);
  res.send('Datos recibidos!');
});
```

En el ejemplo anterior, cuando un usuario envíe un formulario con el método POST a la URL `/ruta`, se ejecutará la función y se imprimirán los datos recibidos en la consola del servidor.

## Rutas anidadas

Las rutas anidadas son rutas que se definen dentro de otras rutas. Por ejemplo, si tenemos una ruta `/ruta` y queremos definir una ruta `/ruta/subruta`, podemos definir la ruta `/ruta/subruta` dentro de la ruta `/ruta`.

```javascript
app.get('/ruta', function(req, res) {
  res.send('Hola mundo!');
});

app.get('/ruta/subruta', function(req, res) {
  res.send('Hola mundo!');
});
```

En el ejemplo anterior, cuando un usuario acceda a la URL `/ruta`, se ejecutará la función asociada a la ruta `/ruta` y se imprimirá `Hola mundo!` en la pantalla. Cuando un usuario acceda a la URL `/ruta/subruta`, se ejecutará la función asociada a la ruta `/ruta/subruta` y se imprimirá `Hola mundo!` en la pantalla.



## Organización de rutas anidadas en Express.js

Para organizar rutas anidadas en Express.js, primero debemos dividir las rutas en diferentes archivos y luego requerirlos desde un archivo principal. Los sub-archivos de ruta se pueden llamar según su función (ejemplo: `auth.js` para manejar la autorización, `product.js` para manejar las operaciones de productos, etc.) y se pueden alojar en una carpeta denominada `routes`. También se pueden dividir las rutas según la versión del API o según la funcionalidad.

La organización de rutas anidadas se realiza mediante el método `router()` proporcionado por Express.js. Podemos crear un enrutador utilizando el método `router()` y luego utilizar ese enrutador para manejar todas las rutas relacionadas con una funcionalidad específica. Por ejemplo, si tenemos las rutas `/products/list`, `/products/create`, `/products/update` y `/products/delete`, podemos crear una ruta raíz llamada `products.js` y manejar todas estas rutas en esa ruta raíz utilizando el método `router()`.

Aquí hay un ejemplo básico de cómo podemos organizar rutas anidadas en Express.js:

### Archivo principal de la aplicación `app.js`
```javascript
const express = require('express');
const app = express();
const productsRoutes = require('./routes/products');
const userRoutes = require('./routes/user');

app.use('/api/products', productsRoutes);
app.use('/api/user', userRoutes);

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});
```
En este ejemplo, hemos requerido dos archivos de rutas `products.js` y `user.js` y los hemos montado en sus respectivas rutas base `/api/products` y `/api/user` utilizando el método `use()` de Express.js.

### Archivo de rutas del producto `routes/products.js`
```javascript
const express = require('express');
const router = express.Router();

router.get('/list', (req, res) => {
    res.send('List of products');
});

router.post('/create', (req, res) => {
    res.send('Create a new product');
});

router.put('/update/:id', (req, res) => {
    res.send('Update a product with id ' + req.params.id);
});

router.delete('/delete/:id', (req, res) => {
    res.send('Delete a product with id ' + req.params.id);
});

module.exports = router;
```
En este archivo, hemos creado un objeto de enrutador utilizando el método `Router()` de Express.js y definido las diferentes rutas para manejar la lista, la creación, la actualización y la eliminación de productos. Hemos exportado este objeto de enrutador para usarlo en el archivo principal de la aplicación

### Archivo de ruta del usuario `routes/user.js`
```javascript
const express = require('express');
const router = express.Router();

router.get('/profile', (req, res) => {
    res.send('User profile');
});

router.post('/register', (req, res) => {
    res.send('User registration');
});

router.post('/login', (req, res) => {
    res.send('User login');
});

router.get('/logout', (req, res) => {
    res.send('User logout');
});

module.exports = router;
```
En este archivo, hemos creado un objeto de enrutador utilizando el método `Router()` de Express.js y definido las diferentes rutas para manejar el perfil, el registro, el inicio de sesión y la salida de usuario. Hemos exportado este objeto de enrutador para usarlo en el archivo principal de la aplicación.

## Ejemplo de caso de uso

Supongamos que estamos creando una aplicación para una tienda en línea que permite a los usuarios buscar productos, agregar productos a un carrito de compras y realizar un pedido. Podemos dividir las rutas en diferentes archivos según la funcionalidad y organizarlas anidadas de la siguiente manera:
- `auth.js` para manejar la autorización de usuarios
- `product.js` para manejar las operaciones de productos
   - `product_category.js` para manejar las categorías del producto
- `cart.js` para manejar las operaciones del carrito
- `order.js` para manejar las órdenes de los usuarios

Podemos crear un enrutador raíz en cada archivo de rutas y organizarlo jerárquicamente. Por ejemplo, podemos crear las siguientes rutas:
- `/auth` para manejar la autorización (registro, inicio de sesión y salida)
- `/products` para listar productos, crear nuevos productos, actualizar productos y eliminar productos.
- `/products/categories` para listar categorías, crear nuevas categorías, actualizar categorías y eliminar categorías
- `/cart` para agregar productos al carrito, eliminar productos del carrito y listar los productos en el carrito.
- `/order` para crear un pedido, mostrar detalles del pedido, listar los pedidos.

En conclusion, la organización de rutas anidadas es una forma efectiva de organizar rutas y modularizar la aplicación. Permite una mayor escalabilidad, mantenimiento y limpieza del código.

## Referencias

-[Routing](https://expressjs.com/en/guide/routing.html)
-[Router](https://expressjs.com/en/4x/api.html#router)