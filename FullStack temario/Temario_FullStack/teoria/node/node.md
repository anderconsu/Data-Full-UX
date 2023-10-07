# Node.js

Node.js es un entorno de tiempo de ejecución JavaScript construido sobre el motor V8 de Google Chrome. Node.js utiliza un modelo de E/S sin bloqueo y orientado a eventos, lo que lo hace muy eficiente y escalable. 

Con Node.js, se puede crear aplicaciones de servidor de alto rendimiento utilizando JavaScript en el lado del servidor. Algunas de las características más importantes de Node.js incluyen:

- Velocidad
- Escalabilidad
- No bloqueante
- Modular
- Multiplataforma

## npm
`npm` es el administrador de paquetes de Node.js y permite descargar e instalar módulos de terceros para ser utilizados en nuestras aplicaciones. 

Los paquetes npm pueden ser instalados a través del terminal usando el siguiente comando: 

```
$ npm install <nombre_del_paquete>
```

Los paquetes también pueden ser incluidos en el archivo `package.json` y automáticamente instalados en el proyecto con el comando:

```
$ npm install
```

## Express
`Express` es un framework popular de Node.js que se utiliza para construir aplicaciones web. Con Express, podemos crear controladores de ruta para manejar las solicitudes de los clientes y retornar respuestas. 

Un ejemplo básico de un servidor web en express sería el siguiente: 

```javascript
const express = require('express'); 
const app = express();

app.get('/', function (req, res) { //Crea una ruta envíando una respuesta
  res.send('Hola, mundo!');
});

app.listen(3000, function () { // Crea el servidor en el puerto 3000
  console.log('Example app listening on port 3000!');
});
```

## Endpoints
Un endpoint es el término utilizado para describir la extremidad de una operación. En el contexto de una API web, el endpoint es el punto final de una solicitud a un servidor web. 

Por ejemplo, si tuviéramos un endpoint `/usuarios`, un cliente puede enviar una solicitud GET a `https://miapi.com/usuarios` y recibir una lista de usuarios como respuesta. 

Para crear un endpoint en Express, simplemente usamos uno de los métodos de direccionamiento de ruta. Por ejemplo, para definir una ruta de endpoint `/usuarios`, podríamos hacer lo siguiente:

```javascript
const express = require('express'); 
const app = express();

app.get('/usuarios', function (req, res) { 
  // Manejar la solicitud de los usuarios
  res.send('Aquí se muestran los usuarios');
});

app.listen(3000, function () { 
  console.log('Example app listening on port 3000!');
});
```

Uno de los casos de uso más comunes para endpoints es en la creación de APIs. Los endpoints pueden ser utilizados para manejar solicitudes de clientes y retornar respuestas en diferentes formatos, como JSON y XML.

# Referencias

- [Node.js](https://nodejs.org/es/about)
- [Express](https://www.tutorialspoint.com/nodejs/nodejs_express_framework.htm)

