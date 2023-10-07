Aquí van algunos ejercicios para practicar con funciones:

### Funciones declarativas
1. Crea una función declarativa que tome dos argumentos numéricos y los sume.
```javascript
function suma(num1, num2){
  return num1 + num2;
}

console.log(suma(2,3)); // 5
```

2. Crea una función declarativa que tome un parámetro de texto y lo devuelva en mayúsculas.
```javascript
function aMayusculas(texto){
  return texto.toUpperCase();
}

console.log(aMayusculas('hola mundo')); // HOLA MUNDO
```

### Funciones expresivas

1. Crea una función expresiva anónima que tome dos argumentos numéricos y los multiplique.
```javascript
const multiplicacion = function(num1, num2){
  return num1 * num2;
}

console.log(multiplicacion(2,3)); // 6
```

2. Crea una función expresiva anónima que tome un parámetro numérico y lo devuelva en negativo.
```javascript
const negativo = function(num){
  return -num;
}

console.log(negativo(8)); // -8
```

### Funciones flecha

1. Crea una función flecha que tome dos argumentos numéricos y los reste.
```javascript
const resta = (num1, num2) => num1 - num2;

console.log(resta(7,3)); // 4
```

2. Crea una función flecha que tome un parámetro de texto y lo devuelva en minúsculas.
```javascript
const aMinusculas = texto => texto.toLowerCase();

console.log(aMinusculas('HOLA MUNDO')); // hola mundo
```