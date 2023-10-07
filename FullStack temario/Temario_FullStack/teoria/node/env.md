# Variables de entorno en Node.js

Las variables de entorno en Node.js son valores que se pueden establecer fuera de la aplicación y que pueden ser accedidos desde cualquier lugar dentro de la misma. Las variables de entorno son útiles cuando se necesitan configuraciones específicas en entornos diferentes (por ejemplo, configuraciones de base de datos o credenciales API diferentes en un entorno de desarrollo y en un entorno de producción).

Para usar las variables de entorno en Node.js, se necesita una biblioteca llamada `dotenv`. Primero, se debe instalar `dotenv` como una dependencia en el proyecto:
````
npm install dotenv
````
Luego, se deben crear las variables de entorno en un archivo `.env` en la raíz de tu proyecto. Cada variable debe ser una asignación `clave=valor`, separada por una línea nueva. Por ejemplo:
````
DB_HOST=localhost
DB_USER=root
DB_PASS=mysecretpassword
````
Para acceder a las variables de entorno, se deben cargar en la aplicación en algún lugar cerca de la parte superior del archivo principal de la aplicación (por ejemplo, `app.js`). Para hacer esto, se debe llamar la función `config()` del paquete `dotenv` y asignar el resultado a una variable. Esto leerá las variables de entorno del archivo `.env` y las configurará para la aplicación:
````
const dotenv = require('dotenv');
dotenv.config();
````
Una vez cargadas las variables de entorno, se pueden acceder a ellas en cualquier lugar de la aplicación usando el objeto `process.env`. Por ejemplo, para acceder al valor de `DB_HOST`:
````
const dbHost = process.env.DB_HOST;
````
En resumen, las variables de entorno en Node.js se utilizan para establecer configuraciones específicas para diferentes entornos y se acceden a ellas usando el objeto `process.env`. El archivo `.env` que contiene estas variables debe estar en la raíz del proyecto y debe ser cargado en la aplicación usando la biblioteca `dotenv`.

---

