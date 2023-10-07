# Ejercicios de asincronía

### Callbacks
1. Crea una función `sumarDosNumeros` que acepte dos números como parámetros y un callback que se llame `mostrarResultado`. La función debe sumar los dos números y llamar al callback pasándole el resultado.
```javascript
function sumarDosNumeros(num1, num2, mostrarResultado) {
  const suma = num1 + num2;
  mostrarResultado(suma);
}

function mostrarResultado(result) {
  console.log(`El resultado es ${result}`);
}

sumarDosNumeros(2, 4, mostrarResultado); // El resultado es 6
```

2. Crea una función `filtrarNumero` que acepte un array de números como primer parámetro y un segundo parámetro que sea una función callback llamada `filtrarPares`. La función `filtrarPares` debe devolver un nuevo array únicamente con los números pares del array original y la función `filtrarNumero` debe llamar al callback y pasarle el array filtrado.
```javascript
function filtrarNumero(numeros, filtrarPares) {
  const pares = filtrarPares(numeros);
  console.log(pares);
}

function filtrarPares(numeros) {
  return numeros.filter(numero => numero % 2 === 0);
}

filtrarNumero([1, 2, 3, 4, 5], filtrarPares); // [2, 4]
```

### Promesas
1. Crea una función `obtenerPrecioProducto` que acepte el nombre de un producto como parámetro y devuelva una promesa. La promesa debe resolver con el precio del producto si el producto existe, o rechazar con el mensaje "Producto no encontrado".
```javascript
const productos = {
  computadora: 1000,
  celular: 800,
  televisión: 2000
}

function obtenerPrecioProducto(producto) {
  return new Promise((resolve, reject) => {
    if (productos[producto]) {
      resolve(productos[producto]);
    } else {
      reject("Producto no encontrado");
    }
  });
}

obtenerPrecioProducto("celular")
  .then(precio => console.log(`El precio del celular es ${precio}`))
  .catch(error => console.log(error)); // El precio del celular es 800

obtenerPrecioProducto("libro")
  .then(precio => console.log(`El precio del libro es ${precio}`))
  .catch(error => console.log(error)); // Producto no encontrado
```

2. Crea una función `obtenerDatosUsuario` que acepte un id de usuario como parámetro y devuelva una promesa. La promesa debe resolver con un objeto que contenga el nombre, correo y ciudad del usuario, o rechazar con el mensaje "Usuario no encontrado".
```javascript
const usuarios = [
  {
    id: 1,
    nombre: "Juan",
    correo: "juan@gmail.com",
    ciudad: "Lima"
  },
  {
    id: 2,
    nombre: "María",
    correo: "maria@gmail.com",
    ciudad: "Bogotá"
  }
]

function obtenerDatosUsuario(id) {
  return new Promise((resolve, reject) => {
    const usuario = usuarios.find(usuario => usuario.id === id);
    if (usuario) {
      const { nombre, correo, ciudad } = usuario;
      resolve({ nombre, correo, ciudad });
    } else {
      reject("Usuario no encontrado");
    }
  });
}

obtenerDatosUsuario(1)
  .then(usuario => console.log(usuario))
  .catch(error => console.log(error)); // { nombre: "Juan", correo: "juan@gmail.com", ciudad: "Lima"}

obtenerDatosUsuario(3)
  .then(usuario => console.log(usuario))
  .catch(error => console.log(error)); // Usuario no encontrado
```

### Async/await
1. Crea una función `ejecutarTarea` que acepte el nombre de una tarea como parámetro y devuelva una tarea que tarda en completarse de forma sintética usando `setTimeout`. La función debe usar async/await para esperar a que la tarea termine y luego mostrar el mensaje "La tarea [nombre de la tarea] ha sido completada".
```javascript
function ejecutarTarea(nombreTarea) {
  return new Promise(resolve => {
    setTimeout(() => {
      console.log(`La tarea ${nombreTarea} ha sido completada`);
      resolve(nombreTarea);
    }, 2000);
  });
}

async function completarTarea(nombreTarea) {
  await ejecutarTarea(nombreTarea);
}

completarTarea("hacer la compra"); // La tarea hacer la compra ha sido completada
completarTarea("limpiar la cocina"); // La tarea limpiar la cocina ha sido completada
```

2. Crea una función `obtenerDatosProducto` que acepte el nombre de un producto como parámetro y devuelva un objeto con el nombre y el precio del producto. La función debe usar async/await con la función `obtenerPrecioProducto` creada anteriormente para obtener el precio del producto.
```javascript
async function obtenerDatosProducto(producto) {
  try {
    const precio = await obtenerPrecioProducto(producto);
    return { nombre: producto, precio };
  } catch (error) {
    console.log(error);
  }
}

obtenerDatosProducto("computadora").then(datosProducto => console.log(datosProducto));
// { nombre: "computadora", precio: 1000 }

obtenerDatosProducto("libro").then(datosProducto => console.log(datosProducto));
// Producto no encontrado
```