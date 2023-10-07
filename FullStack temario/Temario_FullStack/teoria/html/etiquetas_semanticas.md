# Etiquetas semánticas en HTML
Las etiquetas semánticas en HTML son elementos que proporcionan información adicional y describen el significado y la estructura del contenido en una página web. Esto es muy importante para mejorar la accesibilidad y la comprensión del contenido para los motores de búsqueda y las personas con discapacidades visuales o auditivas.

A continuación, se presentan algunas de las etiquetas semánticas más comunes en HTML y sus casos de uso:

1. `<header>`: Esta etiqueta se utiliza para el encabezado de una página y contiene elementos como el logotipo, el menú de navegación, etc.

```html
<header>
  <img src="logo.png" alt="Logo">
  <nav>
    <ul>
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Acerca de</a></li>
      <li><a href="#">Contacto</a></li>
    </ul>
  </nav>
</header>
```

2. `<nav>`: Esta etiqueta se utiliza para el menú de navegación en una página y contiene los enlaces que permiten acceder a las distintas secciones de la página.

```html
<nav>
  <ul>
    <li><a href="#">Inicio</a></li>
    <li><a href="#">Acerca de</a></li>
    <li><a href="#">Contacto</a></li>
  </ul>
</nav>
```

3. `<main>`: Esta etiqueta se utiliza para el contenido principal de una página y contiene elementos como el título, los párrafos, las imágenes, etc.

```html
<main>
  <h1>Título de la página</h1>
  <p>Descripción de la página</p>
  <img src="imagen1.jpg" alt="Imagen 1">
  <p>Contenido de la página</p>
  <img src="imagen2.jpg" alt="Imagen 2">
</main>
```

4. `<article>`: Esta etiqueta se utiliza para el contenido principal de la página que puede ser considerado una entidad independiente, como un artículo, un post, una entrada de blog, etc.

```html
<article>
  <h2>Título del artículo</h2>
  <p>Fecha de publicación: 15 de mayo de 2021</p>
  <img src="imagen.jpg" alt="Imagen del artículo">
  <p>Contenido del artículo</p>
</article>
```

5. `<section>`: Esta etiqueta se utiliza para agrupar contenido relacionado en una página y se puede utilizar para dividir una página en distintas secciones.

```html
<section>
  <h2>Sección 1</h2>
  <p>Contenido de la sección 1</p>
</section>
<section>
  <h2>Sección 2</h2>
  <p>Contenido de la sección 2</p>
</section>
```

6. `<aside>`: Esta etiqueta se utiliza para el contenido adicional en una página que no es parte del contenido principal pero es relevante, como un widget de redes sociales, publicidad, etc.

```html
<section>
  <h2>Contenido principal</h2>
  <p>Contenido de la sección principal</p>
</section>
<aside>
  <h3>Últimos tweets</h3>
  <ul>
    <li>tweet 1</li>
    <li>tweet 2</li>
    <li>tweet 3</li>
  </ul>
</aside>
```

7. `<footer>`: Esta etiqueta se utiliza para el pie de la página y contiene elementos como información de contacto, enlaces de navegación adicionales, etc.

```html
<footer>
  <p>Derechos de autor © 2021 Mi sitio web</p>
  <nav>
    <ul>
      <li><a href="#">Inicio</a></li>
      <li><a href="#">Acerca de</a></li>
      <li><a href="#">Contacto</a></li>
      <li><a href="#">Política de privacidad</a></li>
      <li><a href="#">Términos y condiciones</a></li>
    </ul>
  </nav>
</footer>
```

En resumen, las etiquetas semánticas en HTML son muy útiles para proporcionar información adicional y describir el significado y la estructura del contenido en una página web. Esto mejora la accesibilidad y la comprensión del contenido y, por lo tanto, se recomienda su uso siempre que sea posible.