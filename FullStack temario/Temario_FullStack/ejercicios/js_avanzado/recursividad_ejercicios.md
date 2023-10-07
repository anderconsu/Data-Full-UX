¡Claro que sí! Aquí te presento algunos ejercicios sencillos para practicar funciones recursivas en Javascript. 

#### Ejercicio 1: Factorial 

En este primer ejercicio se trata de calcular el factorial de un número utilizando una función recursiva. El factorial de un número es el producto de todos sus enteros positivos menores o iguales al número en cuestión. Por ejemplo, el factorial de 5 es 5\*4\*3\*2\*1 = 120.

```javascript
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n-1);
  }
}

console.log(factorial(5)); // 120
```

En este ejemplo, si el número proporcionado es 0 o 1, entonces se devuelve 1 ya que el factorial de estos números es uno. De lo contrario, se utiliza la recursividad para obtener el factorial del número correspondiente.

#### Ejercicio 2: Fibonacci

El segundo ejercicio es una función recursiva que calcule la serie de Fibonacci para un número dado. La serie de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores en la serie. Por ejemplo, los primeros 10 números de la serie de Fibonacci son: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

```javascript
function fibonacci(n) {
  if (n === 0) {
    return 0;
  } else if (n === 1 || n === 2) {
    return 1;
  } else {
    return fibonacci(n-1) + fibonacci(n-2);
  }
}

console.log(fibonacci(7)); // 13
```

En este ejemplo, si el número proporcionado es 0, se devuelve 0 ya que este es el primer número de la serie. Si el número es 1 o 2, se devuelve 1 ya que son los dos primeros números de la serie. De lo contrario, se utiliza la recursividad para obtener la suma de los dos números anteriores en la serie.

#### Ejercicio 3: Sumar elementos de un array

En este último ejercicio se trata de crear una función recursiva que sume los elementos de un array. Este ejemplo también combina una condición base y una de recursión. 

```javascript
function sumArray(arr) {
  if (arr.length === 1) {
    return arr[0];
  } else {
    return arr.pop() + sumArray(arr);
  }
}

const array1 = [1, 2, 3, 4, 5];
console.log(sumArray(array1)); // 15
```

En este ejemplo, si el array tiene solo un elemento, se devuelve ese elemento. De lo contrario, se utiliza la recursividad para sumar el último elemento del array con la suma de los demás elementos.
  
### Ejercicio 4: Encontrar el número mayor en un array

- Descripción del problema: Dado un array de números, encuentra el número mayor utilizando recursión.
- Ejemplo de entrada: [4, 1, 9, 2, 5]
- Ejemplo de salida: 9

```javascript
function encuentraMayor(array) {
  if (array.length === 1) {
    return array[0];
  }
  else {
    let subMax = encuentraMayor(array.slice(1));
    return array[0] > subMax ? array[0] : subMax;
  }
}

console.log(encuentraMayor([4, 1, 9, 2, 5])); // salida: 9
```

## Ejercicio 5: Encontrar el número de veces que un elemento aparece en un array
- Descripción del problema: Dado un array y un número, cuenta cuántas veces se repite el número en el array.
- Ejemplo de entrada: ([1, 3, 5, 6, 3, 2, 5], 3)
- Ejemplo de salida: 2

```javascript
function cuentaOcurrencias(array, num) {
  if (array.length === 0) {
    return 0;
  }
  else {
    let firstElement = array[0];
    let slice = array.slice(1);
    return (firstElement === num ? 1 : 0) + cuentaOcurrencias(slice, num);
  }
}

console.log(cuentaOcurrencias([1, 3, 5, 6, 3, 2, 5], 3)); // salida: 2
```

## Ejercicio 6: Encontrar la suma de todos los números positivos en un array
- Descripción del problema: Dado un array de números, encuentra la suma de todos los números positivos utilizando recursión.
- Ejemplo de entrada: [2, -5, 3, -8, 6]
- Ejemplo de salida: 11

```javascript
function sumaPositivos(array) {
  if (array.length === 0) {
    return 0;
  }
  else {
    let firstElement = array[0];
    let slice = array.slice(1);
    return (firstElement > 0 ? firstElement : 0) + sumaPositivos(slice);
  }
}

console.log(sumaPositivos([2, -5, 3, -8, 6])); // salida: 11
```