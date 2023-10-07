# Dataset en HTML

En HTML, el elemento `dataset` se utiliza para almacenar datos personalizados o información adicional relacionada con un elemento específico. Los datos se almacenan en pares clave-valor y se pueden acceder mediante JavaScript.

##### Ejemplo de código

```html
<div id="elemento" data-nombre="Juan" data-edad="25"></div>
```

En este ejemplo, creamos un `div` con el `id` "elemento" y dos atributos `data-` de nombre y edad, y les otorgamos un valor. La idea es que estos datos sean accedidos y utilizados por JavaScript.

##### Accediendo a `dataset` mediante JavaScript

Para acceder a los valores almacenados en el `dataset` desde JavaScript, podemos utilizar la propiedad del objeto `dataset` del elemento.

```javascript
const elemento = document.querySelector('#elemento');
const nombre = elemento.dataset.nombre;
const edad = elemento.dataset.edad;

console.log(`Nombre: ${nombre}, Edad: ${edad}`);
```

En el código anterior, obtenemos el elemento con `querySelector` y guardamos los valores de `data-nombre` y `data-edad` en las variables `nombre` y `edad`. Después, los mostramos en la consola.

##### Casos de uso

El uso más común de `dataset` es para almacenar información adicional en elementos que se manipulan mediante JavaScript. Por ejemplo, si tenemos una lista de elementos para los cuales necesitamos guardar información adicional sin afectar su estructura, podemos utilizar `dataset`.

Otro ejemplo podría ser en formularios, si se necesita guardar valores personalizados para ser accedidos más adelante, como la opción seleccionada en un selector de fecha o el idioma preferido.

Un caso más avanzado es el uso de `dataset` para el mantenimiento de estados en elementos personalizados utilizando la API de Web Components. 

En resumen, `dataset` de HTML es un atributo muy flexible que permite agregar datos adicionales a un elemento, lo que los hace útiles para agregar información personalizada a un elemento sin utilizar un atributo personalizado.