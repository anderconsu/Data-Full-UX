# Sesion en Node.js

Una sesión en un servidor de Node es una forma de almacenar información específica del usuario durante la interacción con una aplicación. Cuando un usuario interactúa con una aplicación web, el servidor de Node crea una sesión única para ese usuario y almacena la información que se necesita para personalizar la experiencia de usuario. 

Por ejemplo, si un usuario inicia sesión en una aplicación, se puede crear una sesión que asocie la información de inicio de sesión del usuario con la sesión. A medida que el usuario interactúa con la aplicación, se pueden almacenar en la sesión diferentes tipos de información personalizada, como productos agregados al carrito de compras o las páginas visitadas. En el caso de un carrito de compras, las sesiones son particularmente útiles porque permiten al usuario agregar varios artículos a la cesta y acceder a ella posteriormente desde cualquier página del sitio.

Otro caso de uso común de las sesiones en el servidor de Node es la gestión de autenticación. Cuando un usuario inicia sesión en una aplicación, se puede crear una sesión que almacene información sobre la cuenta del usuario. De esta forma, cuando el usuario navega por el sitio, sería reconocido y autorizado a realizar diferentes acciones o actividades.

En resumen, las sesiones son una forma de almacenar información del usuario y ofrecer una experiencia personalizada en las aplicaciones web. Algunos casos de uso en la vida real incluyen:

- Gestión de carrito de compra
- Gestión de autenticación de usuario y sesión
- Personalización de contenido basado en preferencias del usuario
- Almacenamiento de datos temporales en un formulario o formulario de solicitud de información.
- Uso de técnicas de seguimiento para promocionar actividades como campañas publicitarias.

Para crear una sesión en Node.js, es común usar librerías como Express o sessions. El siguiente código muestra un ejemplo simple de cómo crear una sesión en Express:

```javascript
const express = require('express');
const session = require('express-session');

const app = express();

app.use(session({
    secret: 'mysecretkey',
    resave: true,
    saveUninitialized: true
}));

app.get('/', (req, res) => {
    req.session.name = 'John'; //almacena un valor en sesión
    res.send('Session stored');
});

app.get('/getName', (req, res) => {
    if (req.session.name) {
        res.send(`The name is ${req.session.name}`); //recuperar el valor almacenado
    } else {
        res.send('No name stored');
    }
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});
```

---

## Referencias

- [Node.js Sessions](https://www.section.io/engineering-education/session-management-in-nodejs-using-expressjs-and-express-session/)
