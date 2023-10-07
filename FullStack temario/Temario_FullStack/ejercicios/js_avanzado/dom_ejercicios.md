# Ejercicios DOM
1. Crea una función que seleccione un elemento HTML por su id y cambie su color de fondo:

```html
<div id="ejercicio1">Este div cambiará de color</div>
```

```javascript
function cambiarColor() {
  let div = document.getElementById("ejercicio1");
  div.style.backgroundColor = "blue";
}
```

2. Crea una función que seleccione todos los elementos de una clase y cambie su tamaño de fuente:

```html
<p class="small">Este párrafo será pequeño</p>
<p class="small">Este párrafo también será pequeño</p>
```

```javascript
function cambiarTamanoFuente() {
  let elementos = document.getElementsByClassName("small");
  for (let i = 0; i < elementos.length; i++) {
    elementos[i].style.fontSize = "small";
  }
}
```

3. Crea una función que seleccione el primer elemento de una lista y agregue un nuevo elemento después:

```html
<ul id="lista">
  <li>Elemento 1</li>
  <li>Elemento 2</li>
  <li>Elemento 3</li>
</ul>
```

```javascript
function agregarElemento() {
  let lista = document.getElementById("lista");
  let nuevoElemento = document.createElement("li");
  nuevoElemento.innerHTML = "Elemento 4";
  lista.insertBefore(nuevoElemento, lista.firstChild.nextSibling);
}
```

4. Crea una función que seleccione un elemento input y cambie su valor por el texto "Nuevo valor":

```html
<input id="input1" type="text" value="Valor actual">
```

```javascript
function cambiarValor() {
  let input = document.getElementById("input1");
  input.value = "Nuevo valor";
}
```

5. Crea una función que seleccione un elemento p, y al hacer click en él, cambie su contenido por el texto "Has hecho click aquí":

```html
<p id="parrafo">Haz click aquí</p>
```

```javascript
let parrafo = document.getElementById("parrafo");
parrafo.addEventListener("click", function() {
  parrafo.innerHTML = "Has hecho click aquí";
});
```
