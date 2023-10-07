# Firebase
**¿Qué es Firebase?**

Firebase es una plataforma en la nube para el desarrollo de aplicaciones móviles y web. Permite el almacenamiento en tiempo real y la sincronización de datos entre los usuarios, así como también la autenticación de usuarios, el análisis de datos, la notificación push, etc. En resumen, se trata de un servicio de backend as a service (BaaS).

**¿Cómo utilizar Firebase con Javascript?**

Para utilizar Firebase con Javascript, lo primero es agregar la biblioteca de Firebase en el archivo HTML:

```html
<script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-database.js"></script>
```

Luego, se debe inicializar Firebase en el archivo Javascript:

```javascript
// Importar las bibliotecas de Firebase
import firebase from 'firebase/app';
import 'firebase/database';

// Configurar Firebase con las credenciales de tu proyecto
const firebaseConfig = {
  apiKey: "<tu_api_key>",
  authDomain: "<tu_auth_domain>",
  databaseURL: "<tu_db_url>",
  projectId: "<tu_project_id>",
  storageBucket: "<tu_storage_bucket>",
  messagingSenderId: "<tu_messaging_sender_id>",
  appId: "<tu_app_id>"
};

firebase.initializeApp(firebaseConfig);
```

**Casos de uso de Firebase con Javascript**

1. **Almacenamiento de datos en tiempo real**

Firebase permite almacenar y sincronizar los datos en tiempo real. Esto significa que cualquier cambio en los datos en la base de datos de Firebase se actualizará automáticamente en la aplicación en tiempo real sin necesidad de recargar la página.

```javascript
// Obtener la referencia a la base de datos
const database = firebase.database();

// Agregar un nuevo dato en la base de datos
database.ref('usuarios').push({
  nombre: 'Juan',
  apellido: 'Pérez',
  edad: 25
});

// Obtener los datos de la base de datos
database.ref('usuarios').on('value', (snapshot) => {
  snapshot.forEach((childSnapshot) => {
    const childData = childSnapshot.val();
    console.log(childData);
  });
});
```

2. **Autenticación de usuarios**

Firebase también permite la autenticación de usuarios mediante diferentes métodos: correo electrónico y contraseña, Google, Facebook, Twitter, entre otros.

```javascript
// Obtener la referencia al objeto de autenticación
const auth = firebase.auth();

// Crear una cuenta de usuario con correo electrónico y contraseña
auth.createUserWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // El usuario se registró con éxito
  })
  .catch((error) => {
    // Si se produce un error en el registro, se mostrará un mensaje de error.
    console.error(error.message);
  });

// Iniciar sesión con correo electrónico y contraseña
auth.signInWithEmailAndPassword(email, password)
  .then((userCredential) => {
    // La sesión se inició con éxito
  })
  .catch((error) => {
    // Si se produce un error en la sesión, se mostrará un mensaje de error.
    console.error(error.message);
  });

// Cerrar sesión
auth.signOut().then(() => {
  // La sesión se cerró con éxito
});
```

3. **Notificaciones push**

Firebase también permite enviar notificaciones push a los usuarios de la aplicación.

```javascript
// Obtener la referencia al objeto de mensajería
const messaging = firebase.messaging();

// Solicitar el permiso para enviar notificaciones push
messaging.requestPermission().then(() => {
  console.log('Permiso concedido');
}).catch((error) => {
  console.error(error.message);
});

// Obtener el token de registro del dispositivo
messaging.getToken().then((currentToken) => {
  if (currentToken) {
    // Enviar el token al servidor
    // ...
  } else {
    console.log('No se obtuvo el token.');
  }
}).catch((error) => {
  console.error(error.message);
});

// Recibir las notificaciones push
messaging.onMessage((payload) => {
  console.log('Se recibió una nueva notificación push: ', payload);
});
```

En resumen, Firebase es una plataforma muy potente y útil para el desarrollo de aplicaciones móviles y web. Proporciona muchos servicios para el backend y puede ahorrar mucho tiempo y esfuerzo en la construcción de aplicaciones en línea.