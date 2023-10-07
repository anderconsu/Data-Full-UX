# Documentación

La documentación con jsDoc es una técnica utilizada en JavaScript para documentar el código de un proyecto de forma clara y concisa. jsDoc se basa en etiquetas que se colocan encima de las funciones, métodos y variables del código que se quieren documentar. Estas etiquetas permiten especificar los propósitos, parámetros, valores de retorno y otros elementos relevantes en la documentación del código.

En términos generales, las etiquetas jsDoc se escriben como fragmentos de código JavaScript, y se colocan encima de la declaración de una variable o función. Los comentarios que se incluyen dentro de estas etiquetas se utilizan para proporcionar información adicional sobre el elemento que se está documentando.

Ejemplo de etiqueta jsDoc:

```js
/**
 * Suma dos números y devuelve el resultado.
 * @param {number} a - El primer número que se va a sumar.
 * @param {number} b - El segundo número que se va a sumar.
 * @returns {number} - El resultado de la suma de a y b.
 */
function sumar(a, b) {
  return a + b;
}
```

El ejemplo anterior muestra una función llamada `sumar` que realiza una suma matemática simple de dos números. En esta función, se han utilizado etiquetas jsDoc para documentar el propósito de la función, los parámetros que necesita para funcionar y el valor que devuelve.

Algunas de las etiquetas jsDoc más comunes son:

- `@param` - Documenta los parámetros de una función o método.
- `@returns` - Documenta el valor de retorno de una función o método.
- `@throws` - Documenta las excepciones que pueden ser lanzadas por una función o método.
- `@class` - Documenta la clase que representa un objeto.
- `@property` - Documenta las propiedades de un objeto.

Los casos de uso más comunes para la documentación con jsDoc son:

- Facilitar el mantenimiento del código: La documentación clara y concisa de un código hace que sea más sencillo de entender y de mantener. Cuando alguien tiene que trabajar en un proyecto ajeno, la documentación reduce drásticamente el tiempo necesario para comprender su funcionamiento y detectar errores.

- Ayudar a otros desarrolladores: Cuando un proyecto es de código libre, hay veces en las que es imposible llegar a todos los usuarios que utilizan el código. La documentación del código ayuda a los desarrolladores que están utilizando tu código sin tener que contactarte.

En resumen, la documentación con jsDoc es un método efectivo para documentar el código de un proyecto, ya que permite a los desarrolladores comprender rápidamente el propósito y la funcionalidad de una función o método. Además, mejora la mantenibilidad del código y ayuda a otros a entender y utilizar el código según las necesidades específicas de sus proyectos.

Para crear un archivo de configuración para jsDoc, primero debemos tener instalado jsDoc en nuestro proyecto de Node.js. Para instalar jsDoc, debemos abrir una terminal en la carpeta del proyecto y escribir el siguiente comando:

```
npm install jsdoc --save-dev
```

Este comando instalará jsDoc y lo registrará como una dependencia de desarrollo en el archivo `package.json` del proyecto.

Para crear el archivo de configuración de jsDoc, debemos crear un archivo llamado `jsdoc.json` en la raíz del proyecto y agregar las opciones de configuración necesarias. El archivo de configuración de jsDoc es un archivo JSON que contiene pares clave-valor que definen las opciones de configuración de jsDoc. Algunas opciones de configuración comunes son:

- **source**: Ruta o archivo donde se encuentra el código fuente que se quiere documentar.
- **destination**: Ruta o carpeta donde se guardará la documentación generada por jsDoc.
- **plugins**: Lista de plugins que se utilizarán para generar la documentación. Los plugins son módulos de Node.js que proporcionan funcionalidad adicional a jsDoc.

Aquí hay un ejemplo de un archivo de configuración jsdoc.json básico:

```json
{
  "source": {
    "include": ["./src"],
    "exclude": ["./src/ignored"],
    "includePattern": ".+\.js(doc|x)?$"
  },
  "plugins": [
    "plugins/markdown"
  ],
  "opts": {
    "destination": "./docs",
    "recurse": true
  }
}
```

En este ejemplo, la opción `source` incluye todos los archivos `.js` y `.jsdoc` que se encuentran en la carpeta `./src` del proyecto, pero excluye los archivos en la subcarpeta `./src/ignored`. La opción `plugins` utiliza el plugin `markdown` para permitir la inclusión de Markdown en la documentación generada. La opción `opts` define la carpeta donde se guardará la documentación en el subdirectorio `./docs`.

Para generar la documentación con jsDoc, desde la linea de comandos dentro de la carpeta de nuestro proyecto, ejecutamos el comando:

```
npx jsdoc -c jsdoc.json
```

Este comando generará la documentación en la carpeta especificada en la opción `destination` del archivo de configuración `jsdoc.json`.

En resumen, la creación de un archivo de configuración para jsDoc es un proceso sencillo que se lleva a cabo creando un archivo JSON y definiendo las opciones de configuración adecuadas. Una vez definido, podemos generar el archivo de documentación mediante el comando `npx jsdoc -c jsdoc.json` en la terminal.

Para poder documentar las partes privadas del código en la documentación generada por jsDoc, debemos agregar la opción `private` al archivo de configuración. Esta opción nos permite indicar a jsDoc que se documenten también las partes privadas del código.

Aquí hay un ejemplo actualizado del archivo `jsdoc.json` que incluye la opción `private`:

```json
{
  "source": {
    "include": ["./src"],
    "exclude": ["./src/ignored"],
    "includePattern": ".+\.js(doc|x)?$"
  },
  "plugins": [
    "plugins/markdown"
  ],
  "opts": {
    "destination": "./docs",
    "recurse": true
  },
  "private": true
}
```

En este ejemplo, la opción `private` está establecida en `true`, lo que indica que jsDoc debe documentar también las partes privadas del código.

Con esta opción habilitada, cuando se ejecute el comando para generar la documentación, jsDoc incluirá la documentación de todas las partes públicas y privadas en el archivo de salida.

Es importante tener en cuenta que documentar las partes privadas puede ser útil para mejorar la comprensión del código y su mantenimiento, pero también puede generar exposición de datos que no queremos hacer visibles a la comunidad. Por lo tanto, es recomendable usar la opción `private` con precaución y solo en aquellos casos en que es necesario proporcionar documentación detallada para un proyecto interno o solo para un grupo de desarrolladores autorizados.