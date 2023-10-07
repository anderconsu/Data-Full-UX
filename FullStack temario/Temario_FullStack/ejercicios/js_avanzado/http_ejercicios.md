Ejercicio 1: Realizar una solicitud GET a jsonplaceholder.typicode.com para obtener la información de un usuario por su ID.

```javascript
fetch('https://jsonplaceholder.typicode.com/users/1')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

Ejercicio 2: Realizar una solicitud POST a jsonplaceholder.typicode.com para crear un nuevo post.

```javascript
const newPost = {
  title: 'Nuevo Post',
  body: 'Contenido del nuevo post',
  userId: 1
};

fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  body: JSON.stringify(newPost),
  headers: {
    'Content-type': 'application/json; charset=UTF-8'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
```

Ejercicio 3: Realizar una solicitud PUT a jsonplaceholder.typicode.com para actualizar un post existente.

```javascript
const updatedPost = {
  title: 'Título actualizado',
  body: 'Contenido actualizado'
}

fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PUT',
  body: JSON.stringify(updatedPost),
  headers: {
    'Content-type': 'application/json; charset=UTF-8'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
```

Ejercicio 4: Realizar una solicitud PATCH a jsonplaceholder.typicode.com para modificar la propiedad "title" de un post existente.

```javascript
const updateTitle = {
  title: 'Título actualizado'
}

fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'PATCH',
  body: JSON.stringify(updateTitle),
  headers: {
    'Content-type': 'application/json; charset=UTF-8'
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
```

Ejercicio 5: Realizar una solicitud DELETE a jsonplaceholder.typicode.com para borrar un post existente.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1', {
  method: 'DELETE'
})
.then(response => console.log('Post eliminado con éxito'))
.catch(error => console.error(error));
```