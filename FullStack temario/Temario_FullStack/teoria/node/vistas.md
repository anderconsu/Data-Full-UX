# Vistas
Para crear vistas con Pug en Node.js y ES6 se debe seguir los siguientes pasos:

1. Descargar Pug y configurar el motor de vistas en el archivo principal de la aplicación.

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.set('views', './views');
app.set('view engine', 'pug');
```

2. Crear la carpeta "views" dentro del proyecto y dentro de ella crear archivos .pug con el formato que requieras.

```pug
html
  head
    title= title
  body
    h1= message
```

3. En el archivo en el cual quieras mostrar esta vista, hacer referencia a la esta pasando como parámetro el nombre del archivo pug creado.

```javascript
app.get('/', (req, res) => {
  res.render('index', { title: 'Inicio', message: 'Bienvenido a mi página' })
});
```

4. En la vista, para mostrar la variable que se ha pasado, se utiliza la notación de igual (“=”) seguida del nombre de la variable.

```pug
html
  head
    title= title
  body
    h1= message
```

Caso de uso: un caso típico donde se utiliza Pug es para generar contenido dinámico en una página web. Por ejemplo, supongamos que tenemos una página que muestra productos de una tienda. La información de los productos se encuentra en una base de datos y se debe mostrar en una tabla. En lugar de escribir el código HTML manualmente, podemos utilizar Pug para generar la tabla de manera dinámica según los productos que se encuentren en la base de datos.

Ejemplo de código:

```pug
table
  tr
    th Producto
    th Precio
  each product in products
    tr
      td= product.nombre
      td= product.precio
```
En este ejemplo, se muestra una tabla que muestra dos columnas: Producto y Precio. Además, se utiliza un bucle “each” para recorrer los productos y por cada producto se genera una fila en la tabla con sus respectivos datos. El identificador “product” se puede utilizar para acceder a los datos de cada producto y el punto (.) al final indica que los demás elementos deberán ir en el mismo nivel de indentación que el identificador. El igual (“=”) permite imprimir una variable en lugar de texto estático en la tabla. 

En conclusión, Pug es una herramienta muy útil y poderosa para generar vistas en Node.js con ES6, ya que permite generar contenido HTML de manera rápida y fácil utilizando Pug para generar partes dinámicamente sin tener que escribir todo el HTML manualmente.

## Referencias

- [Pug](https://pugjs.org/api/getting-started.html)
- [Pug - Tutorial](https://www.youtube.com/watch?v=kt3cEjjkCZA)

