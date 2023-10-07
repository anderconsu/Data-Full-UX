# Sequelize

Sequelize es un ORM (Object-Relational Mapping) para Node.js que nos permite trabajar con bases de datos relacionales utilizando JavaScript sin necesidad de tener conocimientos profundos en SQL. Sequelize nos facilita la creación de modelos, relaciones, validaciones, consultas y migraciones en nuestras bases de datos.

Algunas de sus características principales son:

- Soporte para varios dialectos de SQL (MySQL, PostgreSQL, SQL Server, etc.).
- Mapeo de tablas y columnas a modelos y atributos.
- Relaciones entre modelos (uno a uno, uno a muchos, muchos a muchos).
- Métodos convenientes para realizar consultas comunes (findAll, findOne).
- Validaciones de datos antes de guardarlos en la base de datos.
- Migraciones para actualizar la estructura de la base de datos de manera sencilla.

Para utilizar Sequelize en nuestro proyecto de Node.js, lo primero que debemos hacer es instalarlo con npm:

```bash
npm install sequelize
```

Luego necesitamos definir los modelos que representarán nuestras tablas en la base de datos. Por ejemplo, si tenemos una tabla de usuarios con las columnas `id`, `nombre`, `email` y `contraseña`, nuestro modelo de Sequelize se vería así:

```javascript
import { DataTypes } from 'sequelize';
import db from '../config/database.js';

const Usuario = db.define('usuario', {
  id: {
    type: DataTypes.INTEGER,
    allowNull: false,
    primaryKey: true,
    autoIncrement: true
  },
  nombre: {
    type: DataTypes.STRING,
    allowNull: false
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true
  },
  contrasena: {
    type: DataTypes.STRING,
    allowNull: false
  }
});

export default Usuario;
```

En este ejemplo, estamos definiendo el modelo `Usuario` que representa la tabla `usuarios` en la base de datos. Estamos utilizando `DataTypes` para especificar el tipo de datos de cada columna y `allowNull` para indicar si la columna puede contener valores nulos. También estamos utilizando `primaryKey` y `autoIncrement` para indicar que la columna `id` es la clave primaria y se autoincrementa automáticamente. Por último, estamos utilizando `unique` para indicar que la columna `email` debe contener valores únicos.

Una vez que hemos definido nuestros modelos, podemos utilizar Sequelize para realizar consultas en la base de datos. Por ejemplo, para encontrar todos los usuarios cuyo nombre es "Juan", podemos hacer lo siguiente:

```javascript
import Usuario from '../models/usuario';

Usuario.findAll({
  where: {
    nombre: 'Juan'
  }
}).then((usuarios) => {
  console.log(usuarios);
}).catch((error) => {
  console.log(error);
});
```

En este ejemplo, estamos utilizando `findAll` para encontrar todos los usuarios que cumplan con la condición especificada en `where`. Luego, estamos utilizando una promesa para manejar el resultado de la consulta. Si la consulta se realiza correctamente, imprimimos los usuarios en la consola. Si ocurre algún error, lo imprimimos también.

En resumen, Sequelize nos facilita el trabajo con bases de datos relacionales en Node.js al proporcionarnos herramientas para definir modelos, relaciones, consultas y migraciones.

Sequelize nos permite definir diferentes tipos de relaciones entre tablas de manera sencilla. A continuación, se explican los tres tipos principales de relaciones:

### One-to-one (uno a uno)

En una relación de uno a uno, una fila de una tabla se relaciona con exactamente una fila de otra tabla y viceversa. Por ejemplo, si tenemos una tabla de usuarios y una tabla de perfiles, donde cada usuario tiene un perfil asociado, podríamos definir la relación así:

```javascript
// definimos el modelo del usuario
const Usuario = sequelize.define('usuario', {
  // atributos del usuario
});

// definimos el modelo del perfil
const Perfil = sequelize.define('perfil', {
  // atributos del perfil
});

// definimos la relación uno a uno
Usuario.hasOne(Perfil);
Perfil.belongsTo(Usuario);
```

En este ejemplo, estamos utilizando `hasOne` para indicar que un usuario tiene un perfil y `belongsTo` para indicar que un perfil pertenece a un usuario. Esto creará una clave foránea en la tabla de perfiles que referencia la clave primaria de la tabla de usuarios.

### One-to-many (uno a muchos)

En una relación de uno a muchos, una fila de una tabla se relaciona con varias filas de otra tabla, pero cada fila de la segunda tabla se relaciona con solo una fila de la primera tabla. Por ejemplo, si tenemos una tabla de cursos y una tabla de estudiantes, donde cada curso tiene varios estudiantes asociados, podríamos definir la relación así:

```javascript
// definimos el modelo del curso
const Curso = sequelize.define('curso', {
  // atributos del curso
});

// definimos el modelo del estudiante
const Estudiante = sequelize.define('estudiante', {
  // atributos del estudiante
});

// definimos la relación uno a muchos
Curso.hasMany(Estudiante);
Estudiante.belongsTo(Curso);
```

En este ejemplo, estamos utilizando `hasMany` para indicar que un curso tiene varios estudiantes y `belongsTo` para indicar que un estudiante pertenece a un curso. Esto creará una clave foránea en la tabla de estudiantes que referencia la clave primaria de la tabla de cursos.

### Many-to-many (muchos a muchos)

En una relación de muchos a muchos, varias filas de una tabla se relacionan con varias filas de otra tabla. Para hacer esto, necesitamos crear una tercera tabla que relacione las dos tablas originales. Por ejemplo, si tenemos una tabla de estudiantes y una tabla de profesores, donde cada estudiante puede tener varios profesores y cada profesor puede tener varios estudiantes, podríamos definir la relación así:

```javascript
// definimos el modelo del estudiante
const Estudiante = sequelize.define('estudiante', {
  // atributos del estudiante
});

// definimos el modelo del profesor
const Profesor = sequelize.define('profesor', {
  // atributos del profesor
});

// definimos la relación muchos a muchos
Estudiante.belongsToMany(Profesor, { through: 'estudiantes_profesores' });
Profesor.belongsToMany(Estudiante, { through: 'estudiantes_profesores' });
```

En este ejemplo, estamos utilizando `belongsToMany` para indicar que tanto los estudiantes como los profesores pueden pertenecer a varios de los otros. La opción `through` especifica el nombre de la tabla intermedia que se utilizará para almacenar las relaciones. En este ejemplo, la tabla se llamará `estudiantes_profesores`.

En resumen, Sequelize nos proporciona métodos intuitivos para definir diferentes tipos de relaciones entre tablas, lo que facilita el trabajo con bases de datos relacionales en nuestras aplicaciones Node.js.

## Referencias

- [Sequelize](https://sequelize.org/)
- [Sequelize - Getting Started](https://sequelize.org/master/manual/getting-started.html)