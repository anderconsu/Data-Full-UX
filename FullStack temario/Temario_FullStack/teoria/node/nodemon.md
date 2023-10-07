# Nodemon

**Nodemon** es una herramienta de línea de comandos para desarrolladores de Node.js que monitorea cambios en el código fuente y automáticamente reinicia su servidor cuando se detecta algún cambio.

Esto significa que no es necesario detener y reiniciar manualmente el servidor cada vez que se haga algún cambio en el código. Esto ahorra tiempo y hace el proceso de desarrollo más eficiente.

Para instalar nodemon a nivel global, basta con ejecutar el siguiente comando en la consola de comandos:

```bash
npm install -g nodemon
```

Una vez instalado, en lugar de ejecutar `node` para correr nuestro servidor Node.js, ejecutaremos la siguiente línea de comandos:

```bash
nodemon archivo.js
```

Por ejemplo, para ejecutar un archivo de servidor web con Express, podemos escribir lo siguiente en la línea de comandos:

```bash
nodemon app.js
```

Además, también podemos agregar algunos argumentos para personalizar la forma en que nodemon se comporta. Por ejemplo, para hacer que nodemon ignore algunos archivos o carpetas, podemos utilizar el siguiente comando:

```bash
nodemon --ignore carpeta1/ --ignore carpeta2/ app.js
```

También podemos utilizar nodemon con archivos de configuración en `package.json`. En el archivo `package.json`, añadimos un nuevo objeto llamado `"nodemonConfig"` y establecemos las opciones que queramos. Por ejemplo, aquí tenemos un ejemplo en el que nodemon ignora archivos de prueba y realiza la monitorización cada vez que hay un cambio:

```json
{
  "name": "mi-proyecto",
  "version": "1.0.0",
  "main": "app.js",
  "nodemonConfig": {
    "ignore": [
      "test/*"
    ],
    "watch": [
      "src"
    ]
  },
  "dependencies": {
    "express": "^4.17.1"
  }
}
```

En resumen, nodemon es una herramienta muy útil para desarrolladores de Node.js ya que les permite mantener su servidor ejecutándose automáticamente mientras hacen cambios en el código fuente con la finalidad de agilizar el proceso de desarrollo y testeo de aplicaciones.

## Referencias
- [Nodemon](https://nodemon.io/)
