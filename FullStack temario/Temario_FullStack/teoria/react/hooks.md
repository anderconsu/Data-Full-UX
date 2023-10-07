# Hooks
Los Hooks son una característica introducida en React 16.8 que permiten usar el estado y otros features de React sin escribir clases. Los Hooks permiten a los desarrolladores trabajar con componentes funcionales y brindan una forma más limpia y concisa de escribir código. 

Algunos de los Hooks más populares son:

- useState: Este Hook permite agregar el estado de un componente funcional, dando la oportunidad de actualizar el estado y reflejar los cambios en la vista. 

    Ejemplo:
    
```javascript
import React, { useState } from 'react'

function App() {
  const [count, setCount] = useState(0)
  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  )
}
```

- useEffect: Este Hook permite realizar acciones cada vez que el componente es renderizado. 

    Ejemplo:
    
```javascript
import React, { useState, useEffect } from 'react'

function App() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    document.title = `You clicked ${count} times`
  })

  return (
    <div>
      <p>You clicked {count} times</p>
      <button onClick={() => setCount(count + 1)}>
        Click me
      </button>
    </div>
  )
}
```

- useContext: Este Hook permite compartir datos entre componentes sin tener que pasar los datos a través de props.

    Ejemplo:
    
```javascript
import React, { useContext } from 'react'
const ThemeContext = React.createContext('light')

function App() {
  return (
    <ThemeContext.Provider value="dark">
      <Toolbar />
    </ThemeContext.Provider>
  )
}

function Toolbar(props) {
  return (
    <div>
      <ThemedButton />
    </div>
  )
}

function ThemedButton() {
  const theme = useContext(ThemeContext)
  return <button>{theme}</button>
}
```

En general, los Hooks permiten una mejor organización del código, ya que cada característica de React se separa en pequeñas unidades reutilizables que pueden mejorar significativamente la calidad de un proyecto.

## Contexto

Para modificar el contexto desde un componente cualquiera es necesario utilizar el Hook useContext para obtener la función o variable que se quiere modificar, y luego, utilizando los parámetros de esa función, hacer el cambio al contexto.

Por ejemplo, si tenemos un contexto con un estado y una función que modifica ese estado:

```javascript
import { createContext, useState } from "react";

export const CounterContext = createContext({});

export const CounterContextProvider = ({ children }) => {
  const [count, setCount] = useState(0);
  const increment = (value) => {
    setCount(count + value);
  };
  return (
    <CounterContext.Provider value={{ count, increment }}>
      {children}
    </CounterContext.Provider>
  );
};
```

Podríamos utilizar esa función `increment` en cualquier componente que se encuentre dentro de `CounterContextProvider`. Para hacerlo, primero debemos obtener la función increment utilizando el Hook useContext:

```javascript
import { useContext } from "react";
import { CounterContext } from "./CounterContext";

const IncrementButton = () => {
  const { increment } = useContext(CounterContext);

  return <button onClick={() => increment(1)}>Increment</button>;
};
```

En este ejemplo, se utiliza el Hook useContext para obtener la función increment del contexto CounterContext, y luego, en el evento onClick del botón, llamamos a esa función con el valor 1 como parámetro para incrementar en 1 el contador.

De esta manera, podemos modificar el contexto desde cualquier componente conectado a él mediante el uso del Hook useContext.

Es importante tener en cuenta que solo se puede modificar el contexto desde los componentes que estén dentro del árbol de Componentes que tengan el proveedor del contexto, ya que el proveedor establece el valor inicial del contexto para los componentes hijas que estén en el árbol descendente.

Además, al modificar el contexto, todos los componentes que dependan de esa variable o función se actualizarán automáticamente, lo que significa que verán el nuevo valor del contexto sin tener que hacer nada extra. Esto es posible gracias a la naturaleza "reactiva" de React.

Es importante tener en cuenta que modificar el contexto en componentes que se encuentran demasiado lejos de la definición del contexto puede hacer que el código sea menos legible y difícil de depurar. Por lo tanto, es recomendable limitar su uso a situaciones muy específicas donde realmente sea necesario tener acceso al contexto desde un componente secundario especifico.

En resumen, para modificar el contexto desde cualquier componente, debemos seguir estos pasos:

1. Obtener la función o variable que queremos modificar utilizando el Hook useContext
2. Modificar la variable llamando la función con los valores apropiados
3. Los componentes que dependen de esa variable o función se actualizarán automáticamente.

En conclusión, los contextos son una herramienta muy útil en React para compartir variables y funciones entre componentes. Saber cómo modificar el contexto desde cualquier componente nos permite tener aún más control sobre cómo se comunican nuestros componentes y nos permite crear aplicaciones más escalables y organizadas.