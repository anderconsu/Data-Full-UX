
En ES6, existen diferentes tipos de funciones que podemos utilizar al programar con Javascript. A continuación se detallan algunos de ellos:

### Funciones Declarativas

Las funciones declarativas son aquellas que se definen utilizando la keyword `function` seguida de su nombre y parámetros, si tiene, y cuerpo de la función entre llaves {}. Estas funciones se pueden invocar en cualquier parte del código, incluso antes de ser definidas, debido al hoisting (levantamiento o elevación) que se produce en tiempo de compilación.

* Características:
  * Si la función no retorna un valor explícito, por defecto retorna `undefined`.
  * Utilizan la palabra reservada `return` para devolver un valor.
  * Permite la utilización de `arguments`, aunque se recomienda el uso de parámetros con nombres explícitos.
  * No permite utilizar funciones anónimas.

* Usos: 
  * Para modularizar el código en funciones más pequeñas y reutilizables.
  * Para calcular un resultado a partir de un conjunto de datos de entrada.
  * Para ejecutar una tarea específica.

* Ejemplo:

```javascript
// Declaración de función
function sum(a, b) {
  return a + b;
}

// Invocación de función
sum(2, 3); // retorna 5
```

### Funciones Expresivas

Las funciones expresivas son aquellas que se asignan a una variable o constante. Estas funciones no pueden ser invocadas antes de ser definidas y, por lo general, no poseen un nombre, como sucede con las funciones declarativas. Esto significa que se llaman a través de la variable o constante a la que se les asigna.

* Características:
  * Pueden ser anónimas o no.
  * No se benefician del hoisting.
  * Se asignan a una variable o constante.
  * Permiten utilizar funciones anónimas.

* Usos:
  * Para asignar funciones como argumentos a otras funciones de orden superior (higher-order functions).
  * Para crear closures (funciones que mantienen el estado interno de una función superior).

* Ejemplo:

```javascript
// Función expresiva anónima
const sum = function(a, b) {
  return a + b;
}

// Función expresiva con nombre
const multipliedByTwo = function(num) {
  return num * 2;
}

// Invocación de funciones expresivas
sum(2, 3); // retorna 5
multipliedByTwo(5); // retorna 10
```

### Funciones de Flecha

Las funciones de flecha son una forma más simplificada de definir funciones expresivas en ES6. En lugar de utilizar la palabra reservada `function`, se utilizan `=>` para definir la función. Esto reduce la complejidad sintáctica de las funciones expresivas convencionales.

* Características:
  * Sintaxis simplificada.
  * Implicitamente se aplica *return* en simples expresiones.
  * No poseen la propiedad `arguments`.
  * No permite definir su propio `this` (deben heredar el `this` de la función padre).
  * Son más legibles y fácil de entender.

* Usos:
  * Para simplificar la sintaxis de funciones expresivas convencionales.
  * Para crear funciones en una sola línea.

* Ejemplo:

```javascript
// Función de flecha
const sum = (a, b) => a + b;

const multipliedByTwo = num => num * 2; // al no poseer llaves retornará automáticamente el resultado.

// Invocación de funciones de flecha
sum(2, 3); // retorna 5
multipliedByTwo(5); // retorna 10
```