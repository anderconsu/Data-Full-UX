
# HTTP
El protocolo HTTP (Hypertext Transfer Protocol) es el protocolo utilizado en la Web para la transferencia de datos. HTTP define una serie de métodos de solicitud y respuesta estándar que se utilizan para la comunicación entre el cliente (por ejemplo, un navegador web) y el servidor (por ejemplo, una aplicación web).

## Métodos HTTP:

- **GET**: Solicita una representación de un recurso especificado. Las solicitudes GET sólo deben recuperar datos.
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'GET'
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error))
```

- **POST**: Envia datos a un recurso especifio, en este caso crea un recurso en el servidor recibiendo el payload en la petición HTTP.
```javascript 
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: 'foo',
    body: 'bar',
    userId: 1
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error))
```

- **PUT**: Actualiza una representación completa de un recurso existente.
```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    id: 1,
    title: 'foo',
    body: 'bar',
    userId: 1
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error))
```

- **DELETE**: Borra un recurso especificado.
```javascript 
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE'
})
.then(response => console.log(response.status))
.catch(error => console.error(error))
```

- **PATCH**: Actualiza parcialmente un recurso existente.
```javascript 
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PATCH',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    title: 'foo'
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error))
```

- **HEAD**: Pide una respuesta idéntica a la de una petición GET, pero sin el cuerpo de la respuesta.
```javascript 
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'HEAD'
})
.then(response => {
  console.log(response.headers)
})
.catch(error => console.error(error))
```

- **OPTIONS**: Describe las opciones de comunicación con el recurso de destino.
```javascript 
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'OPTIONS'
})
.then(response => {
  console.log(response.headers)
})
.catch(error => console.error(error))
```

Estos son los métodos HTTP y sus usos más comunes en la Web. Es importante tener en cuenta que los métodos HTTP como GET, POST, PUT y DELETE son utilizados para manipulación de recursos y su correcto uso depende del diseño de la API que se esté consumiendo.  

## Códigos de estado HTTP
Al realizar una petición HTTP a un servidor, este devuelve una respuesta que incluye un código de estado HTTP que indica el resultado de la petición.

Los códigos de estado HTTP son números de tres dígitos que se utilizan para proporcionar información sobre el resultado de una petición HTTP. Estos códigos se dividen en cinco clases principales:

- Clase 1xx - Respuestas informativas: Estos códigos indican que la petición ha sido recibida y el servidor está continuando a procesarla.

- Clase 2xx - Respuestas satisfactorias: Estos códigos indican que la petición ha sido recibida, entendida y aceptada correctamente.

- Clase 3xx - Redirecciones: Estos códigos indican que se requiere tomar acciones adicionales para completar la petición.

- Clase 4xx - Errores de cliente: Estos códigos indican algún problema en la petición del cliente.

- Clase 5xx - Errores de servidor: Estos códigos indican que el servidor no pudo completar la petición debido a un problema interno.

Algunos ejemplos de códigos de estado HTTP y sus casos de uso son:

- **200 OK**: Indica que la petición fue exitosa y el servidor ha devuelto una respuesta.

- **201 Created**: Indica que la petición ha sido exitosa y el servidor ha creado un nuevo recurso.

- **204 No Content**: Indica que la petición fue exitosa, pero el servidor no devuelve contenido.

- **301 Moved Permanently**: Indica que el recurso solicitado ha sido movido permanentemente a una nueva ubicación.

- **400 Bad Request**: Indica una solicitud incorrecta por parte del cliente.

- **401 Unauthorized**: Indica que la autenticación es necesaria para acceder al recurso solicitado.

- **403 Forbidden**: Indica que el servidor ha entendido la solicitud, pero se niega a autorizarla.

- **404 Not Found**: Indica que el recurso solicitado no se pudo encontrar en el servidor.

- **500 Internal Server Error**: Indica un error interno del servidor.

- **503 Service Unavailable**: Indica que el servidor no está disponible en ese momento para manejar la petición.

Para manejar estos códigos de estado HTTP en JavaScript, se utilizan las promesas. Un ejemplo de cómo se podría manejar una petición HTTP y su respuesta en JavaScript podría ser:

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => {
    if (!response.ok) {
      throw Error(response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.log(error);
  });
```

En este ejemplo, se utiliza la función `fetch` para realizar una petición HTTP a la URL proporcionada. Si la respuesta del servidor no es satisfactoria (por ejemplo, si se recibe un código de estado 404), se lanza un error utilizando la sentencia `throw`. De lo contrario, se llama al método `json()` para obtener los datos de la respuesta en formato JSON, y se imprimen en la consola. Si ocurre algún error durante el proceso, se captura y se maneja con el método `catch()`.