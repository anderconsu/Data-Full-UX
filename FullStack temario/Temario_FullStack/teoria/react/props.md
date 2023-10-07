# Props

En React, `props` es una forma de pasar datos desde un componente padre a sus componentes hijos. `props` es un objeto que contiene pares de valores clave que representan las propiedades que se pasan a un componente.

A continuación, se presenta un ejemplo de un componente de `Button` que recibe `props` como el `texto` a ser mostrado en el botón y un `manejador de eventos onClick`.

```jsx
import React from 'react';

const Button = (props) => {
  return (
    <button onClick={props.onClick}>
      {props.text}
    </button>
  );
};

export default Button;
```

El component `Button` utiliza `props` para renderizar el texto y manejar eventos `onClick` al hacer click en el botón. Este componente puede ser utilizado en otro componente padre de la siguiente manera:

```jsx
import React from 'react';
import Button from './Button';

const ParentComponent = () => {
  const handleClick = () => {
    console.log('Button was clicked.');
  };

  return (
    <div>
      <Button text="Click me" onClick={handleClick} />
    </div>
  );
};

export default ParentComponent;
```

El componente `ParentComponent` está utilizando el componente `Button` y le está pasando propiedades `text` y `onClick` mediante `props`. Al hacer click en el botón, se ejecuta el método `handleClick` definido en el componente `ParentComponent`.

Los casos de uso de `props` son variados y se pueden utilizar en diferentes situaciones. Algunos casos de uso comunes incluyen:

- Pasar datos dinámicos a los componentes hijos.
- Pasar manejadores de eventos desde el componente padre para ser utilizados en los hijos.
- Configurar estilos para los componentes hijos.
- Enviar información de control de accesibilidad a los componentes. 

En resumen, `props` es una forma de comunicar datos entre componentes en React. Esto permite que los componentes sean flexibles y reutilizables, ya que pueden ser configurados y personalizados para adaptarse a diferentes situaciones.

En React también es posible desestructurar los `props` dentro de la función del componente directamente. Esto permite que las propiedades puedan ser accedidas directamente como variables dentro del componente, en vez de mediante el objeto `props`. A continuación, se presenta un ejemplo del componente `Button` utilizando la desestructuración de props:

```jsx
import React from 'react';

const Button = ({ text, onClick }) => {
  return (
    <button onClick={onClick}>
      {text}
    </button>
  );
};

export default Button;
```

En este ejemplo, la función del componente `Button` está tomando un objeto con dos propiedades: `text` y `onClick`. La desestructuración del objeto de `props` ocurre de manera explícita en el paréntesis anterior a la flecha `=>`. Por lo tanto, dentro del componente podemos utilizar directamente las variables `text` y `onClick` en vez de `props.text` y `props.onClick`.

El componente puede ser utilizado de la misma manera que el ejemplo anterior, mediante la creación de una instancia del componente y pasando las propiedades dentro de los corchetes, como se muestra a continuación:

```jsx
import React from 'react';
import Button from './Button';

const ParentComponent = () => {
  const handleClick = () => {
    console.log('Button was clicked.');
  };

  return (
    <div>
      <Button text="Click me" onClick={handleClick} />
    </div>
  );
};

export default ParentComponent;
```

En este ejemplo, la instancia del componente `Button` recibe dos propiedades (`text` y `onClick`) que son utilizadas en el componente para renderizar el botón y manejar el evento `onClick`. La diferencia radica en que ya no es necesario utilizar el objeto `props` para acceder a las propiedades.