# Ejercicios de expresiones regulares
## Ejercicio 1:
Realiza una función que reciba un correo electrónico y valide si es válido o no. Considera que un correo electrónico válido contiene una sola @ y al menos un punto después del @.

```javascript
function validarCorreo(correo) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(correo);
}

console.log(validarCorreo('correo@dominio.com')); // true
console.log(validarCorreo('correodominio.com')); // false
console.log(validarCorreo('correo@dominio.com.mx')); // true
console.log(validarCorreo('correo@dominio')); // false
console.log(validarCorreo('')); // false
console.log(validarCorreo('correo@')); // false
console.log(validarCorreo('@dominio.com')); // false
```

## Ejercicio 2:
Realiza una función que reciba una cadena de texto y reemplace todas las apariciones de la palabra "Javascript" por la palabra "JS".

```javascript
function reemplazarPalabra(cadena) {
  const regex = /Javascript/gi;
  const nuevaCadena = cadena.replace(regex, 'JS');
  return nuevaCadena;
}

console.log(reemplazarPalabra('Learn Javascript, the best programming language in Javascript')); // Learn JS, the best programming language in JS
```

## Ejercicio 3:
Realiza una función que valide si una cadena de texto es un número decimal con dos decimales.

```javascript
function validarNumero(cadena) {
  const regex = /^\d+(\.\d{1,2})?$/;
  return regex.test(cadena);
}

console.log(validarNumero('123.45')); // true
console.log(validarNumero('123')); // true
console.log(validarNumero('.45')); // false
console.log(validarNumero('123.456')); // false
console.log(validarNumero('abc')); // false
```

## Ejercicio 4:
Realiza una función que valide si una cadena de texto contiene solamente letras y/o espacios.

```javascript
function validarCadena(cadena) {
  const regex = /^[a-zA-Z\s]*$/;
  return regex.test(cadena);
}

console.log(validarCadena('Cadena de texto')); // true
console.log(validarCadena('Cadena 123')); // false
console.log(validarCadena('')); // true
console.log(validarCadena('Cadena #&%')); // false
```