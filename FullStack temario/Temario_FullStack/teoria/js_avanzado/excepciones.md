## Gestión de excepciones en JavaScript
La gestión de excepciones es una habilidad importante en la programación, en donde los errores son inevitables. En el caso de JavaScript, su manejo de excepciones es similar a otros lenguajes de programación.

Las excepciones pueden ocurrir cuando se ejecuta un bloque de código y se encuentra un problema que impide que se realice alguna tarea. Por ejemplo, intentar dividir entre cero o hacer referencia a una variable no definida, son errores comunes que pueden ocurrir mientras se ejecuta el código.

En JavaScript, podemos usar `try ... catch` para manejar las excepciones. Una declaración `try` incluye el código que puede lanzar una excepción. Si ocurre una excepción, la ejecución del código se detiene y se pasa al bloque `catch`. Si no se produce una excepción, se saltará el bloque `catch` y se continuará ejecutando la siguiente línea de código después del bloque `try ... catch`.
- [MDN: try...catch](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/try...catch)
- [MDN: throw](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Statements/throw)
- [W3Schools: JavaScript Errors ](https://www.w3schools.com/js/js_errors.asp)


```javascript
try {
  // aquí va el código que puede lanzar una excepción
} catch (error) {
  // aquí se maneja la excepción
}
```

El parámetro `error` en el bloque `catch` captura la excepción y nos permite leer el mensaje y otras propiedades de la excepción para determinar qué ha ido mal. Podemos lanzar nuestras propias excepciones personalizadas usando la sentencia `throw`.

```javascript
try {
  if(x == "") throw "empty";
  if(isNaN(x)) throw "not a number";
  x = Number(x);
  if(x < 5) throw "too low";
  if(x > 10) throw "too high";
} catch(error) {
  console.log("Input is "+error);
}
```

Este código intenta convertir una cadena en un número usando `Number ()`. Si la cadena está vacía, no es un número, es demasiado bajo o demasiado alto, lanzará una excepción personalizada con el mensaje correspondiente.

Un caso de uso común para la gestión de excepciones en JavaScript es en las `promesas`. Si una promesa se resuelve correctamente, entonces la función `then()` se ejecutará. Si una promesa se rechaza por alguna razón, la función `catch()` se ejecutará.

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.log(error))
```

La función `fetch()` devuelve una promesa que se resuelve con la respuesta del servidor. Si la petición tiene éxito, la respuesta se convierte a un objeto JSON. Si ocurre un error, se pasará al bloque `catch()`.

En conclusión, el uso de `try ... catch` es una forma efectiva de manejar las excepciones en JavaScript. Cuando se utiliza bien, permite que el código continúe ejecutándose a través de errores comunes, lo que reduce la probabilidad de fallos del programa y mejora la experiencia del usuario.