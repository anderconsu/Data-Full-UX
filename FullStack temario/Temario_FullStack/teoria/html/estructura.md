  
  # Estructura HTML

La estructura HTML (HyperText Markup Language o Lenguaje de Marcado de Hipertexto, en español) es la base sobre la que se construyen las páginas web. HTML es un lenguaje de marcado que se utiliza para estructurar y mostrar el contenido en un navegador web.

La estructura básica de una página HTML es la siguiente:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Título de la página</title>
  </head>
  <body>
    Contenido de la página
  </body>
</html>
```

Veamos en detalle cada una de las partes:

- `<!DOCTYPE html>`: Se utiliza para indicar el tipo de documento que vamos a utilizar. En este caso, estamos utilizando HTML5.

- `<html>`: La etiqueta `html` es la etiqueta principal que envuelve todo el contenido de la página.

- `<head>`: La etiqueta `head` se utiliza para incluir información importante sobre la página, como pueden ser las etiquetas `meta` para especificar el lenguaje o la descripción de la página, o en este caso, `<title>` para establecer el título que aparecerá en la pestaña del navegador.

- `<body>`: La etiqueta `body` es la que contiene todo el contenido de la página que queremos mostrar en el navegador.

Dentro del `body` podemos utilizar otras etiquetas HTML para estructurar el contenido como necesitemos:

- `<h1>` a `<h6>`: Para encabezados de diferentes niveles.

```html
<h1>Encabezado nivel 1</h1>
<h2>Encabezado nivel 2</h2>
<h3>Encabezado nivel 3</h3>
<h4>Encabezado nivel 4</h4>
<h5>Encabezado nivel 5</h5>
<h6>Encabezado nivel 6</h6>
```

- `<p>`: Para párrafos de texto.

```html
<p>Este es un párrafo de texto.</p>
```

- `<ul>` y `<li>`: Para listas de elementos.

```html
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
  <li>Elemento 3</li>
</ul>
```

- `<a>`: Para enlaces a otras páginas web.

```html
<a href="http://www.ejemplo.com">Enlace a Ejemplo.com</a>
```

- `<img>`: Para insertar imágenes.

```html
<img src="ruta_de_la_imagen.jpg" alt="Descripción de la imagen">
```

- `<div>`: Para agrupar elementos relacionados.

```html
<div>
  <h2>Encabezado del grupo 1</h2>
  <p>Elemento 1</p>
  <p>Elemento 2</p>
</div>
<div>
  <h2>Encabezado del grupo 2</h2>
  <p>Elemento 3</p>
  <p>Elemento 4</p>
</div>
```

En resumen, la estructura HTML es la base sobre la que se construyen las páginas web y se compone de diferentes etiquetas que nos permiten dar formato y estructura al contenido. Las posibilidades son muy amplias y con el tiempo y la práctica se pueden ir aprendiendo nuevas etiquetas y usos.  
