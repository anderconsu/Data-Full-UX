MVC (Modelo-Vista-Controlador) es un patrón de diseño arquitectónico ampliamente utilizado en el desarrollo de aplicaciones web. Consiste en dividir una aplicación en tres componentes principales: el Modelo, la Vista y el Controlador.

- **Modelo**: El modelo representa los datos y la lógica de negocio de la aplicación. Es responsable de la gestión y manipulación de los datos, así como de realizar todas las operaciones relacionadas con la lógica de negocio. En el contexto de Node.js, el modelo puede consistir en clases, funciones y módulos que se encarguen de interactuar con la base de datos u otras fuentes de datos.

- **Vista**: La vista se encarga de mostrar la información al usuario. Es responsable de la interfaz de usuario y de la presentación de los datos al usuario final. En el contexto de Node.js, la vista puede consistir en archivos HTML, plantillas, componentes de interfaz de usuario, etc.

- **Controlador**: El controlador actúa como intermediario entre el modelo y la vista. Es responsable de recibir las solicitudes del usuario, interactuar con el modelo para obtener los datos necesarios y enviarlos a la vista para su presentación. También se encarga de manejar eventos, validaciones y cualquier otra lógica relacionada con la interacción usuario-aplicación. En el contexto de Node.js, los controladores son generalmente funciones que se encargan de manejar las rutas y las solicitudes HTTP.

A continuación se muestra un ejemplo de cómo implementar el patrón MVC en Node.js:

```javascript
// app.js

import express from 'express';
const app = express();

// Controladores
import userController from './controllers/userController';

// Rutas
app.get('/users', userController.getAllUsers);
app.get('/users/:id', userController.getUserById);
app.post('/users', userController.createUser);
app.put('/users/:id', userController.updateUser);
app.delete('/users/:id', userController.deleteUser);

// Iniciar la aplicación
app.listen(3000, () => {
  console.log('La aplicación está corriendo en el puerto 3000');
});
```

```javascript
// controllers/userController.js

import userModel from '../models/userModel';

// Obtener todos los usuarios
const getAllUsers = async (req, res) => {
  try {
    const users = await userModel.getAll();
    res.json(users);
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al obtener los usuarios' });
  }
}

// Obtener un usuario por ID
const getUserById = async (req, res) => {
  try {
    const user = await userModel.getById(req.params.id);
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al obtener el usuario' });
  }
}

// Crear un nuevo usuario
const createUser = async (req, res) => {
  try {
    const newUser = await userModel.create(req.body);
    res.json(newUser);
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al crear el usuario' });
  }
}

// Actualizar un usuario existente
const updateUser = async (req, res) => {
  try {
    const updatedUser = await userModel.update(req.params.id, req.body);
    res.json(updatedUser);
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al actualizar el usuario' });
  }
}

// Eliminar un usuario
const deleteUser = async (req, res) => {
  try {
    await userModel.delete(req.params.id);
    res.json({ message: 'Usuario eliminado correctamente' });
  } catch (error) {
    res.status(500).json({ error: 'Ocurrió un error al eliminar el usuario' });
  }
}

export default {
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser
}
```

```javascript
// models/userModel.js

// Simulando una base de datos con un array de usuarios
const users = [
  { id: 1, name: 'John Doe', email: 'john@example.com' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com' },
];

// Obtener todos los usuarios
const getAll = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(users);
    }, 1000);
  });
};

// Obtener un usuario por ID
const getById = (id) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const user = users.find(user => user.id === parseInt(id));
      if (user) {
        resolve(user);
      } else {
        reject();
      }
    }, 1000);
  });
};

// Crear un nuevo usuario
const create = (newUser) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const id = users.length + 1;
      const user = { id, ...newUser };
      users.push(user);
      resolve(user);
    }, 1000);
  });
};

// Actualizar un usuario existente
const update = (id, updatedUser) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const index = users.findIndex(user => user.id === parseInt(id));
      if (index !== -1) {
        const user = { id: parseInt(id), ...updatedUser };
        users[index] = user;
        resolve(user);
      } else {
        reject();
      }
    }, 1000);
  });
};

// Eliminar un usuario
const remove = (id) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const index = users.findIndex(user => user.id === parseInt(id));
      if (index !== -1) {
        users.splice(index, 1);
        resolve();
      } else {
        reject();
      }
    }, 1000);
  });
};

export default {
  getAll,
  getById,
  create,
  update,
  remove
};
```


En este ejemplo, el archivo `app.js` es el punto de entrada de la aplicación y se encarga de definir las rutas y los controladores asociados a cada ruta. El archivo `userController.js` contiene los controladores que se encargan de manejar las solicitudes y respuestas HTTP relacionadas con los usuarios. El archivo `userModel.js` representa el modelo y es responsable de realizar las operaciones relacionadas con los usuarios en la "base de datos" simulada.

En resumen, el patrón MVC en Node.js permite organizar y estructurar una aplicación de manera modular y escalable, separando las responsabilidades en diferentes componentes. La utilización de este patrón facilita el mantenimiento, la reutilización de código y la legibilidad del código.

## Referencias

- [MDN](https://developer.mozilla.org/es/docs/Glossary/MVC)
- [Wikipedia](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador)
- [GeeksforGeeks](https://www.geeksforgeeks.org/mvc-design-pattern/)
- [GeeksforGeeks js](https://www.geeksforgeeks.org/model-view-controllermvc-architecture-for-node-applications/)