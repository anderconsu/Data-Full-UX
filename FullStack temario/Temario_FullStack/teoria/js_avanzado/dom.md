# DOM

El DOM (Document Object Model) es una representación en forma de árbol de la estructura de un documento HTML (o documento XML) que puede ser manipulado por JavaScript para crear dinámicamente páginas web interactivas y dinámicas. 

Cuando un navegador carga un archivo HTML, convierte ese archivo en una estructura de árbol llamada DOM. Cada etiqueta HTML se convierte en un objeto en el árbol, permitiendo acceder y manipulating los elementos individuales del árbol HTML con JavaScript.

Los diferentes métodos que podemos utilizar en el DOM para manipular elementos en la página incluyen:

1. getElementById() - Permite seleccionar un elemento HTML a través de su atributo "id". Este método devuelve un solo elemento.

```html
<div id="example">Hello, world!</div>
```

```javascript
let element = document.getElementById("example");
console.log(element.innerHTML); // "Hello, world!"
```

2. getElementsByClassName() - Devuelve una colección de elementos que tienen la misma clase.

```html
<div class="example">Elemento 1</div>
<div class="example">Elemento 2</div>
<div class="example">Elemento 3</div>
```

```javascript
let elements = document.getElementsByClassName("example");
console.log(elements.length); // 3
console.log(elements[0].innerHTML); // "Elemento 1"
```

3. getElementsByTagName() - Devuelve una colección de elementos que tienen el mismo nombre de etiqueta.

```html
<div><p>Elemento 1</p></div>
<div><p>Elemento 2</p></div>
<div><p>Elemento 3</p></div>
```

```javascript
let elements = document.getElementsByTagName("p");
console.log(elements.length); // 3
console.log(elements[0].innerHTML); // "Elemento 1"
```

4. querySelector() - Permite seleccionar un elemento HTML utilizando un selector CSS. Este método devuelve el primer elemento que coincide con el selector.

```html
<div class="example">Elemento 1</div>
<div class="example">Elemento 2</div>
<div id="example">Elemento 3</div>
```

```javascript
let element = document.querySelector(".example");
console.log(element.innerHTML); // "Elemento 1"

let element2 = document.querySelector("#example");
console.log(element2.innerHTML); // "Elemento 3"
```

5. querySelectorAll() - Permite seleccionar una colección de elementos HTML utilizando un selector CSS.

```html
<div class="example">Elemento 1</div>
<div class="example">Elemento 2</div>
<div id="example">Elemento 3</div>
```

```javascript
let elements = document.querySelectorAll(".example");
console.log(elements.length); // 2
console.log(elements[0].innerHTML); // "Elemento 1"
```

6. createElement() - Permite crear un nuevo elemento HTML.

```javascript
let newElement = document.createElement("div");
newElement.innerHTML = "Nuevo elemento creado";
```

7. appendChild() - Agrega un nuevo elemento hijo a un elemento padre existente.

```html
<div id="parent">
  <p>Elemento 1</p>
</div>
```

```javascript
let parentElement = document.getElementById("parent");
let newElement = document.createElement("p");
newElement.innerHTML = "Elemento 2";
parentElement.appendChild(newElement);
```

En resumen, el DOM es una representación de la estructura del documento HTML, que puede ser manipulada a través de JavaScript para agregar, eliminar o actualizar elementos en la página. Los diferentes métodos del DOM permiten seleccionar uno o varios elementos, crear nuevos elementos y agregarlos a elementos existentes.

## Referencias

- [Document Object Model (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
- [Document Object Model (Wikipedia)](https://en.wikipedia.org/wiki/Document_Object_Model)
- [Document Object Model (W3Schools)](https://www.w3schools.com/js/js_htmldom.asp)