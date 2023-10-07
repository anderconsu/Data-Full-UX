#  package.json

`package.json` es un archivo en formato JSON que se utiliza en aplicaciones Node.js para describir el proyecto, sus dependencias y metadatos asociados. Es la forma estándar de declarar las dependencias de un proyecto Node.js y sus configuraciones. 

El archivo `package.json` se crea automáticamente cuando se inicia un nuevo proyecto Node.js, y es importante para la instalación y gestión de las dependencias del proyecto. El archivo contiene campos que se utilizan para describir la información del proyecto, versiones de la aplicación, listas de dependencias, scripts de ejecución de tareas, información del autor y licencia, entre otros.

Aquí hay un ejemplo de cómo se ve el archivo `package.json` básico:

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My App Project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/user/my-app.git"
  },
  "author": "My Name",
  "license": "MIT"
}
```

- `"name"`: el nombre del proyecto.
- `"version"`: la versión actual del proyecto.
- `"description"`: una breve descripción del proyecto.
- `"main"`: el archivo principal de la aplicación.
- `"scripts"`: objeto que contiene scripts para ejecutar comandos. En este ejemplo, `"start"` ejecuta el script `"node index.js"`.
- `"repository"`: información de control de versiones del proyecto.
- `"author"`: el autor del proyecto.
- `"license"`: la licencia del proyecto.

El archivo `package.json` también se utiliza para declarar las dependencias y devDependencies del proyecto. Existen dos tipos de dependencias: las dependencias normales que se requieren para que el proyecto se ejecute correctamente, y las devDependencies que se requieren para desarrollar el proyecto.

Los paquetes pueden ser instalados usando npm, el gestor de paquetes de Node.js. Para instalar y guardar una nueva dependencia en el archivo `package.json`, se puede utilizar el comando `npm install <nombre-de-paquete> --save`. 

Por ejemplo, si se quisiera instalar el paquete Express y guardarlo como dependencia en el archivo `package.json`, se utilizaría el siguiente comando:

```bash
npm install express --save
```

El paquete Express se agregará a la sección `"dependencies"` del archivo `package.json`.

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "description": "My App Project",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/user/my-app.git"
  },
  "author": "My Name",
  "license": "MIT",
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

Es importante destacar que el archivo `package-lock.json` guarda la versión exacta de cada paquete y todas sus dependencias en el árbol de dependencias. Este archivo se utiliza para garantizar que se puedan generar instalaciones determinísticas del paquete, y también garantiza que el paquete funcione con la misma versión exacta de cada paquete y dependencia en todas las máquinas.

## Referencias

- [Node.js Package Manager](https://docs.npmjs.com/about-npm/)
- [package.json](https://docs.npmjs.com/files/package.json)
- [package-lock.json](https://docs.npmjs.com/files/package-lock.json)
