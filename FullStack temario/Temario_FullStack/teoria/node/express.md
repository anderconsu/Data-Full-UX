# Express

Express.js es un framework de Node.js que se utiliza para construir aplicaciones web y APIs de manera rápida y sencilla. Permite definir rutas, gestionar peticiones y respuestas HTTP, trabajar con plantillas, autenticación de usuarios, entre otras funcionalidades. 

### Instalación y uso básico

Para utilizar Express.js, primero es necesario instalarlo a través de npm:

```bash
npm install express
```

Para crear una aplicación sencilla con Express.js, se debe requerir el módulo y llamar a la función `express()`.

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('¡Hola Mundo!');
});

// Escuchando el servidor en el puerto 3000
app.listen(3000, () => console.log('Servidor en puerto 3000'));
```

En el ejemplo anterior, se crea una aplicación de Express.js y se define la ruta principal `/` utilizando el verbo HTTP GET. Cuando se accede a esa ruta, se envía al cliente la respuesta `¡Hola Mundo!`. También se inicia el servidor de forma que quede a la escucha de peticiones HTTP en el puerto `3000`.

### Rutas

Express.js utiliza la función `app.MÉTODO(PATH, MANEJADOR)` para definir rutas en una aplicación. Donde "MÉTODO" es un verbo HTTP como `get`, `post`, `put`, `delete`, `use`, `all`, etc.; "PATH" es un string que define la ruta; y "MANEJADOR" es una función que se ejecuta cuando llega una petición HTTP a esa ruta.

```javascript
app.get('/', (req, res) => {
  res.send('¡Hola Mundo!');
});

app.post('/usuarios', (req, res) => {
  res.send('Usuario creado correctamente');
});

app.delete('/usuarios/:id', (req, res) => {
  const { id } = req.params;
  res.send(`Usuario con ID ${id} eliminado correctamente`);
});
```

En el ejemplo anterior se definen tres rutas diferentes en nuestra aplicación. La primera responde a una petición GET a la ruta `/` y envía el mensaje "¡Hola Mundo!" como respuesta. La segunda responde a una petición POST a la ruta `/usuarios` y envía un mensaje indicando que el usuario ha sido creado. La tercera, por su parte, responde a una petición DELETE a una ruta dinámica `/usuarios/:id` donde ":id" es un parámetro que se enviará en la URL y lo usaremos para eliminar el usuario correspondiente.

### Middleware

Los middleware son funciones que se ejecutan antes que otras funciones al solicitar una ruta en nuestra aplicación. Funcionan como intermediarios entre el cliente y el servidor y nos permiten añadir funcionalidades a nuestras rutas como autenticación, control de errores, comprensión de archivos JSON, entre otras.

Para utilizar un middleware se debe utilizar la función `app.use(MIDDLEWARE)` colocando la función del middleware como parámetro.

```javascript
app.use(logger);

function logger(req, res, next) {
  console.log(`Petición recibida en la ruta ${req.url}`);
  next();
}
```

En el ejemplo anterior, se ha creado un middleware `logger` que es registrado en nuestra aplicación utilizando la función `app.use`. Cuando se accede a una ruta, este middleware muestra por consola la ruta accedida y pasa el control a la siguiente función utilizando el parámetro `next()`. 

### Plantillas

Express.js también permite trabajar con plantillas de HTML, lo que nos permite crear páginas web dinámicas renderizando información en el servidor. Para trabajar con plantillas, debemos instalar una plantilla de nuestro gusto, como Pug (antes conocido como Jade), Handlebars, EJS, etc.

Para utilizar una plantilla se debe requerir el módulo y definir la ruta de la carpeta donde estarán almacenados los ficheros de las plantillas. A continuación, se utiliza la función `res.render` para renderizar la plantilla que deseamos enviar al cliente.

```javascript
const express = require('express');
const app = express();

// Definimos la carpeta de las plantillas
app.set('views', './views');
// Definimos el motor de renderizado, en este caso Pug
app.set('view engine', 'pug');

app.get('/', (req, res) => {
  res.render('index', { title: 'Página de inicio', message: '¡Hola mundo!' });
});

app.listen(3000, () => console.log('Servidor en puerto 3000'));
```

En el ejemplo anterior, hemos definido que las plantillas estén ubicadas en la carpeta `/views` y utilizamos Pug como motor de renderización. Cuando se accede a la ruta `/` se renderiza la plantilla `index` y se pasa un objeto con datos para renderizar.

### Casos de uso

Express.js es muy utilizado en la construcción de aplicaciones web y APIs RESTful, entre otros casos de uso:

- Creación de aplicaciones web que se comuniquen con una base de datos.
- Creación de APIs RESTful seguras que autentiquen usuarios y gestionen permisos.
- Creación de aplicaciones SPA (Single Page Applications) utilizando frameworks en el frontend y comunicándose con Express.js mediante AJAX.

