## Asincronía en JavaScript
La asincronía en JavaScript se refiere a la capacidad de ejecutar tareas que pueden tardar tiempo en completarse sin interrumpir la ejecución secuencial del código. En otras palabras, se puede iniciar una tarea y continuar con el resto del código sin esperar a que esa tarea se complete.

En JavaScript, la asincronía se implementa a través de callbacks, promesas y async/await.

## Callbacks:
 Un callback es una función que se pasa como argumento a otra función y se llama una vez que se ha completado la tarea. Un ejemplo común de callback es el manejo de eventos como el clic de un botón en una página web.  
[MDN](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function) / [W3Schools](https://www.w3schools.com/js/js_callback.asp)
```javascript
function procesoAsync(callback) {
  setTimeout(function() {
    console.log('Proceso completado después de 2 segundos');
    callback();
  }, 2000);
}

console.log('Inicio de la tarea');
procesoAsync(function() {
  console.log('Fin de la tarea');
});
```

En este ejemplo, la función `procesoAsync` realiza una tarea que toma 2 segundos y luego llama al callback para indicar que la tarea ha terminado.

## Promesas:
 Las promesas son otro mecanismo de asincronía que se introdujo en ES6. Son objetos que representan el resultado eventual de una tarea asíncrona. Una promesa tiene tres estados posibles: pendiente, cumplida o rechazada.  
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) / [W3Schools](https://www.w3schools.com/js/js_promise.asp)
```javascript
function procesoAsync() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      console.log('Proceso completado después de 2 segundos');
      resolve();
    }, 2000);
  });
}

console.log('Inicio de la tarea');
procesoAsync().then(function() {
  console.log('Fin de la tarea');
});
```

En este ejemplo, `procesoAsync` devuelve una promesa que se resuelve después de 2 segundos. El método `then` se usa para indicar qué se debe hacer una vez que se ha cumplido la promesa.

## Async/await:
Estos son mecanismos de asincronía más recientes. Async/await son una forma más simple y legible de trabajar con promesas. Utilizamos la palabra clave `async` antes de una función para indicar que contiene código asincrónico, mientras que la palabra clave `await` se usa para esperar a que se resuelva una promesa en una función asíncrona.  
**ASYNC**  
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) / [W3Schools](https://www.w3schools.com/js/js_async.asp)  
**AWAIT**  
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await) 
```javascript
function espera(ms) {
  return new Promise(function(resolve) {
    setTimeout(resolve, ms);
  });
}

async function tareaAsync() {
  console.log('Inicio de la tarea');
  await espera(2000);
  console.log('Fin de la tarea');
}

tareaAsync();
```

En este ejemplo, `tareaAsync` es una función asíncrona que espera 2 segundos antes de imprimir "Fin de la tarea".

Casos de uso comunes de la asincronía en JavaScript incluyen la solicitud de datos a un servidor, la interacción de usuarios con una interfaz de usuario en una aplicación web y la ejecución de operaciones de larga duración sin bloquear el hilo principal de JavaScript que mejoran la experiencia del usuario.