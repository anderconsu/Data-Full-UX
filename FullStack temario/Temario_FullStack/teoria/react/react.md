# React

React es una librería de JavaScript que se utiliza para construir interfaces de usuario interactivas. Fue desarrollada por Facebook y se lanzó en 2013 como código abierto. Una de las principales características de React es su enfoque en el rendimiento, ya que utiliza una técnica llamada DOM virtual para minimizar la manipulación del DOM real.

Las principales diferencias entre React y JavaScript vanilla son:

1. Componentes: React se basa en componentes, que son bloques independientes de código que se pueden reutilizar en toda la aplicación. Esto facilita la organización del código y la creación de interfaces de usuario componibles.

2. Virtual DOM: como se mencionó anteriormente, React utiliza un Virtual DOM para minimizar la manipulación del DOM real. En lugar de actualizar todo el árbol de elementos de la página, React actualiza solamente los componentes específicos que han cambiado. Esto mejora el rendimiento de la aplicación y proporciona una mejor experiencia de usuario.

3. JSX: React utiliza una sintaxis llamada JSX, que permite mezclar HTML y JavaScript en el mismo archivo. Esto puede parecer extraño al principio, pero hace que sea más fácil construir componentes y proporciona una mejor separación de preocupaciones entre la vista y la lógica.

4. State y Props: React utiliza dos conceptos importantes llamados state y props. State se refiere a los datos que son relevantes para un componente específico y pueden cambiar con el tiempo. Props, por otro lado, son argumentos que se pasan a un componente y no cambian dentro de él. Esto hace que sea fácil crear componentes reutilizables y asegurar la coherencia en toda la aplicación.

En resumen, React tiene una serie de características que lo diferencian de JavaScript vanilla. Los componentes, el Virtual DOM, JSX y la gestión de state y props son algunos de los fundamentos más importantes de React. Al utilizar estas características, es posible crear aplicaciones web modernas y eficientes que proporcionen una experiencia de usuario excepcional.

## Componentes

Los componentes son la base de React y se pueden describir como bloques de construcción independientes y reutilizables de una interfaz de usuario. Cada componente está compuesto por HTML (o JSX, una extensión de sintaxis de JavaScript para React), CSS y JavaScript (o TypeScript). Un componente puede tener uno o varios de los siguientes campos:

- Props: Son los argumentos que se pasan a un componente, pueden ser tanto strings, números, objetos, funciones, etc.

- State: Es un objeto que contiene los datos internos del componente y puede cambiar a lo largo del tiempo como resultado de alguna interacción.

- Métodos: Funciones que pueden ser definidas dentro del componente que luego pueden ser llamados para realizar alguna acción específica.

- Render: Método que devuelve la visualización del componente en el sitio web y puede ser heredado por otros componentes.

Los hooks, introducidos en React version 16.8, son una forma de hacer que los componentes funcionales de React tengan estado y otras características que antes sólo los componentes de clase tenían. Los hooks son funciones que te permiten "enganchar" o acceder al ciclo de vida de los componentes, y realizar otras tareas adicionales.

Algunos de los hooks más importantes son:

- useState: Te permite agregar estado a un componente funcional incluyendo una variable y una función actualizadora. 

- useEffect: Te permite ejecutar efectos secundarios (como tareas HTTP, operaciones DOM, etc.) después de renderizar el componente.

- useContext: Te permite compartir información entre componentes, creando un contexto que puede ser proveído a cualquier nivel de la estructura del componente.

- useMemo: Te permite optimizar la performance de la aplicación calculando valores únicos, y utiliza la técnica de memoización para guardar los últimos resultados.

- useRef: Te permite acceder al DOM y a otros elementos a los cuales no puedes acceder usando un estado normal.

En conclusión, los componentes son las piezas individuales de una interfaz de usuario en React, mientras que los hooks son funciones que permiten agregar características y tomar más control del ciclo de vida de los componentes funcionales en React. Juntos, los componentes y los hooks hacen React una librería muy potente para la construcción de aplicaciones web modernas y dinámicas.

## Hooks

Los hooks ofrecen varias ventajas con respecto a las clases en React:

1. Facilita la lógica reutilizable: Antes de los hooks, para reutilizar la lógica en distintos componentes en React, era necesario gestionar la complejidad utilizando patrones como Render Props o la HOC (Higher-order component). Esto resultaba en un código complejo y difícil de mantener. Los hooks ofrecen una solución más sencilla, ya que te permiten extraer lógica específica de un componente y reutilizarla en otros componentes de forma muy sencilla.

2. Fácil gestión del ciclo de vida: Los hooks te permiten controlar el ciclo de vida de los componentes de una manera más sencilla y explícita, lo que hace que sea más fácil mantener el código y evitar "efectos secundarios" no deseados. 

3. Más legibilidad del código: La sintaxis de los hooks es más simple y fácil de leer que la de las clases de React, lo que facilita la lectura y mantenimiento del código.

4. Permite el uso del estado en los componentes funcionales: Antes de los hooks, los componentes funcionales no tenían un estado interno y su uso estaba limitado a tareas simples. Ahora, los hooks te permiten agregar estado a los componentes funcionales, lo que hace posible que el código sea más limpio, legible y fácil de entender.

En resumen, los hooks permiten una gestión más sencilla y explícita del estado y del ciclo de vida de los componentes funcionales, lo que hace que el código sea más legible y reutilizable. Además, ofrecen una solución más limpia y fácil de usar en comparación con las clases. Por lo tanto, los hooks son la solución preferida para la mayoría de los desarrolladores de React hoy en día.

### Ejemplo 1

Este es un ejemplo de un componente de React que muestra un formulario sencillo con dos campos (`input`), y muestra el resultado de cada campo en un `h1` y `h2` respectivamente. Los `h1` y `h2` se encuentran en la parte superior, mientras que el formulario se encuentra debajo.

```jsx
import React, { useState } from 'react';

function Formulario() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');

  function handleUsernameChange(event) {
    setUsername(event.target.value);
  }

  function handleEmailChange(event) {
    setEmail(event.target.value);
  }

  return (
    <div>
      <h1>Nombre: {username}</h1>
      <h2>Email: {email}</h2>
      <form>
        <label>
          Nombre:
          <input type="text" value={username} onChange={handleUsernameChange} />
        </label>
        <br />
        <label>
          Email:
          <input type="text" value={email} onChange={handleEmailChange} />
        </label>
      </form>
    </div>
  );
}

export default Formulario;
```

En este ejemplo, estamos utilizando el hook `useState` para declarar un estado interno en nuestro componente para almacenar la información de los campos del formulario (`username` y `email`). También hemos creado dos funciones (`handleUsernameChange` y `handleEmailChange`) que serán llamadas cada vez que se modifique el valor de los campos del formulario mediante el evento `onChange`. Finalmente, se muestra la información ingresada en los campos del formulario mediante el `h1` y `h2` que se crearon en la parte superior del componente.

#Ejemplo 2

Aquí hay un ejemplo de cómo podemos modificar el componente anterior para que tenga un botón que permita al usuario cambiar entre ver el formulario y una imagen:

```jsx
import React, { useState } from 'react';

function Formulario() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [showForm, setShowForm] = useState(true); // Estado para mostrar/ocultar el formulario

  function handleUsernameChange(event) {
    setUsername(event.target.value);
  }

  function handleEmailChange(event) {
    setEmail(event.target.value);
  }

  function toggleForm() {
    setShowForm(!showForm);
  }

  return (
    <div>
      {showForm ? ( // Si showForm es true, mostrar el formulario
        <div>
          <h1>Nombre: {username}</h1>
          <h2>Email: {email}</h2>
          <form>
            <label>
              Nombre:
              <input type="text" value={username} onChange={handleUsernameChange} />
            </label>
            <br />
            <label>
              Email:
              <input type="text" value={email} onChange={handleEmailChange} />
            </label>
          </form>
        </div>
      ) : ( // Si showForm es false, mostrar la imagen
        <img src="https://via.placeholder.com/350x150" alt="Placeholder" />
      )}
      <br />
      <button onClick={toggleForm}>
        { showForm ? "Ver imagen" : "Ver formulario" }
      </button>
    </div>
  );
}

export default Formulario;
```

En este ejemplo, hemos agregado un nuevo estado `showForm`, que es un booleano que indica si el formulario o la imagen deben ser mostrados. Se muestra el formulario si `showForm` es verdadero, de lo contrario, se muestra la imagen. También se ha añadido un botón con el texto "Ver imagen" o "Ver formulario" según el estado actual del componente, que permite al usuario cambiar entre las dos pantallas. El botón hace uso de la función `toggleForm`, que cambia el valor de `showForm` usando `setShowForm` cuando se hace clic.

### Instalación

Para crear una aplicación de React sencilla usando `create-react-app`, sigue los siguientes pasos:

1. Instala Node.js en tu computadora si aún no lo has hecho. Puedes descargarlo desde el sitio oficial de Node.js: https://nodejs.org/en/.

2. Abre una terminal o línea de comandos y escribe el siguiente comando para instalar `create-react-app` a través de npm (el gestor de paquetes de Node.js):
  
   ```
   npm install -g create-react-app
   ```
   
   Este comando instala `create-react-app` de forma global en tu computadora, por lo que podrás usarlo en cualquier proyecto.

3. Crea una nueva aplicación de React ejecutando el comando `create-react-app` en la terminal:

   ```
   create-react-app my-app
   ```
   
   Este comando crea una nueva aplicación de React en una carpeta llamada `my-app`. Puedes cambiar este nombre por cualquier otro que desees.

4. Una vez que se haya creado la aplicación, ingresa al directorio utilizando el comando `cd`:

   ```
   cd my-app
   ```

5. Ahora puedes iniciar la aplicación en un servidor local ejecutando el siguiente comando:

   ```
   npm start
   ```
   
   Este comando iniciará la aplicación en tu navegador web predeterminado. Si todo va bien, deberías ver un mensaje de bienvenida.

¡Y eso es todo! Ahora tienes una aplicación de React básica en funcionamiento. Puedes empezar a escribir código dentro de la carpeta `src` de tu aplicación, y `create-react-app` se encargará de la compilación y otros detalles técnicos.

