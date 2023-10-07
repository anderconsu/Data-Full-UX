# Ejercicios de Excepciones
**Ejercicio 1:** 
Elabora un programa que solicite al usuario los números para realizar una división. Si el usuario introduce cero como segundo número, debe lanzarse una excepción indicando que no se puede dividir entre cero. Si el usuario introduce un valor no numérico, también debe lanzarse una excepción indicando que el valor introducido no es válido.

```javascript
let num1 = Number(prompt("Introduce el dividendo"));
let num2 = prompt("Introduce el divisor");

try {
  if (isNaN(num1) || isNaN(num2)) {
    throw "Valor introducido no es valido";
  } else if (num2 == 0) {
    throw "No se puede dividir entre cero";
  } else {
    console.log(`El resultado de la division es: ${num1/num2}`);
  }
}
catch(err) {
  console.log(`Error: ${err}`);
}
```

**Ejercicio 2:**
Elabora un programa que solicite al usuario su edad. Si el usuario introduce un valor no numérico, debe lanzarse una excepción indicando que el valor introducido no es válido. Si el usuario introduce una edad negativa, también debe lanzarse una excepción indicando que la edad no puede ser negativa.

```javascript
let edad = prompt("Introduce tu edad");
try {
  if (isNaN(edad)) {
    throw "El valor introducido no es valido";
  } else if (edad < 0) {
    throw "La edad no puede ser negativa";
  } else {
    console.log("La edad introducida es: " + edad);
  }
}
catch(err) {
  console.log(`Error: ${err}`);
}
```

**Ejercicio 3:**
Elabora un programa que solicite al usuario que introduzca una cadena de texto. Si la cadena es vacía o nula, debe lanzarse una excepción indicando que la cadena no puede estar vacía.

```javascript
let cadena = prompt("Introduce una cadena de texto");

try {
  if (cadena == "" || cadena == null) {
    throw "La cadena no puede estar vacía";
  } else {
    console.log("La cadena introducida es: " + cadena);
  }
}
catch(err) {
  console.log(`Error: ${err}`);
}
```