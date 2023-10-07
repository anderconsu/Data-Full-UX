# Programación Orientada a Objetos
 
La programación orientada a objetos (POO) en ES6 se refiere a la manera de programar en JavaScript utilizando conceptos de la POO, como clases, objetos, herencia, encapsulación, entre otros.

En lugar de usar formas antiguas de programación en JavaScript, que se basan en la manipulación de objetos globales y funciones anónimas, las clases en ES6 permiten la creación de objetos más estructurados y más fáciles de entender y mantener.

Las clases en ES6 se definen con la palabra clave `class` seguida del nombre de la clase, los miembros de la clase se definen en su constructor. Veamos un ejemplo:

```javascript
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }
  
  saludar() {
    console.log(`Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`);
  }
}

let nuevaPersona = new Persona('John', 30);
nuevaPersona.saludar(); // Hola, mi nombre es John y tengo 30 años.
```

En el ejemplo anterior, creamos una clase `Persona` que tiene dos propiedades, `nombre` y `edad`, y un método llamado `saludar()`. Luego, creamos un objeto nuevo `nuevaPersona` de la clase `Persona` con los valores "John" y 30 pasados como argumentos, y llamamos al método `saludar()` de ese objeto.

## Herencia

Uno de los conceptos clave en la POO es la herencia, que permite crear nuevas clases a partir de otras clases ya existentes. Para heredar una clase en ES6, se utiliza la palabra clave `extends`. Veamos un ejemplo:

```javascript
class Estudiante extends Persona {
  constructor(nombre, edad, curso) {
    super(nombre, edad);
    this.curso = curso;
  }
  
  presentar() {
    console.log(`Hola, soy ${this.nombre} y curso el ${this.curso}.`);
  }
}

let nuevoEstudiante = new Estudiante('Mary', 22, 'Programación');
nuevoEstudiante.saludar(); // Hola, mi nombre es Mary y tengo 22 años.
nuevoEstudiante.presentar(); // Hola, soy Mary y curso el Programación.
```

En el ejemplo anterior, creamos una clase `Estudiante` que hereda de la clase `Persona` utilizando la palabra clave `extends`. En el constructor, se llaman los parámetros de la clase `Persona` que se desea heredar, además se agrega un nuevo parámetro `curso`. Luego se define un método llamado `presentar`, que es específico de la clase `Estudiante`.

## Encapsulación

La POO en ES6 también permite la encapsulación de datos, que significa que los datos de una clase se ocultan de su entorno y sólo pueden ser accedidos mediante métodos de la propia clase. Para lograr esto, se utiliza el prefijo `_` en las propiedades y métodos privados de la clase. Sin embargo, esto sólo oculta el dato, no lo hace inaccesible. Veamos un ejemplo:

```javascript
class Banco {
  #totalDinero;
  constructor() {
    this.#totalDinero = 5000;
  }
  
  depositar(cantidad) {
    this.#totalDinero += cantidad;
  }
  
  reporteDinero() {
    console.log(`El total de dinero en el banco es ${this.#totalDinero}.`);
  }
}

let miBanco = new Banco();
miBanco.reporteDinero(); // El total de dinero en el banco es 5000.
miBanco.depositar(1000);
miBanco.reporteDinero(); // El total de dinero en el banco es 6000.
```

En el ejemplo anterior, creamos una clase `Banco` que tiene una propiedad privada `_totalDinero` que se incia con un valor de 5000 y dos métodos, `depositar()` que incrementa el total de dinero en el banco y `reporteDinero()` que muestra el total de dinero en console.log. Aunque no existe una forma directa de acceder a `_totalDinero` desde fuera de la clase, es posible modificarlo mediante la llamada al método `depositar()`.

## Polimorfismo

El polimorfismo es un concepto de la programación orientada a objetos (POO) que permite que un objeto pueda tomar diferentes formas o comportamientos en función del contexto en el que se utiliza.

En otras palabras, un objeto polimórfico es aquel que tiene la capacidad de tomar diferentes formas al implementar una interfaz o clase abstracta, es decir, pueden representar varios tipos de objetos.

El polimorfismo permite la reutilización de código y la modularidad en los sistemas. Por ejemplo, se pueden definir métodos abstractos y aplicarlos a diferentes clases con diferentes implementaciones. De esta manera, se pueden realizar operaciones similares en diferentes tipos de objetos que se comportan de manera distinta.

Veamos un ejemplo para entenderlo mejor:

Supongamos que tenemos una función `reproducirse()` que llama un método en diferentes animales. Si implementamos un pato, un perro y un gato, la función `reproducirse()` funcionaría de manera diferente en cada uno de ellos. En este caso, el polimorfismo nos permite utilizar un mismo método con diferentes implementaciones.

```javascript
class Animal {
  reproducirse() {
    console.log('El animal se está reproduciendo.')
  }
}

class Pato extends Animal {
  reproducirse() {
    console.log('El pato está poniendo huevos.')
  }
}

class Perro extends Animal {
  reproducirse() {
    console.log('El perro está teniendo cachorros.')
  }
}

class Gato extends Animal {
  reproducirse() {
    console.log('El gato está teniendo gatitos.')
  }
}

let animal1 = new Pato();
animal1.reproducirse(); // El pato está poniendo huevos.

let animal2 = new Perro();
animal2.reproducirse(); // El perro está teniendo cachorros.

let animal3 = new Gato();
animal3.reproducirse(); // El gato está teniendo gatitos.
```

En el ejemplo anterior vemos una clase genérica llamada `Animal` con un método común `reproducirse()`. Luego se crean tres clases que extienden de esta clase genérica: `Pato`, `Perro` y `Gato`. En cada una de estas clases, se sobre-escribe el método `reproducirse()` con una implementación especifica.

Finalmente, creamos tres objetos de tres clases distintas y llamamos al método `reproducirse()`. Gracias al polimorfismo, cada objeto llama a su propia versión del método `reproducirse()` y produce resultados diferentes.

## Referencias

- [MDN Web Docs](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Classes)
- [W3Schools](https://www.w3schools.com/js/js_classes.asp)

