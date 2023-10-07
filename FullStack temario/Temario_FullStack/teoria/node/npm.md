# NPM

Para instalar una librería en un proyecto con npm, se puede utilizar el siguiente comando desde la terminal:

```
npm install <nombre-de-la-librería>
```

Por ejemplo, si queremos instalar la librería `axios` que se utiliza para hacer peticiones HTTP, ejecutamos el siguiente comando:

```
npm install axios
```

Esto descarga la librería y la guarda en la carpeta `node_modules` del proyecto, así como también actualiza el archivo `package.json` con la información de la librería instalada. Dentro de `node_modules` se encuentran todas las dependencias que el proyecto tiene instaladas, incluyendo las que son dependencias de las propias librerías.

Un ejemplo de caso de uso podría ser el siguiente:

```javascript
const axios = require('axios');

axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.log(error);
  });
```

En este ejemplo, se utiliza la librería `axios` para hacer una petición GET a la API de JSONPlaceholder que retorna un objeto con información de un post del blog. Una vez que la petición es exitosa, se loguea el resultado en la consola de nuestro editor de código. Esta es una forma básica de cómo podemos utilizar una librería en nuestro proyecto.


Para instalar librerías en un proyecto de Node.js, normalmente se utiliza el administrador de paquetes de Node.js, `npm`. `npm` es un comando que funciona a través de la línea de comando de nuestro sistema operativo que permite buscar y descargar módulos Node.js de forma sencilla desde su repositorio oficial. Para instalar una librería de manera específica se utiliza el comando `npm install`. 

Por ejemplo, si queremos instalar el módulo `express` en nuestro proyecto de Node.js, podemos hacerlo ejecutando el siguiente comando desde la terminal:

```bash
npm install express
```

El comando anterior descargará el módulo `express` desde el repositorio de `npm` e instalará sus dependencias en nuestro proyecto, agregando la carpeta `node_modules` y un archivo `package-lock.json` (a partir de la versión 5.0 de `npm`) en la raíz del proyecto.

Por defecto, el comando `npm install` instala las librerías como dependencias del proyecto (con el flag `-S` o `--save`). Esto significa que las dependencias se agregarán automáticamente en el archivo `package.json`, en la sección `dependencies`. Podemos verificar esto en nuestro archivo `package.json`.

```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

Si queremos instalar una librería como dependencia de desarrollo (para que sea utilizada únicamente durante el desarrollo del proyecto y no como parte de la aplicación en sí), podemos utilizar el flag `-D` o `--save-dev`. Por ejemplo, si queremos instalar la librería `nodemon` como dependencia de desarrollo, ejecutamos:

```bash
npm install nodemon --save-dev
```

Igual que antes, esto descarga y se instala la librería `nodemon` y agrega sus dependencias al archivo `package-lock.json`. Sin embargo, esta vez la librería aparecerá en la sección `devDependencies` en el archivo `package.json`.

```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.7"
  }
}
```

Un caso de uso común se da cuando se quiere utilizar una librería de terceros para implementar una funcionalidad específica en nuestro proyecto. Por ejemplo, si queremos integrar un sistema de autenticación en nuestra aplicación web, podríamos utilizar una librería como `passport`.

```bash
npm install passport
```

También se puede instalar una librería a partir de un archivo local. Por ejemplo, si se necesita instalar la librería `my-package` ubicada en el directorio `../path/my-package`, se puede usar el siguiente comando:

```bash
npm install ../path/my-package
```

De esta forma se realiza la instalación de la librería `my-package` en el directorio de nuestro proyecto. También se puede utilizar un archivo `.tgz` para instalar una librería. Esto puede ser útil cuando se quiere instalar una versión específica de una librería.

```bash
npm install my-package-1.0.0.tgz
```

En resumen, instalar librerías en un proyecto de Node.js es una tarea sencilla utilizando el administrador de paquetes `npm`. El comando `npm install` es utilizado para instalar librerías específicas en el proyecto y se puede utilizar otros flags como `-S` o `-D` para especificar si una librería es una dependencia o dependencia de desarrollo.

## Referencias

- [npm](https://www.npmjs.com/)
- [npm install](https://docs.npmjs.com/cli/install)

