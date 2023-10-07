# Recursividad
La recursividad es un concepto fundamental en programación que consiste en que una función se llame a sí misma para resolver un problema. De forma más técnica, un algoritmo se considera recursivo si se define en términos del mismo problema que se está resolviendo y contiene llamadas repetidas a sí mismo para abordar subproblemas más pequeños.

Para entender mejor el concepto, podemos tomar como ejemplo el siguiente problema:

Supongamos que queremos sumar los primeros n números naturales. Por ejemplo, si n=5, queremos calcular la suma 1 + 2 + 3 + 4 + 5.

Podemos resolver este problema de forma recursiva. Denotando la suma de los primeros n números naturales como sum(n), podemos escribir:

sum(n) = 1 + 2 + 3 + ... + (n-1) + n  
sum(n-1) = 1 + 2 + 3 + ... + (n-1)  
sum(n) = sum(n-1) + n  

La última ecuación es una llamada recursiva a la función sum(), que se está invocando a sí misma con un argumento más pequeño en cada paso hasta llegar al caso base sum(1) = 1.

A continuación, se muestra el código en JavaScript de la función recursiva para sumar los primeros n números naturales:

```javascript
function sum(n) {
   if (n === 1) { // caso base
      return 1;
   } else { // caso recursivo
      return n + sum(n-1);
   }
}
```

Otro ejemplo común de uso de la recursividad es en la implementación de la función factorial. El factorial de un número entero n se define como la multiplicación de todos los enteros positivos desde 1 hasta n. Es decir:

n! = 1 x 2 x 3 x ... x (n-1) x n

Podemos programar una función recursiva para calcular el factorial de n de la siguiente manera:

```javascript
function factorial(n) {
   if (n === 0) { // caso base
      return 1;
   } else { // caso recursivo
      return n * factorial(n-1);
   }
}
```

En ambos casos, es importante asegurarse de que existe un caso base que detenga la recursión en un momento dado para no caer en un bucle infinito.

La recursividad suele ser una técnica muy poderosa para resolver problemas complejos. Algunos otros ejemplos de problemas que se pueden resolver de forma recursiva incluyen:

- Cálculo de números de Fibonacci
- Búsqueda de caminos en un grafo
- Ordenamiento de arrays (por ejemplo, mediante el algoritmo quicksort)
- Resolución de laberintos

Es importante tener en cuenta que, aunque la recursividad puede ser muy elegante y útil, también puede tener costos elevados en términos de memoria y eficiencia. Por lo tanto, es importante evaluar cuidadosamente si la recursividad es la mejor opción para un problema en particular y comparar con otras alternativas algorítmicas.