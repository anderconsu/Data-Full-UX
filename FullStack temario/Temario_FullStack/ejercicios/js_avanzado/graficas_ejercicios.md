# Gráficas con Chart.js
##### Ejercicio 1: Crear una gráfica de barras

Crear una gráfica de barras que muestre el número de ventas de productos en un determinado periodo de tiempo. La gráfica debe tener título, etiquetas en el eje X e Y y una leyenda para identificar cada producto. Utiliza datos ficticios y muestra en la gráfica al menos 3 productos.

```javascript
// Datos de prueba
const data = {
  labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
  datasets: [
    {
      label: 'Producto 1',
      data: [12, 19, 3, 5, 2],
      backgroundColor: 'rgba(255, 99, 132, 0.2)'
    },
    {
      label: 'Producto 2',
      data: [3, 5, 2, 3, 1],
      backgroundColor: 'rgba(54, 162, 235, 0.2)'
    },
    {
      label: 'Producto 3',
      data: [7, 8, 2, 6, 4],
      backgroundColor: 'rgba(255, 206, 86, 0.2)'
    }
  ]
};

const config = {
  type: 'bar',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Ventas por mes'
      }
    },
    scales: {
      x: {
        stacked: true,
      },
      y: {
        stacked: true
      }
    }
  }
};

// Creación de la gráfica
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);
```

##### Ejercicio 2: Crear una gráfica de línea

Crear una gráfica de línea que muestre la evolución del precio de una acción en bolsa en un determinado periodo de tiempo. La gráfica debe tener título, etiquetas en el eje X e Y y un color que identifique la línea. Utiliza datos ficticios y muestra en la gráfica al menos 2 años de datos.

```javascript
// Datos de prueba
const data = {
  labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'],
  datasets: [
    {
      label: 'Precio de la acción',
      data: [140, 135, 139, 145, 153, 148, 152, 156, 160, 155, 165, 172],
      fill: false,
      borderColor: 'rgb(75, 192, 192)',
      tension: 0.1
    }
  ]
};

const config = {
  type: 'line',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Precio de la acción durante el año'
      }
    },
    scales: {
      x: {
        title: {
          display: true,
          text: 'Meses'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Precio ($)'
        }
      }
    }
  }
};

// Creación de la gráfica
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);
```

##### Ejercicio 3: Crear una gráfica de pastel

Crear una gráfica de pastel que muestre la distribución del presupuesto de una empresa en diferentes áreas. La gráfica debe tener título y etiquetas para identificar cada área. Utiliza datos ficticios y muestra en la gráfica al menos 4 áreas.

```javascript
// Datos de prueba
const data = {
  labels: ['Marketing', 'Desarrollo', 'Ventas', 'Contabilidad'],
  datasets: [
    {
      label: 'Presupuesto',
      data: [20000, 30000, 25000, 15000],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)'
      ],
      borderWidth: 1
    }
  ]
};

const config = {
  type: 'pie',
  data: data,
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Distribución del presupuesto'
      }
    }
  }
};

// Creación de la gráfica
const myChart = new Chart(
  document.getElementById('myChart'),
  config
);
```