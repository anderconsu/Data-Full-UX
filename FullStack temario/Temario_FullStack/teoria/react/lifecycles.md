# Lifecycles

Los lifecycles en React son una serie de métodos que se ejecutan en un componente React en diferentes etapas de su ciclo de vida. Estos métodos son útiles para realizar tareas en ciertas etapas del ciclo de vida del componente, como configuración, actualización y eliminación.

Hay tres fases principales del ciclo de vida de un componente React:

1. Montaje (mounting): Es cuando el componente es creado y agregado al DOM (Document Object Model).

2. Actualización (updating): Es cuando se realizan cambios en el componente, ya sea por cambios en las propiedades o en el estado.

3. Desmontaje (unmounting): Es cuando el componente es eliminado del DOM.

A continuación se muestran los principales métodos de ciclo de vida y sus casos de uso:

### Métodos de ciclo de vida de Montaje

- constructor(): Método que se ejecuta cuando se crea una instancia del componente. Se utiliza para inicializar el estado y enlazar los métodos a `this`.

```jsx
constructor(props) {
    super(props);
    this.state = { count: 0 };
    this.handleClick = this.handleClick.bind(this);
}
```

- render(): Método que devuelve el elemento JSX. Es obligatorio para todo componente React.

```jsx
render() {
    return (
        <div>
            <h1>Count: {this.state.count}</h1>
            <button onClick={this.handleClick}>Increment</button>
        </div>
    )
}
```

- componentDidMount(): Método que se ejecuta inmediatamente después del renderizado inicial del componente. Se utiliza para realizar peticiones a una API o establecer una animación.

```jsx
componentDidMount() {
    fetch('https://api.example.com/items')
        .then(response => response.json())
        .then(data => this.setState({ items: data }));
}
```

### Métodos de ciclo de vida de Actualización

- shouldComponentUpdate(): Método que se ejecuta antes de actualizar el componente. Se utiliza para mejorar el rendimiento del componente, evaluando si los cambios justifican una nueva renderización o no.

```jsx
shouldComponentUpdate(nextProps, nextState) {
    if (nextProps.color !== this.props.color) {
        return true;
    }
    if (nextState.count !== this.state.count) {
        return true;
    }
    return false;
}
```

- componentDidUpdate(): Método que se ejecuta después de actualizar el componente. Se utiliza para realizar actualizaciones en el DOM o para enviar datos a una API.

```jsx
componentDidUpdate(prevProps, prevState) {
    if (this.props.title !== prevProps.title) {
        document.title = this.props.title;
    }
}
```

### Métodos de ciclo de vida de Desmontaje

- componentWillUnmount(): Método que se ejecuta antes de que el componente sea eliminado. Se utiliza para realizar limpieza de datos, quitar eventos y cancelar peticiones.

```jsx
componentWillUnmount() {
    clearInterval(this.timerID);
}
```

Conociendo los métodos de ciclo de vida, podemos utilizarlos para realizar diferentes tareas en las diferentes etapas del ciclo de vida del componente, mejorando su rendimiento, control y funcionalidad.

Es importante destacar que a partir de React 16.3, algunos métodos están siendo marcados como obsoletos y se recomienda el uso de otros métodos en su lugar. Por ejemplo, `componentWillReceiveProps()` se ha marcado como obsoleto y se recomienda el uso de `static getDerivedStateFromProps()`. Por lo tanto, es recomendable mantenerse actualizado con las últimas versiones de React y las recomendaciones de la documentación oficial.