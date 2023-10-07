# Web Storage

El Web Storage es una API que nos permite almacenar datos de manera persistente en el navegador. Hay dos mecanismos de almacenamiento: `localStorage` y `sessionStorage`. Ambos permiten almacenar pares clave-valor y tienen un límite de almacenamiento.

- `localStorage`: almacena los datos de manera permanente, es decir, los datos no expiran aunque se cierre la ventana o se reinicie el navegador. Los datos almacenados en `localStorage` están disponibles para todas las ventanas del mismo origen (dominio, protocolo y puerto).

- `sessionStorage`: almacena los datos por sesión, es decir, los datos se eliminan cuando se cierra la ventana o se reinicia el navegador. Los datos almacenados en `sessionStorage` están disponibles solo para la ventana que los creó.


## Ejemplo de uso de localStorage

Podemos guardar valores en el localStorage, junto con su llave. Un ejemplo básico seria:

```javascript
localStorage.setItem('nombre', 'Juan');
```

De esta forma, se ha guardado el string "Juan" bajo la llave "nombre" en el localStorage. Ahora, si queremos recuperar este valor, lo podemos hacer de la siguiente manera:

```javascript
const nombre = localStorage.getItem('nombre');
console.log(nombre); // "Juan"
```

También podemos eliminar un valor del localStorage. Para ello, podemos usar el método `removeItem()`:

```javascript
localStorage.removeItem('nombre');
console.log(localStorage.getItem('nombre')); // null
```

Finalmente, si queremos borrar todo el contenido del localStorage, lo podemos hacer de la siguiente manera:

```javascript
localStorage.clear();
```

## Ejemplo de uso de sessionStorage

Podemos usar sessionStorage de forma muy similar a como usamos localStorage. Un ejemplo básico es:

```javascript
sessionStorage.setItem('nombre', 'Pedro');
console.log(sessionStorage.getItem('nombre')); // "Pedro"
```

También podemos eliminar un valor de la siguiente manera:

```javascript
sessionStorage.removeItem('nombre');
console.log(sessionStorage.getItem('nombre')); // null
```

Y podemos borrar todo el contenido de sessionStorage usando:

```javascript
sessionStorage.clear();
```

**Casos de uso**

- Guardar preferencias de usuario: podemos guardar preferencias de usuario en localStorage para que la próxima vez que el usuario visite nuestra web, sus preferencias ya estén preestablecidas.

- Guardar información de la sesión: podemos guardar información como el ID de sesión o los datos del usuario logueado en sessionStorage para que se mantengan disponibles solo mientras el usuario tenga abierta la ventana del navegador.

- Implementar un carrito de compras: podemos guardar los productos que ha añadido un usuario al carrito en localStorage para que si vuelve a visitar nuestra tienda más tarde, su carrito siga con los productos que había añadido previamente. 

- Guardar estado de una aplicación: si estamos trabajando en una aplicación web para edición de documentos, podemos guardar el estado del documento en localStorage y así permitir al usuario continuar donde dejó la última vez que accedió a la aplicación.