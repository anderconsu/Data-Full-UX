
1. **MAP**:
    
    - Crea un array con los números del 1 al 5. A continuación, utilizando el método `map`, devuelve un nuevo array con los números multiplicados por 2.
      ```javascript
      const numeros = [1, 2, 3, 4, 5];
      const numerosMultiplicados = numeros.map(numero => numero * 2);
      console.log(numerosMultiplicados);
      ```

2. **FILTER**:

    - Crea un nuevo array con los strings "apple", "banana", "kiwi", "mango" y "orange". Utiliza el método `filter` para obtener del array anterior únicamente los elementos que contienen la letra "a".
      ```javascript
      const frutas = ["apple", "banana", "kiwi", "mango", "orange"];
      const frutasConA = frutas.filter(fruta => fruta.includes("a"));
      console.log(frutasConA);
      ```

3. **REDUCE**:

   - Crea un array con los números del 1 al 5. Utiliza el método `reduce` para obtener la suma de todos los números.
      ```javascript
      const numeros = [1, 2, 3, 4, 5];
      const sumaTotal = numeros.reduce((acumulador, numero) => acumulador + numero, 0);
      console.log(sumaTotal);
      ```

4. **FIND**:
    
    - Crea un array con los strings "casa", "coche", "ordenador", "libro" y "pelota". Utiliza el método `find` para obtener del array anterior el elemento que empieza por la letra "o".
      ```javascript
      const elementos = ["casa", "coche", "ordenador", "libro", "pelota"];
      const elementoEncontrado = elementos.find(elemento => elemento.startsWith("o"));
      console.log(elementoEncontrado);
      ```

5. **FOR EACH**:
    
    - Crea un array con los nombres de tus cinco mejores amigos. Utiliza el método `forEach` para imprimir por consola el mensaje "Mi amigo X se llama como tu amigo" para cada uno de tus amigos. 
      ```javascript
      const amigos = ["Juan", "Pedro", "Maria", "Luisa", "Carmen"];
      amigos.forEach(amigo => console.log(`Mi amigo ${amigo} se llama como tu amigo`));
      ```

6. **SOME**:
    
    - Crea un array con los números del 1 al 5. Utiliza el método `some` para comprobar si algún número es mayor que 4. Si es así, imprime por consola el mensaje "Hay algún número mayor que 4 en el array". Si no, imprime "No hay ningún número mayor que 4 en el array".
      ```javascript
      const numeros = [1, 2, 3, 4, 5];
      const hayNumeroMayor4 = numeros.some(numero => numero > 4);
      
      if (hayNumeroMayor4) {
          console.log("Hay algún número mayor que 4 en el array");
      } else {
          console.log("No hay ningún número mayor que 4 en el array");
      }
      ```
      
Puedes combinar estos ejercicios y seguir practicando con diferentes combinaciones y variaciones en los argumentos de cada uno de estos métodos. ¡Ánimo!