# Redux

Redux es una biblioteca de JavaScript utilizada para centralizar y controlar el estado de una aplicación web. Esta biblioteca sigue el patrón de arquitectura de flux que consiste en un flujo unidireccional de datos. Redux utiliza tres conceptos fundamentales para alcanzar este objetivo: store, actions y reducers.

- Store: Es el objeto que contiene todo el estado de la aplicación. El store es inmutable y sólo puede ser actualizado mediante acciones.
- Actions: Son objetos JavaScript que contienen información sobre un cambio que se llevará a cabo en el estado de la aplicación. Las acciones son una forma de enviar datos desde nuestra aplicación a nuestro store. Cada acción debe tener una propiedad "type" que indica el tipo de acción que se está llevando a cabo.
- Reducers: Son funciones puras que especifican cómo el estado de la aplicación debe cambiar en respuesta a una acción en particular. Reciben el estado actual de la aplicación y una acción, y devuelven un nuevo estado.

A continuación se muestra un ejemplo de cómo implementar Redux en una pequeña aplicación.

**index.js:**
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import App from './App';
import rootReducer from './reducers';

const store = createStore(rootReducer);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);
```

En este archivo creamos el store y lo envolvemos en un componente de proveedor (Provider) que se utiliza para hacer que el store esté disponible en toda la aplicación. También importamos la función createStore y el rootReducer.

**actions.js:**
```javascript
export const increaseCounter = () => {
  return {
    type: 'INCREASE_COUNTER'
  }
}

export const decreaseCounter = () => {
  return {
    type: 'DECREASE_COUNTER'
  }
}
```

En este archivo, creamos dos funciones de acción que incrementarán y decrementarán el valor del contador respectivamente.

**reducers.js:**
```javascript
const initialState = {
  counter: 0
};

const rootReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'INCREASE_COUNTER':
      return { ...state, counter: state.counter + 1 };
    case 'DECREASE_COUNTER':
      return { ...state, counter: state.counter - 1 };
    default:
      return state;
  }
}

export default rootReducer;
```

En este archivo, creamos el reducer que tomará el estado actual y una acción, y devolverá un nuevo estado. El contador se inicializa en 0 y se actualiza en función de la acción que se haya ejecutado.

**App.js:**
```javascript
import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { increaseCounter, decreaseCounter } from './actions';

function App() {
  const counter = useSelector(state => state.counter);
  const dispatch = useDispatch();

  return (
    <div>
      <h1>Contador: {counter}</h1>
      <button onClick={() => dispatch(increaseCounter())}>Incrementar</button>
      <button onClick={() => dispatch(decreaseCounter())}>Decrementar</button>
    </div>
  );
}

export default App;
```

En este archivo, utilizamos la función useSelector para leer el estado actual del store y la función useDispatch para mandar las acciones. Luego, renderizamos los botones que incrementarán y decrementarán el valor del contador en función de las acciones.

Este es un ejemplo básico de cómo implementar Redux en una pequeña aplicación. Redux es útil para aplicaciones de gran tamaño en las que la gestión del estado puede llegar a ser complicada y difícil de mantener.