# CSS Modules

CSS Modules es una técnica de estilización de CSS que permite a los desarrolladores tener un alcance global en sus estilos, a la vez que los encapsula en un archivo específico para cada componente, nivelándolos de manera individual. Esta separación de los estilos permite evitar conflictos entre diferentes clases CSS que se utilizan en componentes diferentes. 

Es la forma de escribir CSS que se enfoca en el resultado de diseñar una aplicación web segura, robusta y escalable. La estructura de CSS Modules se basa en la idea de que cada elemento visual en una aplicación web debe ser tratado como un componente.

Considera este ejemplo: 

```css
.btn {
  background: blue;
  color: white;
  font-size: 1rem;
}

.btn:hover {
  background: white;
  color: blue;
  border: 1px solid blue;
}
```
Este botón tiene dos estados: normal y hover (sobre la cual el usuario interactúa con el cursor). Puede ser se puede reutilizar en otras partes de la aplicación.

Pero, ¿Qué sucede si hay dos botones en la misma página con el mismo aspecto? Una buena práctica es crear una clase más específica para el botón nuevo de este tipo, algo como .button-blue. Pero, ¿Qué pasa si se necesitan cinco  versiones diferentes del  botón para diferentes secciones de la aplicación?

En general, el uso de CSS se vuelve más difícil a medida que la aplicación web crece. Si los estilos son un factor importante en el proyecto, se pueden encontrar muchos problemas:

* Sobrescribir estilos sin querer en diferentes secciones de la aplicación.
* Conflictos sobre el orden de los estilos. 
* Debugging más complicado porque los estilos pueden ser difíciles de rastrear.
* La escalabilidad se vuelve más difícil a medida que el archivo CSS crece.

CSS Modules aborda estos problemas vinculando CSS a un módulo específico de JavaScript y creando el estilo individual en un archivo aparte. 

Ejemplo: 

```jsx
import styles from './mymodule.module.css';

function MyComponent() {
  return <button className={styles.btn}>Click me</button>;
}
```

En su archivo CSS, podría haber instrucciones CSS para estilizar el botón. 

```css
.btn {
  background-color: blue;
  color: white;
  padding: 1rem 2rem;
  font-size: 1.4rem;
}
```

Este archivo se guarda con la extensión .module.css. 

Cada archivo CSS se limita a un ámbito y contiene solo los estilos definidos como  clases. Todos los nombres de clases en un archivo CSS se convierten automáticamente en únicos. 

```css
.btn_mymodule_287q {
  background-color: blue;
  color: white;
  padding: 1rem 2rem;
  font-size: 1.4rem;
}

.btn_mymodule_287q:hover {
  background-color: white;
  color: blue;
  border: 2px solid blue;
}
```

Aquí, el identificador `_mymodule_287q` es una cadena generada aleatoriamente que evita la colisión de nombres de clases en diferentes módulos. 

En resumen, las ventajas de usar CSS Modules son:

* Asegurar que los estilos solo sean aplicados donde queremos, sin interferir con otros estilos.
* Crear nombres de clase exclusivos al encapsular todo en un objeto de Javascript.
* Hacer que suponga menos problemas encontrar y resolver errores de estilización en el proyecto.
* Hacer crecer la aplicación más fácil, con un CSS mucho más modular.

En general, CSS Modules es una buena práctica para la estilización de una aplicación web, mejorando la facilidad de escritura CSS y haciéndola fácil de mantener.
Sass es un preprocesador de CSS que permite escribir CSS en un lenguaje más intuitivo y avanzado, con características adicionales como variables, anidamiento, mixins, entre otros, para mejorar la legibilidad y la facilidad de mantenimiento del código CSS.

# SASS

En React, Sass se puede integrar fácilmente en el proyecto creando un archivo `.scss` en la carpeta del componente. Para utilizar Sass en React es necesario instalar el paquete `node-sass` a través de npm. 

A continuación se presenta un ejemplo de cómo se podría utilizar Sass en un componente de React.

```jsx
import React from 'react';
import './Button.scss';

const Button = ({ text }) => {
  return (
    <button className="button">
      {text}
    </button>
  );
};

export default Button;
```
En este ejemplo, utilizamos Sass para crear estilos para el botón. El archivo Sass para el botón se encuentra en `Button.scss`, y se importa en el componente mediante la línea: `import './Button.scss';`

El archivo `Button.scss` podría tener la siguiente estructura:

```scss
$primary-color: #007bff;

.button {
  background-color: $primary-color;
  border: none;
  border-radius: 5px;
  color: white;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;

  &:hover {
    background-color: darken($primary-color, 10%);
  }
}
```
En este ejemplo, utilizamos el operador `&` para hacer referencia a la clase `.button` en su estado normal y su estado hover. 

También se utiliza la variable `$primary-color` para simplificar la definición del color principal del botón, lo que permite cambiar fácilmente el color en un solo lugar sin tener que cambiarlo en todo el archivo SCSS.

Además, se puede utilizar anidamiento para hacer que el archivo SCSS se vea más organizado, lo que facilita su mantenimiento en el futuro.

En resumen, Sass es una herramienta esencial para la estilización de aplicaciones web en React, que permite escribir CSS de manera más intuitiva y avanzada. Los casos de uso específicos incluyen:

* Utilizar variables para aplicar cambios globales en estilos y permitir un mantenimiento más sencillo.
* Utilizar anidamiento para mantener una estructura organizada y fácil de leer.
* Utilizar mixins para reutilizar estilos y mejorar la reutilización de código.
* Utilizar directamente funciones de Sass como `darken` para aplicar cambios dinámicos a los estilos. 

En general, el uso de Sass permite un código CSS más sencillo y mantenible, lo que facilita la tarea de mantener la consistencia y el diseño de una aplicación web.

Es posible combinar el uso de Sass y CSS Modules en un proyecto de React. Esto permite utilizar lo mejor de ambos enfoques para escribir estilos más avanzados y evitar la interferencia entre ellos.

El uso de Sass y CSS Modules en combinación puede ser útil en los siguientes casos:

1. Estilos globales: el uso de Sass permite definir estilos globales para toda la aplicación que no están limitados a un componente en particular y pueden ser reutilizados en toda la aplicación. Por otro lado, CSS Modules permite definir estilos específicos para un componente en particular y evitar que las clases definidas en un componente afecten a otro componente.

2. Personalización de temas: el uso de Sass permite definir variables que se pueden utilizar en toda la aplicación para definir los colores, fuentes y otros estilos básicos. Luego, utilizando CSS Modules, se pueden personalizar los temas de los componentes de manera individual.

3. Estilos complejos: el uso de Sass permite crear estilos más avanzados, como mixins y funciones, mientras que CSS Modules puede usarse para definir estilos específicos de un componente en particular y hacer que estos estilos complejos sean más manejables.

A continuación se presenta un ejemplo de cómo se pueden combinar Sass y CSS Modules en un proyecto de React: 

```scss
// Button.scss
$primary-color: #007bff;
$btn-border-radius: 5px;

.button {
  background-color: $primary-color;
  border: none;
  border-radius: $btn-border-radius;
  color: white;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
}

// Button.module.css
.btn {
  composes: button from './Button.scss';
  
  &:hover {
    background-color: darken($primary-color, 10%);
  }
}
```

En este ejemplo, se definen las variables globales en el archivo Sass `Button.scss`, que se utilizan en los estilos de la clase `.button`. Luego, en el archivo CSS Modules `Button.module.css`, se utiliza la propiedad `composes` para utilizar los estilos de la clase `.button` definida en `Button.scss`. 

Además, se utiliza la función de Sass `darken` para modificar el color de fondo del botón al pasar el cursor por encima.

En resumen, combinar el uso de Sass y CSS Modules permite poder sacar lo mejor de ambos enfoques para la estilización en proyectos de React. Sass puede usarse para definir estilos más avanzados y globales, mientras que CSS Modules puede usarse para definir estilos específicos de un componente en particular y evitar la interferencia entre componentes.
