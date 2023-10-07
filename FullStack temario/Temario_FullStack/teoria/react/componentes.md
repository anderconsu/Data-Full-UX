# Componentes

Los componentes son uno de los principales conceptos de React. En términos generales, los componentes son secciones reutilizables de un sitio web o aplicación. Se pueden pensar como elementos que tienen una función y que se utilizan muchas veces y en diferentes lugares en una página web.

Existen dos tipos de componentes en React: los componentes de clase y los componentes funcionales.

#### Componentes de clase:

Los componentes de clase son la forma antigua de crear componentes en React. Utilizan una sintaxis de ES6 para crear clases que extienden la clase "Component" de React.

Ejemplo de código de un componente de clase:

```javascript
import React, { Component } from 'react';

class MiComponente extends Component {
  render() {
    return (
      <div>
        <h1>Mi Componente</h1>
        <p>Este es un componente de clase en React.</p>
      </div>
    );
  }
}

export default MiComponente;
```

#### Componentes funcionales:

Los componentes funcionales son un tipo especial de componente que se introdujo con React Hooks. Son considerados la forma moderna de crear componentes en React y ofrecen una sintaxis más sencilla y fácil de usar que los componentes de clase.

Ejemplo de código de un componente funcional:

```javascript
import React from 'react';

const MiComponente = () => {
  return (
    <div>
      <h1>Mi Componente</h1>
      <p>Este es un componente funcional en React.</p>
    </div>
  );
};

export default MiComponente;
```

##### Diferencias clave entre componentes de clase y componentes funcionales:

- Los componentes de clase se crean mediante la extensión de la clase "Component" de React, mientras que los componentes funcionales son funciones normales de JavaScript que devuelven un valor JSX.
- Los componentes de clase tienen un método de ciclo de vida llamado "render" que se utiliza para definir lo que se muestra en pantalla en el componente, mientras que los componentes funcionales return un valor JSX dentro de la función.
- Los componentes funcionales no tienen estado, mientras que los componentes de clase sí tienen estado.

En resumen, los componentes son la unidad básica de construcción de una aplicación de React. Son secciones reutilizables de código que se pueden utilizar en diferentes partes de un sitio o aplicación, y pueden ser creados tanto como componentes de clase como componentes funcionales.