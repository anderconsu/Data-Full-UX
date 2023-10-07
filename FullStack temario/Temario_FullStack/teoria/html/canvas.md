# Canvas

Canvas es un elemento de HTML que se utiliza para crear gráficos y animaciones en 2D y 3D en tiempo real. Permite dibujar formas, texto, imágenes y aplicar efectos mediante el uso de JavaScript. 

### Sintaxis básica

Para utilizar canvas en HTML, debemos crear un elemento canvas en el HTML y luego acceder a él mediante JavaScript para poder dibujar en él. La sintaxis básica es la siguiente:

```html
<canvas id="miCanvas" width="500" height="500"></canvas>
```

El atributo `id` es necesario para acceder al canvas desde JavaScript. Los atributos `width` y `height` especifican el tamaño del canvas en píxeles.

### Accediendo al canvas

Para acceder al canvas desde JavaScript, podemos utilizar el método `getContext()` con el argumento `"2d"` para acceder al contexto en 2D, o `"webgl"` para acceder al contexto en 3D. La sintaxis para acceder al canvas es la siguiente:

```js
const canvas = document.getElementById("miCanvas")
const ctx = canvas.getContext("2d")
```

### Dibujando en el canvas

Una vez que hemos accedido al contexto del canvas, podemos empezar a dibujar utilizando métodos como `fillRect()`, `strokeRect()`, `beginPath()`, `moveTo()`, `lineTo()`, `fillText()`, `strokeText()`, entre otros.

```js
// Dibujar un rectángulo relleno
ctx.fillStyle = "blue"
ctx.fillRect(0, 0, 100, 100)

// Dibujar un rectángulo con borde
ctx.strokeStyle = "red"
ctx.strokeRect(50, 50, 100, 100)

// Dibujar una línea
ctx.beginPath()
ctx.moveTo(0, 0)
ctx.lineTo(100, 100)
ctx.stroke()

// Escribir texto
ctx.font = "30px Arial"
ctx.fillStyle = "green"
ctx.fillText("Hola canvas!", 200, 50)
```

También podemos dibujar imágenes utilizando el método `drawImage()` y cargando la imagen con `Image()`.

```js
const img = new Image()
img.src = "mi-imagen.png"
img.onload = () => {
  ctx.drawImage(img, 0, 0)
}
```

### Casos de uso

Canvas es muy útil para crear gráficas, juegos, visualizaciones de datos, animaciones y cualquier otra aplicación que requiera gráficos en tiempo real.

En conclusión, canvas es una herramienta poderosa para crear gráficos y animaciones en HTML con JavaScript. Con un poco de práctica, podrás crear impresionantes visualizaciones y juegos en tiempo real.