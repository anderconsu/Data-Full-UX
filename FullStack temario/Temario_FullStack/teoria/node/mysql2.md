# Mysql2 en Node

**mysql2** es una biblioteca de cliente MySQL para Node.js que se utiliza para interactuar con un servidor MySQL desde una aplicación Node.js. Proporciona una API simple y eficiente para conectarse a una base de datos MySQL, enviar consultas y recibir resultados.

Para instalar mysql2 en un proyecto de Node.js, ejecute el siguiente comando en la terminal:

```bash
npm install mysql2
```

La biblioteca mysql2 es una alternativa moderna y eficiente al paquete **mysql** ya que está escrito completamente en JavaScript y se basa en las últimas capacidades asincrónicas de Node.js, lo que resulta en un rendimiento y una eficiencia mejorados. Además, tiene soporte para consultas preparadas, lo que ayuda a mitigar ciertos problemas de seguridad como la inyección de SQL.

A continuación, se muestra un ejemplo de código básico para conectarse a una base de datos MySQL utilizando mysql2:

```javascript
const mysql = require('mysql2');

// Crear la conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydatabase'
});

// Establecer una consulta
const sql = 'SELECT * FROM users';

// Ejecutar la consulta
connection.query(sql, (error, results) => {
  if (error) {
    console.error(error);
  } else {
    console.log(results);
  }
});

// Cerrar la conexión
connection.end();
```

En este ejemplo, primero importamos el módulo mysql2 y luego creamos una conexión utilizando `createConnection()`. Pasamos los detalles de la conexión, como el host, el usuario, la contraseña y la base de datos que se utilizará.

Luego, definimos una consulta simple utilizando SQL que selecciona todos los registros de una tabla llamada "users". Usamos el método `query()` para ejecutar la consulta en la conexión. El método `query()` toma una función de devolución de llamada que maneja el resultado de la consulta. Si hay un error, lo mostramos en la consola. Si no hay errores, mostramos los resultados.

Finalmente, cerramos la conexión utilizando `end()` para liberar los recursos.

La biblioteca mysql2 también es muy útil para trabajar con consultas preparadas, que es una técnica para separar la consulta SQL de los datos proporcionados por el usuario. Esto ayuda a prevenir ataques de inyección de SQL. A continuación, se muestra un ejemplo de cómo usar consultas preparadas con mysql2:

```javascript
const mysql = require('mysql2');

// Crear la conexión
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydatabase'
});

// Configurar la consulta preparada
const sql = 'SELECT * FROM users WHERE username = ?';

// Datos proporcionados por el usuario
const username = 'john';

// Ejecutar la consulta preparada
connection.query(sql, [username], (error, results) => {
  if (error) {
    console.error(error);
  } else {
    console.log(results);
  }
});

// Cerrar la conexión
connection.end();
```

En este ejemplo, utilizamos el signo de interrogación (?) como marcador de posición en la consulta SQL. Luego, pasamos un array de valores a la función `query()` que coinciden con los marcadores de posición en el orden en que aparecen en la consulta SQL.

La biblioteca mysql2 también admite otras funcionalidades interesantes, como conexiones de piscina y promesas. Una conexión de piscina es un conjunto configurable de conexiones que se pueden reutilizar, lo que mejora el rendimiento de la aplicación. Por otro lado, el soporte para promesas permite usar promesas en lugar de callbacks para manejar los resultados de las consultas.

En resumen, mysql2 es una biblioteca popular y eficiente para interactuar con una base de datos MySQL desde una aplicación Node.js. Proporciona una API sencilla y moderna, soporte para consultas preparadas y otras funcionalidades útiles. Es una excelente opción para desarrolladores que trabajan con Node.js y MySQL.
## Pool

Una pool o piscina de conexiones en mysql2 se refiere a un conjunto de conexiones a la base de datos que se pueden compartir y reutilizar en una aplicación Node.js. En lugar de crear y cerrar conexiones individuales cada vez que se necesita interactuar con la base de datos, la piscina administra un grupo de conexiones abiertas y las administra de manera eficiente.

El uso de una piscina de conexiones tiene varias ventajas:

1. Mejora del rendimiento: Al reutilizar conexiones existentes en lugar de abrir y cerrar nuevas conexiones en cada interacción con la base de datos, se reduce la latencia y el tiempo de procesamiento, lo que lleva a una mejora general en el rendimiento de la aplicación.

2. Manejo de la concurrencia: En entornos de alto tráfico donde múltiples solicitudes pueden llegar simultáneamente, una piscina de conexiones puede administrar eficientemente las conexiones disponibles y garantizar que cada solicitud obtenga una conexión sin esperar o bloquear otras solicitudes.

3. Control de la carga: Una piscina de conexiones puede limitar el número máximo de conexiones abiertas a la base de datos. Esto ayuda a controlar la carga en el servidor de la base de datos y evita problemas de rendimiento debido a un exceso de conexiones.

A continuación se muestra un ejemplo de cómo crear y utilizar una piscina de conexiones en mysql2:

```javascript
const mysql = require('mysql2');

// Crear la piscina de conexiones
const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydatabase',
  connectionLimit: 10 // Límite de conexiones en la piscina
});

// Obtener una conexión de la piscina
pool.getConnection((error, connection) => {
  if (error) {
    console.error(error);
  } else {
    // Ejecutar una consulta utilizando la conexión
    connection.query('SELECT * FROM users', (error, results) => {
      if (error) {
        console.error(error);
      } else {
        console.log(results);
      }
      
      // Liberar la conexión de vuelta a la piscina
      connection.release();
    });
  }
});

// Cerrar la piscina de conexiones
pool.end();
```

En este ejemplo, primero importamos la biblioteca mysql2. Luego, creamos una piscina de conexiones utilizando el método `createPool()` y pasamos los detalles de la conexión, como el host, el usuario, la contraseña y la base de datos.

A continuación, utilizamos el método `getConnection()` para obtener una conexión de la piscina. Esto se realiza proporcionando una función de devolución de llamada que maneja la conexión obtenida. Dentro de la función de devolución de llamada, podemos ejecutar una consulta utilizando la conexión y manejar los resultados.

Después de terminar con la conexión, es importante liberarla utilizando el método `release()`. Esto asegura que la conexión se ponga de vuelta en la piscina y esté disponible para su reutilización por otras solicitudes.

Finalmente, cerramos la piscina de conexiones utilizando el método `end()`. Esto asegura que todas las conexiones se cierren adecuadamente cuando ya no sean necesarias.

En resumen, una piscina de conexiones en mysql2 proporciona una manera eficiente de administrar conexiones a la base de datos en una aplicación Node.js. Permite una reutilización y gestión adecuada de las conexiones, lo que mejora el rendimiento y el manejo de la concurrencia.
## Cierre de conexión

En un backend hecho en Node.js, generalmente es bueno cerrar la conexión de mysql2 cuando el servidor se detenga o se cierre la aplicación. Esto se puede hacer en el proceso de salida o en un evento de cierre del servidor.

Una manera común de asegurarse de que la conexión se cierre adecuadamente es utilizando el evento "beforeExit" del objeto `process`, el cual se dispara justo antes de que el proceso de Node.js se cierre.

Aquí tienes un ejemplo de cómo cerrar la conexión de mysql2 en un backend de Node.js utilizando el evento "beforeExit":

```javascript
const mysql = require('mysql2');

const pool = mysql.createPool({
  host: 'localhost',
  user: 'root',
  password: 'password',
  database: 'mydatabase',
  connectionLimit: 10
});

// Otros códigos relacionados con el backend...

// Evento "beforeExit" para cerrar la conexión al finalizar el programa
process.on('beforeExit', () => {
  pool.end();
});
```

En este ejemplo, creamos la piscina de conexiones `pool` utilizando `createPool()` como antes. Luego, utilizamos el evento "beforeExit" de `process` para escuchar cuándo el proceso de Node.js está a punto de cerrarse. Dentro del controlador del evento, llamamos al método `end()` de la piscina de conexiones para cerrar todas las conexiones.

De esta manera, podemos asegurarnos de que la conexión se cierre adecuadamente y evitemos dejar conexiones abiertas innecesariamente. Recuerda que cerrar la conexión es especialmente importante si la aplicación se ejecuta en un entorno de producción o en un servidor que está en funcionamiento continuo.