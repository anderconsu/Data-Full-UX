# Eventos

En React, los eventos se utilizan para manejar las acciones del usuario, como hacer clic en un botón o presionar una tecla en el teclado, y para actualizar la interfaz de usuario en consecuencia.

Los eventos en React se comportan de manera similar a los eventos en JavaScript común. Cuando se produce un evento, React envía un objeto de evento sintético (evento sintético) que abstrae las diferencias de comportamiento de los navegadores.

Los eventos en React se manejan utilizando atributos de eventos (event handler attributes) , que son funciones que se pasan como props a los componentes de React y que se llaman en función del tipo de evento que se ha producido. Por ejemplo, para manejar un evento de clic, necesitaríamos agregar un atributo onClick ={miFunción} a un elemento de React. En este caso, miFunción es la función que se llama cuando se realiza un clic en el elemento.

Ejemplo de código:

Supongamos que tenemos un botón en nuestra aplicación y queremos manejar el evento de clic en este botón. Podríamos hacerlo de la siguiente manera:

```jsx
import React from 'react';

function App() {
  function handleClick() {
    console.log('¡Hiciste clic en el botón!');
  }

  return (
    <div>
      <button onClick={handleClick}>Haz clic aquí</button>
    </div>
  );
}

export default App;
```

En este ejemplo, hemos definido una función handleClick que se llamará cuando se haga clic en el botón. Luego, hemos pasado esta función como un atributo de evento onClick a nuestro elemento de botón. Cuando se hace clic en el botón, se llama a la función handleClick y se imprime en la consola "¡Hiciste clic en el botón!".

Casos de uso:

- Manejar los eventos de clic, cambio, envío de formularios, etc. en elementos de React como botones, cuadros de texto, cuadros de selección, etc.
- Realizar acciones específicas en respuesta a eventos, como cerrar un cuadro de diálogo cuando se hace clic en el botón de "Cerrar".
- Actualizar el estado de la aplicación en respuesta a eventos, como actualizar la lista de tareas pendientes cuando se marca una tarea como completada.