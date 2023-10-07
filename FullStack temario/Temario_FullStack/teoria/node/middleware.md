
# Middleware

El middleware es una función o conjunto de funciones que procesan una respuesta HTTP antes de que el servidor la envíe al cliente. En otras palabras, es una capa de software que se sitúa entre la petición y la respuesta en el flujo de ejecución de Node.js.

Un middleware puede realizar una gran variedad de acciones en Node.js, tal como añadir datos a la respuesta, modificar la petición, realizar funciones de autorellenado de información entre otras.

Desde la versión 4 de ExpressJS, el uso de Middlewares es cada vez más intuitivo, por lo que puede ser extendido a casi cualquier acción que se desee realizar. Además, para facilitar su manejo, se han introducido comandos abreviados (use(), get(), post(), delete() etc).

Código de ejemplo:

```javascript
const express = require('express');
const app = express();

// Antes de la función middleware
app.use((req, res, next) => {
  console.log('Soy un middleware');
  next();
});

// Función middleware
app.get('/', (req, res, next) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Servidor web escuchando en el puerto 3000');
});
```

En este ejemplo, el app.use() es un middleware. Al solicitar cualquier ruta lo primero que va a hacer el servidor es ejecutar lo que se encuentra definido en el middleware y después ejecutará la siguiente acción en la cadena, que en este caso es la función que nos responde el "Hello World!".

Un caso de uso de los middlewares sería para verificar si el usuario está autenticado en una aplicación web, mediante sesión o mediante Token.

```javascript
// Middleware de autenticación
const authMiddleware = (req, res, next) => {
  const isAuth = ... // verificar si el usuario está autenticado

  if (isAuth) {
    next();
  } else {
    res.redirect('/login');
  }
}

// Ruta privada que solo puede acceder si el usuario está autenticado
app.get('/dashboard', authMiddleware, (req, res) => {
  res.send('Bienvenido al dashboard');
});
```

En este ejemplo, el middleware verifica si el usuario que desea acceder a la ruta está autenticado. Si lo está, se llama a la función next() que permite que la ruta definida como "/dashboard" sea procesada. Si no está, se redirige a la ruta "/login".




En conclusión, los middlewares son fundamentales en la arquitectura de una aplicación, su función es permitir ciertos permisos a los usuarios dependiendo de si cumplen con ciertos criterios de autenticación, permitiendo a su vez que el flujo de datos sea más seguro y así evitar la exposición de información innecesaria.


## Referencias

- [Middleware en ExpressJS](https://expressjs.com/es/guide/using-middleware.html)


