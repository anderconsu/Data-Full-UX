# Test Driven Development

Test-driven development (TDD) es una práctica de programación que consiste en escribir los tests unitarios antes de escribir el código fuente de la aplicación. Esta metodología se basa en la premisa de que escribir los tests antes de escribir el código tiene múltiples ventajas.

Los distintos tipos de tests que se pueden aplicar en TDD son los siguientes:

- Tests unitarios: son pruebas que se realizan a unidades de código aisladas. Estas pruebas tienen como objetivo asegurar que cada unidad de código se comporta de forma correcta.

- Tests de integración: son pruebas que se ejecutan en la interacción entre dos o más unidades de código. Con estos tests se busca detectar posibles problemas que puedan surgir con la conexión entre estas unidades.

- Tests de aceptación: son pruebas que se realizan para validar que la funcionalidad de la aplicación coincide con los requisitos del cliente. Con estas pruebas se busca garantizar que la aplicación se comportará adecuadamente cuando el usuario la utilice.

Entre las ventajas de utilizar TDD y la ejecución de tests periódicos durante el proceso de desarrollo del software tenemos:

- Ayuda a reducir errores: ya que los tests pueden detectar posibles errores en el código antes de que se conviertan en problemas mayores.

- Facilita el mantenimiento del código: dado que TDD fomenta un diseño modular y enfocado en la reutilización de código, el proceso de mantenimiento resulta más sencillo.

- Genera un código más escalable: al desarrollar código modular, se puede añadir nuevas funcionalidades sin tener que realizar cambios significativos.

Estas razones hacen que test-driven development sea una práctica fundamental a día de hoy en el ciclo de vida de desarrollo de software.

Jest es un framework de pruebas para Javascript, específicamente diseñado para pruebas en proyectos de ES6 y Node.js.

Para utilizar Jest, primero se debe instalar en el proyecto con el comando `npm install --save-dev jest`.

Para poder ejecutar los tests, podemos añadir la siguiente línea en el `package.json` de nuestro proyecto:
```json

"scripts": {
    ...
    "test": "node --experimental-vm-modules node_modules/jest/bin/jest.js --coverage"
    ...
  }
```

`--experimental-vm-modules` nos permitirá usar módulos ES6, y `--coverage` nos generará un informe de cobertura de los tests.

Podemos ejecutar los tests con el comando `npm test`.

---

A continuación, podemos escribir nuestras pruebas utilizando las funciones `describe()` y `it()`.

La función `describe()` se usa para agrupar pruebas relacionadas. Dentro de `describe()`, podemos definir los casos de prueba utilizando la función `it()`.

Cada test se ejecuta de forma aislada y se puede utilizar la sintaxis de ES6 para importar cualquier función o librería que sea necesaria para hacer las pruebas.

Un ejemplo de test utilizando Jest puede ser el siguiente:

``` javascript
import { suma } from '../utils';

describe('Utils', () => {
  describe('suma', () => {
    it('suma correctamente dos números', () => {
      expect(suma(1, 2)).toBe(3);
    });

    it('devuelve NaN si no se proporcionan números', () => {
      expect(suma('1', 2)).toBeNaN();
    });
  });
});
```

En este ejemplo, se agrupan pruebas relacionadas con la función `suma()` en el módulo llamado `utils`. 

Dentro de `describe('suma')`, definimos dos pruebas utilizando la función `it()`. La primera prueba comprueba que `suma(1, 2)` devuelve 3, mientras que la segunda prueba comprueba que si los argumentos no son números, se devuelve NaN.

La sintaxis `expect().toBe()` se utiliza para definir las condiciones que se deben cumplir para que la prueba sea validada correctamente. En este caso, `toBe()` define que el resultado de la operación debe ser igual al valor esperado.

Este es solo un ejemplo básico de cómo se pueden utilizar `describe()` y `it()` en Jest. Dependiendo de la complejidad del proyecto y las necesidades de la prueba, se pueden agregar más pruebas, utilizar otras funciones de Jest, como `beforeEach()` o `afterEach()`, para ejecutar código antes o después de cada prueba.

En resumen, Jest es una herramienta muy potente para realizar pruebas en proyectos de ES6 y Node.js, y las funciones `describe()` y `it()` nos permiten agrupar pruebas relacionadas y definir los casos de prueba de forma clara y organizada.

Jest proporciona una gran cantidad de funciones `expect()` para realizar pruebas en JavaScript. A continuación, se describirán algunos ejemplos de pruebas comunes utilizando distintos tipos de expect.

1. toEqual(): esta función comprueba que dos objetos sean iguales en valor y contenido.

```javascript
describe('Array', () => {
  describe('#indexOf()', () => {
    it('debe devolver -1 cuando el valor no está presente', () => {
      expect([1, 2, 3].indexOf(4)).toEqual(-1);
    });

    it('debe devolver el índice cuando el valor está presente', () => {
      expect([1, 2, 3].indexOf(1)).toEqual(0);
    });
  });
});
```

En este caso, `toEqual()` se utiliza para comparar el valor devuelto por la función `indexOf()` con el valor esperado.

2. toMatch(): esta función se utiliza para comparar una cadena de texto con una expresión regular.

```javascript
describe('Validar contraseña', () => {
  it('debe aceptar contraseñas que contengan letras y números', () => {
    expect(validarContrasena('Password123')).toMatch(/^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z]{8,}$/);
  });
});
```

En este ejemplo, `toMatch()` se utiliza para validar que la contraseña cumple con ciertos requisitos, en este caso, obliga a que tenga al menos 8 caracteres y contenga tanto letras como números.

3. toContain(): esta función comprueba si un valor se encuentra en una lista o cadena.

```javascript
describe('Array', () => {
  describe('#filter()', () => {
    it('debe filtrar números mayores o iguales a 5', () => {
      expect([1, 2, 5, 7, 10].filter(x => x >= 5)).toContain(5);
    });

    it('no debe filtrar números menores a 5', () => {
      expect([1, 2, 5, 7, 10].filter(x => x >= 5)).not.toContain(2);
    });
  });
});
```

En este ejemplo, `toContain()` se utiliza para validar si el número `5` se encuentra en la lista generada por el filtro. 

4. toThrow(): la función `toThrow()` se utiliza para comprobar si una función lanza una excepción.

```javascript
describe('División', () => {
  it("debe lanzar una excepción al dividir entre cero", () => {
    expect(() => { dividir(10, 0) }).toThrow("No se puede dividir entre cero");
  });
});
```

En este caso, `toThrow()` se utiliza para validar que la función `dividir()` lanza una excepción si se intenta dividir por cero.

En resumen, Jest proporciona una gran cantidad de funciones `expect()` que se adaptan a distintos tipos de pruebas, siendo también fácil de utilizar con las pruebas escritas con ECMAScript 6.