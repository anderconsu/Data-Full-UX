# Crear una aplicación web con Node.js y MySQL

## Paso 1: Dockerizar la aplicación

Podemos crear un Dockerfile como este:
En `Dockerfile`
```Dockerfile
FROM node:latest

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "start" ]
```

Además de esto, deberiamos tener un docker-compose con servicios para node y mysql:
En `docker-compose.yml`
```yaml
version: '3'
services:  

  node:
    build: .
    volumes:
      - .:/app
    ports:
      - 3000:3000
    depends_on:
      - mysql

  mysql:
    image: mysql:latest
    volumes:
      - mysql:/var/lib/mysql
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=database
    ports:
      - "3306:3306"

volumes:
    mysql:
```
Ahora para correr todo usa docker-compose con `docker-compose up --build`.


## Paso 2: Crear un nuevo proyecto Node.js

* Para crear un nuevo proyecto, abre el terminal en una carpeta donde quieras alojar el proyecto y escribe:

```bash
npm init -y
```

Esto creará un archivo `package.json` en tu directorio.

* Después modificamos el archivo `package.json` para poner que es un m´dulo de tipo ES6:

```json
{
  "type": "module"
}
```

* Creamos el script de inicio en `package.json`:

```json
{
  "scripts": {
    "start": "nodemon src/index.js"
  }
}
```

Ejemplo:

```json
{
  "name": "node-mysql",
  "version": "1.0.0",
  "description": "Node.js and MySQL",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "nodemon src/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

## Paso 3: Instalar dependencias

Debajo están los paquetes que vas a necesitar:

```bash
npm install dotenv express cors bcrypt sequelize mysql2 jsonwebtoken pug cors express-session

npm install --save-dev nodemon
```

## Paso 4: Configurar estructura del proyecto

Crearemos las siguientes carpetas y archivos:

```
- src
 - models
 - routes
 - services
 - middleware
 - views
 - config
- .env
- docker-compose.yml 
- .dockerignore
- Dockerfile
- package.json
- .gitignore
```

## Paso 5: Crear y configurar `.env`

En el archivo `.env` configuraremos nuestras variables de entorno:

```env
DB_HOST = "mysql"
DB_USER = "root"
DB_PASSWORD = "password"
DB_DATABASE = "database"
JWT_SECRET = "secret"

```

Estas son las credenciales de tu base de datos MySQL y el secreto de tu jsonwebtoken.

## Paso 6: Configurar Sequelize
Sequelize es un ORM para Node.js, que se utilizará para gestionar la conexión de nuestra base de datos:
Primero necesitamos instanciar sequelize en el archivo de configuración. Asi se verá:

En `config/connection.js`
```javascript
import  Sequelize  from "sequelize";
/* import dotenv from "dotenv";

dotenv.config(); */

const connection = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASSWORD, {
host: process.env.DB_HOST,
port:3306,
dialect: "mysql",
define: {
    timestamps: false,
    freezeTableName: true,
  },
});

export default connection;
```

## Paso 7: Configurar Express 

Creamos el archivo `src/index.js` y configuramos express.
Debemos requerir las dependencias instaladas e iniciar un servidor.

Así se ve un ejemplo de configuración básica que permite leer el body de las peticiones,
iniciar la sesión de express y configurar el puerto del servidor:

```javascript
import express from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import expressSession from 'express-session';

dotenv.config();

const app = express();

app.use(cors()); // Para permitir peticiones desde cualquier origen

app.use(expressSession({ // Para iniciar la sesión de express
    secret: process.env.JWT_SECRET,
    resave: false,
    saveUninitialized: false,
    cookie: {
        maxAge: 1000 * 60 * 60  // 1 hora
    }
}));

app.use(express.json()); // Para leer los datos enviados por un cliente en formato JSON
app.use(express.urlencoded({extended: true})); // Para leer los datos enviados por un formulario. Extended true permite leer datos anidados en el body



const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

## Paso 8: Crear el modelo de datos

Vamos a crear el modelo en `src/models/user.js`

```javascript
import connection from "../config/connection.js";
import {DataTypes} from "sequelize";

const Usuario = connection.define(
    "usuario",
    {
        usuario_id: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            autoIncrement: true,
        },
        username:{
            type: DataTypes.STRING(45),
            allowNull: false,
            unique: true,
        },
        password:{
            type: DataTypes.STRING(100),
            allowNull: false,
        }
        
    }
);

export default Usuario;


```


## Paso 9: Crear los controladores

En `src/controllers/userApiController.js`

```javascript
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import Usuario from '../models/user.js';

const userApiController = {
    register: async (req, res) => {
        try {
            const {username, password} = req.body;
            const hash = bcrypt.hashSync(password, 10);
            const usuario = await Usuario.create({username, password: hash});
            res.json(usuario);
        } catch (error) {
            console.log(error);
            res.status(500).json({message: "Error en el servidor"});
        }
    },
    login: async (req, res) => {
        try {
            const {username, password} = req.body;
            const usuario = await Usuario.findOne({where: {username}});
            if(!usuario) return res.status(400).json({message: "Usuario o contraseña incorrectos"});
            const iguales = bcrypt.compareSync(password, usuario.password);
            if(!iguales) return res.status(400).json({message: "Usuario o contraseña incorrectos"});
            const token = jwt.sign({usuario}, process.env.JWT_SECRET, {expiresIn: 60 * 60});
            res.json({usuario, token});
        } catch (error) {
            console.log(error);
            res.status(500).json({message: "Error en el servidor"});
        }
    },
    profile: async (req, res) => {
        try {
          const id = req.usuario.id;
          const usuario = await Usuario.findByPk(id);
          res.json(usuario);
        } catch (error) {
          console.log(error);
          res.status(500).json({ message: "Error en el servidor" });
        }
    }
}

export default userApiController;
```

En `src/controllers/userViewController.js`. Usamos express-session para manejar la sesión del usuario.

```javascript
import bcrypt from 'bcrypt';

import Usuario from '../models/user.js';

const userViewController = {
    registerForm: (req, res) => {
        res.render('register');
    },
    loginForm: (req, res) => {
        res.render('login');
    },
    register: async (req, res) => {
        try {
            const {username, password} = req.body;
            const hash = bcrypt.hashSync(password, 10);
            const usuario = await Usuario.create({username, password: hash});
            res.redirect('/login');
        } catch (error) {
            console.log(error);
            res.status(500).json({message: "Error en el servidor"});
        }
    },
    login: async (req, res) => {
        try {
            const {username, password} = req.body;
            const usuario = await Usuario.findOne({where: {username}});
            if(!usuario) return res.status(400).json({message: "Usuario o contraseña incorrectos"});
            const iguales = bcrypt.compareSync(password, usuario.password);
            if(!iguales) return res.status(400).json({message: "Usuario o contraseña incorrectos"});
            req.session.usuario = usuario;
            res.redirect('/profile');
        } catch (error) {
            console.log(error);
            res.status(500).json({message: "Error en el servidor"});
        }
    },
    logout: (req, res) => {
        req.session.destroy();
        res.redirect('/login');
    },
    profile: (req, res) => {
      try {
        const id = req.session.usuario.usuario_id;
        const usuario = await Usuario.findByPk(id);
        res.render('profile', {usuario});
      } catch (error) {
        console.log(error);
        res.status(500).json({ message: "Error en el servidor" });
      }
        
    }
}

export default userViewController;
```

## Paso 10: Crear los middlewares para manejar la sesion tanto en la API como en las vistas

En `src/middlewares/session.js`

```javascript
const isLogged = (req, res, next) => {
    if(req.session.usuario) next();
    else res.redirect('/login');
}

export default isLogged;
```
En `src/middlewares/sessionApi.js` usando jwt

```javascript
import jwt from 'jsonwebtoken';

const sessionApi = (req, res, next) => {
    try {
        const token = req.headers.authorization.split(' ')[1];
        const usuario = jwt.verify(token, process.env.JWT_SECRET);
        req.usuario = usuario;
        next();
    } catch (error) {
        console.log(error);
        res.status(401).json({message: "No autorizado"});
    }
}

export default sessionApi;
```

## Paso 11: Crear las vistas con pug

En `src/views/layout.pug`

```pug
doctype html
html(lang="es")
    head
        meta(charset="UTF-8")
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        title= title
        link(rel="stylesheet", href="/css/style.css")
    body
        header
            nav
                ul
                    li
                        a(href="/") Home
                    li
                        a(href="/login") Profile
                    li
                        a(href="/register") Register
                    li
                        a(href="/logout") Logout
        main
            block content
        footer
            p &copy; 2023
```

En `src/views/home.pug`

```pug
extends layout

block content
    h1 Home
    p Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.
```

En `src/views/login.pug`

```pug
extends layout

block content
    h1 Login
    form(action="/login", method="POST")
        input(type="text", name="username", placeholder="Username")
        input(type="password", name="password", placeholder="Password")
        input(type="submit", value="Login")
```

En `src/views/register.pug`

```pug
extends layout

block content
    h1 Register
    form(action="/register", method="POST")
        input(type="text", name="username", placeholder="Username")
        input(type="password", name="password", placeholder="Password")
        input(type="submit", value="Register")
```

En `src/views/profile.pug`

```pug
extends layout

block content
    h1 Profile
    p #{usuario.username}
```

## Paso 12: Crear las rutas para las vistas

En `src/routes/userViewRoutes.js`

```javascript
import express from 'express';

import userViewController from '../controllers/userViewController.js';
import session from '../middlewares/session.js';

const router = express.Router();

router.get('/register', userViewController.registerForm);
router.get('/login', userViewController.loginForm);
router.post('/register', userViewController.register);
router.post('/login', userViewController.login);
router.get('/logout', session, userViewController.logout);
router.get('/profile', session, userViewController.profile);

export default router;
```

## Paso 13: Crear las rutas para la API

En `src/routes/userApiRoutes.js`

```javascript
import express from 'express';

import userApiController from '../controllers/userApiController.js';
import sessionApi from '../middlewares/sessionApi.js';

const router = express.Router();

router.post('/register', userApiController.register);
router.post('/login', userApiController.login);
router.get('/profile', sessionApi, userApiController.profile);

export default router;
```








## Paso 14: Crear el router principal

En `src/routes/index.js`

```javascript
import express from 'express';

import userViewRoutes from './userViewRoutes.js';
import userApiRoutes from './userApiRoutes.js';

const router = express.Router();

router.use('/', userViewRoutes);
router.use('/api', userApiRoutes);

export default router;
```

## Conclusion

Desarrollamos una aplicación de ejemplo simple con las librerías requeridas, hay muchas cosas más avanzadas que puedes hacer con estas librerías, especialmente en términos de organización y arquitectura de código, autenticación y mucho más. 

También hemos manejo los contenedores docker para facilitar la implementación. 

**Nota:** Esta es una explicación general y puede requerir la instalación de paquetes adicionales en función del entorno del sistema. Se recomienda la documentación oficial para los paquetes individuales para entender completamente cómo funcionan.