**Ejercicio 1: Guardar y recuperar información en localStorage**

Crea un formulario con un input de texto y un botón de guardar. Al hacer clic en el botón, guarda el valor del input de texto en localStorage. Luego, añade un botón de recuperar que, al hacer clic, recupere el valor almacenado en localStorage y muéstralo en la página.

```javascript
<input type="text" id="texto">
<button onclick="guardar()">Guardar</button>
<button onclick="recuperar()">Recuperar</button>

<script>
function guardar() {
  const texto = document.getElementById('texto').value;
  localStorage.setItem('textoGuardado', texto);
}

function recuperar() {
  const textoGuardado = localStorage.getItem('textoGuardado');
  alert(textoGuardado);
}
</script>
```

**Ejercicio 2: Eliminar información en sessionStorage**

Crea un botón que al hacer clic, almacene un valor en sessionStorage. Luego, añade otro botón que al hacer clic, elimine el valor almacenado en sessionStorage.

```javascript
<button onclick="guardar()">Guardar</button>
<button onclick="eliminar()">Eliminar</button>

<script>
function guardar() {
  sessionStorage.setItem('valorGuardado', 'Este valor estará almacenado en sessionStorage');
}

function eliminar() {
  sessionStorage.removeItem('valorGuardado');
}
</script>
```

**Ejercicio 3: Guardar un objeto en localStorage**

Crea un objeto con varias propiedades y guárdalo en localStorage. Luego, recupéralo y muestra sus propiedades en la página.

```javascript
const miObjeto = {
  nombre: 'Juan',
  edad: 30,
  ciudad: 'Madrid'
};

localStorage.setItem('miObjeto', JSON.stringify(miObjeto));

const objetoRecuperado = JSON.parse(localStorage.getItem('miObjeto'));
console.log(objetoRecuperado.nombre); // Juan
console.log(objetoRecuperado.edad); // 30
console.log(objetoRecuperado.ciudad); // Madrid
```