**CORS** (Cross-Origin Resource Sharing) es un mecanismo de seguridad que impide que un sitio web solicite recursos a otro dominio distinto al de origen. Para la comunicación entre sitios web se utilizan solicitudes HTTP que permiten a un cliente solicitar recursos a un servidor. CORS se aplica en el lado del cliente y del servidor para permitir que los recursos de un sitio web puedan ser utilizados desde otro dominio diferente.

En Node.js, CORS puede ser habilitado en el servidor mediante el uso de middlewares. En particular, se puede utilizar el paquete `cors` disponible en `npm` para permitir el acceso a recursos desde diferentes orígenes.

### Configuración básica

La configuración básica simplemente habilita CORS para todos los orígenes. En este caso, no es necesario especificar una lista blanca de los orígenes permitidos. El código siguiente muestra un ejemplo de como habilitar CORS en un servidor Node.js con Express y el paquete `cors`:

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

app.use(cors());
```

### Configurar un listado de dominios permitidos

Para limitar a qué dominios se permite el acceso, se puede pasar un objeto de opciones al middleware `cors`. En este objeto, se puede especificar una lista blanca de orígenes, métodos HTTP permitidos, encabezados personalizados y otros ajustes útiles. El siguiente ejemplo especifica dos orígenes permitidos, `http://localhost:3000` y `http://localhost:4000`, y un método HTTP permitido:

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

const corsOptions = {
  origin: ['http://localhost:3000', 'http://localhost:4000'],
  methods: ['GET', 'POST', 'PUT'],
  allowedHeaders: ['Content-Type', 'Authorization'],
};

app.use(cors(corsOptions));
```

### Configuración avanzada

También se pueden configurar otras opciones como los tiempos de vida (TTL) de las respuestas, personalizar el comportamiento en caso de errores, establecer la exposición de los encabezados y otras configuraciones avanzadas. Por ejemplo, el siguiente código muestra cómo configurar `cors` para que permita solicitudes de credenciales, establecer el TTL de la caché y personalizar el mensaje de error:

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

const corsOptions = {
  origin: '*',
  methods: ['GET', 'POST', 'PUT'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 3600,
  preflightContinue: false,
  optionsSuccessStatus: 204,
  exposedHeaders: ['Content-Length', 'X-Foo', 'X-Bar'],
  // listener function to handle origin policies
  origin: function (origin, callback) {
    if (origin === 'http://example.com') {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  // listener function to handle errors
  onError: function (err, req, res) {
    res.status(500).send({ error: 'Something went wrong', });
  }
};

app.use(cors(corsOptions));
``` 

En conclusión, las configuraciones de CORS en Node.js permiten controlar el acceso a los recursos de un servidor a través de diferentes orígenes y establecer los ajustes que mejor se adapten a las necesidades del proyecto.

---

