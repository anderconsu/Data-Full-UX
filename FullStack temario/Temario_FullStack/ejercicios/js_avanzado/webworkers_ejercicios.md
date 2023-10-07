# Ejercicios de web workers
## Ejercicio 1:

Cree un web worker que calcule el factorial de un número ingresado por el usuario. El resultado debe ser devuelto al hilo principal y mostrado en la consola.

```javascript
// index.js
const worker = new Worker('factorial.js');

const numberInput = document.getElementById('number');
const calculateButton = document.getElementById('calculate');

calculateButton.addEventListener('click', () => {
  const number = Number(numberInput.value);

  worker.postMessage(number);
});

worker.onmessage = (event) => {
  console.log(`El factorial de ${event.data.number} es ${event.data.result}`);
};

// factorial.js
function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

self.addEventListener('message', (event) => {
  const number = event.data;
  const result = factorial(number);

  self.postMessage({ number, result });
});
```

## Ejercicio 2:

Cree un web worker que calcule la suma de los números de un array ingresado por el usuario. El resultado debe ser devuelto al hilo principal y mostrado en la consola.

```javascript
// index.js
const worker = new Worker('sum.js');

const arrayInput = document.getElementById('array');
const calculateButton = document.getElementById('calculate');

calculateButton.addEventListener('click', () => {
  const array = arrayInput.value.split(',').map(Number);

  worker.postMessage(array);
});

worker.onmessage = (event) => {
  console.log(`La suma del array [${event.data.array}] es ${event.data.result}`);
};

// sum.js
function sumArray(array) {
  let sum = 0;

  for (let i = 0; i < array.length; i++) {
    sum += array[i];
  }

  return sum;
}

self.addEventListener('message', (event) => {
  const array = event.data;
  const result = sumArray(array);

  self.postMessage({ array, result });
});
```