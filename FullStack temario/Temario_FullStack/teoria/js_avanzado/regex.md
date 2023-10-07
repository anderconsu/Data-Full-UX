# Expresiones regulares
Las expresiones regulares, también conocidas como regex, son patrones utilizados para buscar y reemplazar cadenas de texto. En JavaScript, las expresiones regulares se crean utilizando la clase `RegExp()` o utilizando un patrón literal entre barras diagonales `/.../`.  
**link para hacer pruebas:** https://regex101.com/

Sintaxis literal: 

```js
/regex/flags
```

Sintaxis con clase `RegExp()`:

```js
new RegExp('regex', 'flags')
```

Los `flags` son los modificadores que se le pueden aplicar a la expresión regular para cambiar su comportamiento, como por ejemplo, hacer que la búsqueda sea insensible a mayúsculas y minúsculas.

Existen distintos caracteres especiales y combinaciones de ellos que se utilizan para crear patrones más complejos. A continuación, te muestro algunos de los más comunes:

- **Punto (.)**: Coincide con cualquier carácter, excepto los caracteres nuevos de línea (`\n`, `\r`). Por ejemplo, `/h.t/` coincidiría con "heat", "hit", "hot", etc.

- **Circunflejo (^)**: Coincide con el principio de la cadena. Por ejemplo, `/^h/` coincidiría con "hello" pero no con "ahoy".

- **Dólar (\$)**: Coincide con el final de la cadena. Por ejemplo, `/dog$/` coincidiría con "hotdog" pero no con "doghouse".

- **Corchetes ([])**: Coincide con cualquier carácter entre corchetes. Por ejemplo, `/[aeiou]/` coincidiría con cualquier vocal.

- **El acento circunflejo (^) dentro de corchetes**: Coincidiría con cualquier carácter que no se encuentre entre los corchetes. Por ejemplo, `/[^aeiou]/` coincidiría con cualquier consonante.

- **Asterisco (*)**: Coincide con cero o más ocurrencias del carácter o grupo anterior. Por ejemplo, `/bo*` coincidiría con "b", "bo", "boo", "booo", etc.

- **Signo más (+)**: Coincide con una o más ocurrencias del carácter o grupo anterior. Por ejemplo, `/bo+/` coincidiría con "bo", "boo", "booo", etc., pero no con "b".

- **Interrogación (?)**: Coincide con cero o una ocurrencia del carácter o grupo anterior. Por ejemplo, `/colou?r/` coincidiría con "color" y "colour".

- **Llaves ({n, m})**: Indican el número mínimo y máximo de ocurrencias del carácter o grupo anterior. Por ejemplo, `/a{2, 4}/` coincidiría con "aa", "aaa" o "aaaa".

Además de estos caracteres especiales, hay varios identificadores que se pueden utilizar para coincidir con ciertos patrones comunes:

- **\d**: Coincide con cualquier dígito (`[0-9]`).
- **\w**: Coincide con cualquier carácter alfanumérico (`[A-Za-z0-9_]`).
- **\s**: Coincide con cualquier espacio en blanco (`[\t\n\f\r ]`).

A continuación, te muestro algunos ejemplos de regex con casos de uso:

```js
// Busca cualquier cantidad de caracteres entre "a" y "z"
const regex = /[a-z]+/;
const texto = "La programación es divertida";
console.log(texto.match(regex)); // ["a", "programación", "es", "divertida"]

// Valida que la cadena sea un número de teléfono en formato internacional.
const regex = /^\+\d{1,3}\s\d{3,14}$/;
const telefono = "+54 911 1111 1111";
console.log(regex.test(telefono)); // true

// Reemplaza todas las instancias de "JavaScript" con "JS" en una cadena.
const regex = /JavaScript/g;
const texto = "JavaScript es un lenguaje de programación popular para la web. Hay muchas bibliotecas JavaScript útiles.";
const nuevoTexto = texto.replace(regex, "JS");
console.log(nuevoTexto); // "JS es un lenguaje de programación popular para la web. Hay muchas bibliotecas JS útiles."

// Busca palabras que empiecen con "fact" o "stack"
const regex = /\b(fact|stack)\w*\b/g;
const texto = "El bootcamp de Full Stack Developer con JavaScript es genial, me encanta facturar y apilar código.";
console.log(texto.match(regex)); // ["facturar", "stack", "stackpear"]
```

Como se puede ver, las expresiones regulares pueden ser muy útiles para buscar, validar y reemplazar cadenas de texto de una manera muy poderosa y flexible.