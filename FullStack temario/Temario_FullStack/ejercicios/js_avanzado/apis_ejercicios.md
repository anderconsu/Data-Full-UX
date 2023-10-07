# Ejericios de APIs

## Ejercicio 1:
Crea un array de urls que representen distintos recursos. Usando fetch, pide cada recurso y únelo a una respuesta final. Luego muestra la respuesta final por consola.

```javascript
const urls = [
  'https://jsonplaceholder.typicode.com/users/1',
  'https://jsonplaceholder.typicode.com/posts/1',
  'https://jsonplaceholder.typicode.com/comments/1'
]

Promise.all(urls.map(url => fetch(url)))
  .then(responses => Promise.all(responses.map(res => res.json())))
  .then(data => console.log(data))
```

## Ejercicio 2:
Usando fetch, pide datos de la API de Pokemon. Muestra el nombre y tipo de los primeros 5 pokemon por consola.

```javascript
fetch('https://pokeapi.co/api/v2/pokemon?limit=5')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(pokemon => {
      fetch(pokemon.url)
        .then(response => response.json())
        .then(data => {
          console.log(`${data.name}: ${data.types.map(type => type.type.name).join(', ')}`)
        })
    })
  })
```

## Ejercicio 3:
Usando fetch, pide datos de la API de Github para obtener el perfil de un usuario. Pide al usuario que introduzca nombre de usuario y muestra por consola el nombre, el avatar y los repositorios.

```javascript
const username = prompt("Introduzca un nombre de usuario de Github")
fetch(`https://api.github.com/users/${username}`)
  .then(response => response.json())
  .then(data => {
    console.log(`Nombre: ${data.name}`)
    console.log(`Avatar: ${data.avatar_url}`)
    fetch(data.repos_url).then(response => response.json())
      .then(data => {
        console.log("Repositorios:")
        data.forEach(repo => console.log(`${repo.name}: ${repo.description || 'Sin descripción'}`))
      })
  })
```