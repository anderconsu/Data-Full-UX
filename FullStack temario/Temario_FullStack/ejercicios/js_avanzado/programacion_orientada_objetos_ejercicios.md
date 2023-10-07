Ejercicio 1:
Crea una clase "Persona" que tenga una propiedad "nombre" y un método "decirNombre()" que imprima por consola el nombre de la persona.

```javascript

const persona1 = new Persona("Juan");
persona1.decirNombre(); // salida esperada: "Mi nombre es Juan"
```

Ejercicio 2:
Agrega una propiedad "edad" a la clase "Persona" y un método "decirEdad()" que imprima por consola la edad de la persona.

```javascript


const persona1 = new Persona("Juan", 30);
persona1.decirNombre(); // salida esperada: "Mi nombre es Juan"
persona1.decirEdad(); // salida esperada: "Tengo 30 años"
```

Ejercicio 3:
Crea una clase "Empleado" que herede de la clase "Persona". Agrega una propiedad "puesto" y un método "decirPuesto()" que imprima por consola el puesto del empleado.

```javascript


const empleado1 = new Empleado("Pedro", 25, "Analista de Sistemas");
empleado1.decirNombre(); // salida esperada: "Mi nombre es Pedro"
empleado1.decirEdad(); // salida esperada: "Tengo 25 años"
empleado1.decirPuesto(); // salida esperada: "Mi puesto es Analista de Sistemas"
```

Ejercicio 4:
Crea una clase "Tienda" que tenga una propiedad "nombre" y un array de objetos "productos". Cada objeto en el array debe tener propiedades como "nombre", "precio" y "cantidad". Crea un método "agregarProducto()" que reciba como parámetro un objeto con las propiedades mencionadas y lo agregue al array de productos de la tienda. Crea un método "mostrarProductos()" que imprima por consola todos los productos de la tienda.

```javascript


const tienda1 = new Tienda("Supermercado");
tienda1.agregarProducto({nombre: "Leche", precio: 15, cantidad: 20});
tienda1.agregarProducto({nombre: "Pan", precio: 5, cantidad: 50});
tienda1.agregarProducto({nombre: "Arroz", precio: 25, cantidad: 10});
tienda1.mostrarProductos();
// salida esperada:

// Productos en Supermercado:
// Leche - $15 (20 disponibles)
// Pan - $5 (50 disponibles)
// Arroz - $25 (10 disponibles)
```

Ejercicio 5:
Crea una clase "Carrito" que tenga una propiedad "productos" y un método "agregarProducto()" que reciba como parámetro un objeto con las propiedades "nombre", "precio" y "cantidad", y lo agregue al array de productos del carrito. Crea un método "mostrarProductos()" que imprima por consola todos los productos del carrito.

```javascript


const carrito1 = new Carrito();
carrito1.agregarProducto({nombre: "Leche", precio: 15, cantidad: 2});
carrito1.agregarProducto({nombre: "Pan", precio: 5, cantidad: 3});
carrito1.agregarProducto({nombre: "Manzanas", precio: 20, cantidad: 5});
carrito1.mostrarProductos();
// salida esperada:

// Productos en el Carrito:
// Leche - $15 (2 piezas)
// Pan - $5 (3 piezas)
// Manzanas - $20 (5 piezas)
```

Ejercicio 6:
Crea una clase "Ventas" que tenga una propiedad "producto" y una propiedad "cantidadVendida". Crea una clase TiendaConVentas que herede de Tienda y tenga una lista de ventas. Crea un método "venderProducto()" que reciba como parámetro un objeto "producto" y una cantidad. El método debe restar la cantidad vendida de la cantidad disponible en el objeto "producto" de la tienda, y agregar un objeto "Ventas" al array de ventas de la tienda con el producto y la cantidad vendida.

```javascript



const tiendaConVentas1 = new TiendaConVentas("Supermercado con Ventas");
tiendaConVentas1.agregarProducto({nombre: "Leche", precio: 15, cantidad: 20});
tiendaConVentas1.agregarProducto({nombre: "Pan", precio: 5, cantidad: 50});
tiendaConVentas1.agregarProducto({nombre: "Arroz", precio: 25, cantidad: 10});
tiendaConVentas1.venderProducto({nombre: "Leche", precio: 15, cantidad: 20}, 5);
tiendaConVentas1.venderProducto({nombre: "Pan", precio: 5, cantidad: 50}, 10);
tiendaConVentas1.venderProducto({nombre: "Manzanas", precio: 5, cantidad: 10}, 3); // producto no existe
tiendaConVentas1.venderProducto({nombre: "Leche", precio: 15, cantidad: 20}, 20); // no hay suficientes
tiendaConVentas1.mostrarProductos();
// salida esperada:

// Se vendieron 5 Leche(s)
// Se vendieron 10 Pan(s)
// El producto Manzanas no existe en la tienda
// No hay suficientes Leche(s) disponibles
// Productos en Supermercado con Ventas:
// Leche - $15 (15 disponibles)
// Pan - $5 (40 disponibles)
// Arroz - $25 (10 disponibles)

tiendaConVentas1.mostrarVentas();
// salida esperada:

// Ventas realizadas:
// 5 Leche
// 10 Pan
```
Ejercicio 7:
Crea una clase "Cliente" que tenga propiedades como "nombre", "direccion" y "carrito". Crea un método "comprarProductos()" que reciba como parámetro una tienda y una cantidad de dinero, y compre productos de la tienda y los agregue a su carrito hasta que ya no tenga suficiente dinero para comprar más. Crea un método "mostrarCarrito()" que imprima por consola los productos en el carrito del cliente.

```javascript

const cliente1 = new Cliente("Maria", "Av. Siempre Viva 123");
cliente1.comprarProductos(tiendaConVentas1, 150);
cliente1.mostrarCarrito();
// salida esperada:

// Productos en Supermercado con Ventas:
// Leche - $15 (15 disponibles)
// Pan - $5 (40 disponibles)
// Arroz - $25 (10 disponibles)
// Se vendieron 5 Leche(s)
// Se vendieron 10 Pan(s)
// Maria ha gastado $135 y tiene $15 restante

// Productos en el Carrito:
// Leche - $15 (5 piezas)
// Pan - $5 (10 piezas)
```

Ejercicio 8:
Crea una clase "Caja" que tenga una propiedad "dinero" y un método "recibirPago()" que reciba como parámetro un monto y lo sume al dinero en la caja.

```javascript

const caja1 = new Caja();
caja1.recibirPago(50);
console.log(`Dinero en caja: $${caja1.dinero}`);
// salida esperada:

// Se recibió un pago de $50
// Dinero en caja: $50
```

Ejercicio 9:
Crea una clase "Cajero" que tenga una propiedad "caja", una propiedad "ventas" y un método "procesarVenta()" que reciba como parámetro un objeto "venta" que tenga propiedades como "cliente", "productos" y "monto". El método debe sumar el monto de la venta al dinero en la caja, y agregar la venta al array "ventas".

```javascript



const cajero1 = new Cajero(caja1);
const venta1 = new Venta("Maria", cliente1.carrito.productos, 135);
cajero1.procesarVenta(venta1);
console.log(`Dinero en caja: $${caja1.dinero}`);
cajero1.mostrarVentas();
// salida esperada:

// Venta procesada: Maria gastó $135
// Dinero en caja: $15

// Ventas realizadas:
// Maria compró productos por $135
``` 

Ejercicio 10:
Crea una clase "SupermercadoCompleto" que tenga propiedades como "nombre", "empleados", "caja", "tienda" y "cajero". Crea un método "iniciarDia()" que inicialice el día con la cantidad de empleados necesarios, el dinero en caja, los productos en la tienda y el cajero disponible.

```javascript


const supermercado1 = new SupermercadoCompleto("Mi Supermercado", 5, caja1, tiendaConVentas1, cajero1);
supermercado1.iniciarDia();
console.log("--------------------------------------------------")
let cliente2 = new Cliente("Peter", "Av. Siempre Viva 123");
cliente2.comprarProductos(supermercado1.tienda, 250);
cliente2.mostrarCarrito();
console.log("--------------------------------------------------")
supermercado1.cajero.procesarVenta(new Venta(cliente2.nombre, cliente2.carrito.productos, 250));
supermercado1.cajero.mostrarVentas();
console.log(`Dinero en caja: $${supermercado1.caja.dinero}`);

// salida esperada:

// El supermercado Mi Supermercado ha abierto
// Creando empleados...
// Empleado 1 contratado
// Empleado 2 contratado
// Empleado 3 contratado
// Empleado 4 contratado
// Empleado 5 contratado
// Dinero en caja al inicio del día: $185
// Agregando productos a la tienda...
// Cajero disponible para procesar ventas
// El supermercado Mi Supermercado ha iniciado su día
// --------------------------------------------------
// Productos en Supermercado con Ventas:
// Leche - $15 (5 disponibles)
// Pan - $5 (40 disponibles)
// Arroz - $25 (10 disponibles)
// Leche - $15 (20 disponibles)
// Pan - $5 (50 disponibles)
// Arroz - $25 (10 disponibles)
// Se vendieron 5 Leche(s)
// Se vendieron 35 Pan(s)
// Peter ha gastado $250 y tiene $0 restante
// Productos en el Carrito:
// Leche - $15 (5 piezas)
// Pan - $5 (35 piezas)
// --------------------------------------------------
// Venta procesada: Peter gastó $250
// Ventas realizadas:
// Maria compró productos por $135
// Peter compró productos por $250
// Dinero en caja: $435
```

Estos ejercicios en conjunto crean un programa integrado que simula un supermercado. Los usuarios pueden comprar productos de la tienda, y la venta es procesada por el cajero, cuyo pago es registrado en la caja.
