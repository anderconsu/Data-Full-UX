A continuación se presentan los métodos de arrays más utilizados en Javascript:

### 1. map()
El método `map()` crea un nuevo array con los resultados de la llamada a una función para cada elemento del array original. Devuelve un nuevo array del mismo tamaño que el original.

**Características:**
- No modifica el array original
- Retorna un nuevo array

**Uso:** Actualizar o transformar los elementos de un array sin modificar el array original.

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const duplicarNumeros = numeros.map(numero => numero * 2);
console.log(duplicarNumeros); // [2, 4, 6, 8, 10]
```

### 2. filter()
El método `filter()` crea un nuevo array con todos los elementos que cumplan la condición de una función proporcionada. Retorna un nuevo array.

**Características:**
- No modifica el array original
- Retorna un nuevo array con los elementos permitidos por la función de filtrado.

**Uso:** Filtrar los elementos de un array según una condición dada.

**Ejemplo:**
```javascript
const numeros  = [1, 2, 3, 4, 5];
const numerosImpares = numeros.filter(function(numero) {
  return numero % 2 !== 0;
});
console.log(numerosImpares); // [1, 3, 5]
```

### 3. reduce()
El método `reduce()` ejecuta una función reductora sobre cada elemento del array, retornando un único resultado. Retorna un simple valor.

**Características:**
- No modifica el array original
- Retorna un solo valor.

**Uso:** Reducir los elementos de un array a un valor único.

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const sumaNumeros = numeros.reduce((acumulador, numero) => acumulador + numero);
console.log(sumaNumeros); // 15
```

### 4. find()
El método `find()` devuelve el valor del primer elemento del array que cumpla una determinada condición proporcionada por una función. Retorna el valor del primer elemento en el array que se cumpla.

**Características:**
- No modifica el array original
- Retorna el primer elemento que cumpla con la condición.

**Uso:** Buscar un elemento específico en un array.

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const numeroBuscado = numeros.find(function(numero) {
  return numero === 3;
});
console.log(numeroBuscado); // 3
```

### 5. forEach()
El método `forEach()` ejecuta una determinada función en cada elemento del array. Retorna `undefined`.

**Características:**
- No modifica el array original
- No retorna un nuevo array o un valor único.

**Uso:** Iterar sobre los elementos de un array.

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
numeros.forEach(function(numero){
  console.log(numero);
});
// 1
// 2
// 3
// 4
// 5
```

### 6. some()
El método `some()` comprueba si al menos uno de los elementos del array cumple una determinada condición proporcionada por una función. Retorna un booleano.

**Características:**
- No modifica el array original
- Retorna `true` si al menos un elemento cumple la condición, y `false` si no hay elementos que lo cumplan.

**Uso:** Comprobar si al menos un elemento de un array cumple una determinada condición.

**Ejemplo:**
```javascript
const numeros = [1, 2, 3, 4, 5];
const numerosMayoresQueTres = numeros.some(function(numero) {
  return numero > 3;
});
console.log(numerosMayoresQueTres); // true
```

Estos son los métodos más comunes de los arrays en Javascript con los que seguramente te encontrarás durante tu trabajo como desarrollador.

## Referencias
- [MDN - Array](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [W3Schools - JavaScript Array Methods](https://www.w3schools.com/jsref/jsref_obj_array.asp)