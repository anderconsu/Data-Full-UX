# React Router

React Router es una librería de enrutamiento para aplicaciones web desarrolladas con React. Su principal objetivo es ofrecer una forma sencilla y flexible para manejar la navegación en aplicaciones de una sola página (SPA).

Básicamente, React Router permite mapear las diferentes rutas de una aplicación con los componentes correspondientes que se renderizarán en la pantalla. Esto significa que cada ruta puede tener su propio componente y esto se puede definir con la ayuda de React Router.

Para utilizar React Router, primero debe instalarse mediante el siguiente comando:

```
npm install react-router-dom
```

Una vez instalado, podemos comenzar a utilizar sus componentes. El componente más importante de React Router es `BrowserRouter`, el cual debe envolver a toda la aplicación. Por ejemplo:

```jsx
import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';

import Home from './Home';
import About from './About';

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
          </ul>
        </nav>

        <Route path="/" exact component={Home} />
        <Route path="/about" component={About} />
      </div>
    </BrowserRouter>
  );
}

export default App;
```

En este ejemplo, importamos los componentes `BrowserRouter`, `Route` y `Link` desde `react-router-dom`. Luego, dentro de `BrowserRouter`, definimos un `nav` que contiene enlaces de navegación utilizando el componente `Link`.

En el siguiente fragmento de código, definimos dos rutas utilizando el componente `Route`. La primera ruta es la raíz del sitio (`/`), que renderizará el componente `Home`. La segunda ruta es `/about`, que renderizará el componente `About`.

```jsx
<Route path="/" exact component={Home} />
<Route path="/about" component={About} />
```

En resumen, React Router es una herramienta vital para mejorar la navegación en una SPA, permitiendo especificar rutas de forma clara y sencilla.

En React Router, la propiedad `exact` se utiliza para indicar que la ruta especificada debe coincidir exactamente con la URL actual del navegador.

Por ejemplo, si definimos una ruta como `path="/"`, esto coincidiría con cualquier ruta que comience con un slash (por ejemplo: "/", "/about", "/products", etc.). Sin embargo, si añadimos la propiedad `exact` como `exact path="/"`, esto solo coincidirá con la URL exacta de la página principal (es decir, solo con la ruta "/").

Veamos un ejemplo de esto:

```jsx
import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/about">About</Link>
            </li>
          </ul>
        </nav>

        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
      </div>
    </BrowserRouter>
  );
}

export default App;
```

En este ejemplo, al agregar la propiedad `exact` a la ruta de inicio, especificamos que solo coincidirá con la URL exacta "/", en lugar de cualquier ruta que comience con "/".