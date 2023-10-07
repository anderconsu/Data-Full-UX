# Formularios

Los formularios son una parte fundamental de cualquier aplicación web que involucre la interacción del usuario. En React, los formularios son manejados mediante el uso de componentes controlados o no controlados.

## Componentes controlados

Los componentes controlados son aquellos en los que los valores de entrada son controlados por el estado del componente de React. Esto significa que el estado de React es la "fuente de verdad" para el valor de la entrada, y cualquier cambio en el estado se refleja en la entrada.

A modo de ejemplo, aquí se muestra un formulario de inicio de sesión en React utilizando componentes controlados:

```jsx
import React, { useState } from 'react';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    // Aquí puedes hacer la lógica necesaria para enviar la información del formulario al servidor
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </label>
      <label>
        Contraseña:
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label>
      <button type="submit">Iniciar sesión</button>
    </form>
  );
}

export default LoginForm;
```

En el ejemplo de código, se utiliza el hook `useState` para inicializar el estado del componente con los valores `email` y `password`. Luego, se define una función `handleSubmit` que se ejecuta cuando el usuario presiona el botón de `submit`.

Finalmente, se renderiza el formulario, incluyendo dos entradas de texto y un botón. Cada entrada de texto se define con un atributo `value` que está vinculado al estado del componente utilizando `useState`, y un controlador de eventos `onChange` que actualiza el estado del componente cuando el usuario cambia el texto de entrada.

## Componentes no controlados

Los componentes no controlados son aquellos en los que los valores de entrada son manejados por el DOM en lugar del estado del componente de React. Esto significa que el DOM es la "fuente de verdad" para el valor de la entrada, y cualquier cambio en la entrada no se refleja en el estado.

A modo de ejemplo, aquí se muestra un formulario de inicio de sesión en React utilizando componentes no controlados:

```jsx
import React from 'react';

function LoginForm() {
  const handleSubmit = (event) => {
    event.preventDefault();
    // Aquí puedes hacer la lógica necesaria para enviar la información del formulario al servidor
    const email = event.target.email.value;
    const password = event.target.password.value;
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Email:
        <input type="email" name="email" />
      </label>
      <label>
        Contraseña:
        <input type="password" name="password" />
      </label>
      <button type="submit">Iniciar sesión</button>
    </form>
  );
}

export default LoginForm;
```

En este ejemplo, no se utiliza el estado del componente para controlar los valores de entrada. En cambio, se define una función `handleSubmit` que se ejecuta cuando el usuario presiona el botón de `submit`. En esta función, se accede a los valores de entrada utilizando `event.target.email.value` y `event.target.password.value`.

## Casos de uso

Los formularios se utilizan comúnmente para recolectar información del usuario, como en el caso de un formulario de inicio de sesión, formulario de registro, formulario de contacto, entre otros. Los formularios también se pueden utilizar para filtrar datos o para enviar datos al servidor para su procesamiento.

Por ejemplo, un formulario de filtro de productList que filtra por categoría podría tener la siguiente implementación:

```jsx
import React, { useState } from 'react';
import ProductList from './ProductList';

function FilterForm() {
  const [category, setCategory] = useState('');
  const [products, setProducts] = useState([]);

  const handleSubmit = (event) => {
    event.preventDefault();
    // Aquí puedes hacer una petición al servidor para obtener los productos filtrados según la categoría
    const filteredProducts = [{ name: 'Product 1', category: 'category1' }, { name: 'Product 2', category: 'category1' }];
    setProducts(filteredProducts);
  }

  return (
    <>
      <form onSubmit={handleSubmit}>
        <label>
          Filtrar por categoría:
          <input type="text" value={category} onChange={(e) => setCategory(e.target.value)} />
        </label>
        <button type="submit">Filtrar</button>
      </form>
      <ProductList products={products} />
    </>
  );
}

export default FilterForm;
```

En este ejemplo, se utiliza el estado `category` para mantener el valor de búsqueda del usuario, y el estado `productos` para almacenar los productos filtrados. Cuando el usuario presiona el botón de `submit`, se ejecuta `handleSubmit`, que realiza una solicitud para obtener los productos filtrados y los actualiza en el estado del componente. Finalmente, se renderiza el componente `ProductList`, que muestra los productos filtrados si existen en el estado del componente.