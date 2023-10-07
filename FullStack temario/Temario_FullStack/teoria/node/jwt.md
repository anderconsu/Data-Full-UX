# Autenticación

Algunos de los métodos de autenticación más populares en Node.js son:

- **Passport.js**: es una biblioteca de autenticación flexible y modular para Node.js que se integra con Express y otros frameworks web. Soporta diversos métodos de autenticación como local, Facebook, Google, Twitter, etc. Passport.js utiliza estrategias (strategies) que definen cómo se autentica al usuario.
```javascript
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

passport.use(new LocalStrategy(
  function(username, password, done) {
    User.findOne({ username: username }, function (err, user) {
      if (err) { return done(err); }
      if (!user) { return done(null, false); }
      if (!user.validPassword(password)) { return done(null, false); }
      return done(null, user);
    });
  }
));
```

- **jsonwebtoken**: es una biblioteca para generar y verificar JWT en JavaScript. Se puede utilizar para autenticar solicitudes del servidor y para la creación de tokens de autorización para aplicaciones cliente.
```javascript
const jwt = require('jsonwebtoken');
const secret = 'mysecretkey';

const token = jwt.sign({ username: 'exampleuser' }, secret, { expiresIn: '1h' });
console.log(token);

const decoded = jwt.verify(token, secret);
console.log(decoded);
``` 

- **OAuth2**: es un protocolo de autorización de terceros que se utiliza para permitir que las aplicaciones de terceros accedan a ciertos recursos en nombre del usuario. OAuth2 es ampliamente utilizado por empresas como Facebook, Google y Twitter para proporcionar acceso a sus APIs.
```javascript
const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth20').Strategy;

passport.use(new GoogleStrategy({
    clientID: '1234567890',
    clientSecret: 'abcdefghijklmnpqrstuvwxyz123456',
    callbackURL: '/auth/google/callback'
  },
  function(accessToken, refreshToken, profile, done) {
    User.findOrCreate({ googleId: profile.id }, function (err, user) {
      return done(err, user);
    });
  }
));
``` 

En general, la elección del método de autenticación dependerá de los requerimientos específicos de la aplicación, así como de la infraestructura existente.

---
## JWT

JSON Web Token (JWT) es un estándar de token de acceso que se utiliza para la autenticación y autorización. Un JWT está compuesto por tres partes: una cabecera (header), un payload y una firma (signature)

- **Header**: contiene metadatos sobre el JWT como el tipo de token y el algoritmo utilizado para firmar el token.
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

- **Payload**: contiene la información que se desea transmitir en el token, como el nombre de usuario, la fecha de expiración, etc. Los datos son codificados en formato JSON.
```json
{
  "username": "exampleuser",
  "exp": 1605008655
}
```

- **Firma**: se utiliza para verificar la autenticidad del token. Se utiliza un secreto (secret) compartido entre el servidor y el cliente para crear una firma única para el JWT.
```javascript
const signature = HMACSHA256(base64UrlEncode(header) + "." + base64UrlEncode(payload), secret);
```

Para autenticar a un usuario utilizando JSON Web Token (JWT) en un servidor Node.js se pueden seguir los siguientes pasos básicos, tanto en una API como en una aplicación web con plantillas Pug:

1. Verificar las credenciales del usuario: Primero se debe verificar que las credenciales proporcionadas por el usuario sean válidas, es decir, que el nombre de usuario y contraseña sean correctos. Este paso puede variar dependiendo del método de autenticación utilizado.

2. Crear un token JWT: Una vez que se han verificado las credenciales, se debe crear un token JWT que contenga la información relevante del usuario, como su identidad o roles. Esto se puede hacer utilizando la biblioteca `jsonwebtoken`. El token debe incluir un tiempo de expiración para mejorar la seguridad.

```javascript
const jwt = require('jsonwebtoken');
const secret = "secretKey";
const expiresIn = "1h";

const token = jwt.sign({ 
  username: "johnDoe",
  role: "admin"
}, secret, { expiresIn });
```

3. Enviar el token al cliente: El token JWT generado debe ser enviado al cliente, ya sea como una respuesta a una solicitud de API o en una cookie para aplicaciones web.

4. Verificar el token del cliente: En cada solicitud sucesiva, el token JWT recibido del cliente debería ser verificado para asegurarse de que el usuario está autorizado a acceder a lo que está solicitando. Esto se puede hacer utilizando middleware en Node.js.

```javascript
const verifyToken = (req, res, next) => {
  const token = req.headers.authorization;
  if (!token) return res.status(401).send("No token provided");

  try {
    const decoded = jwt.verify(token, 'secretKey');
    req.user = decoded;
    next();
  } catch (error) {
    res.status(400).send("Invalid token provided");
  }
}
```

En una API RESTful, este middleware debería ser utilizado para proteger las rutas que requieran autenticación. Por ejemplo:
```javascript
app.get('/api/private', verifyToken, (req, res) => {
  // ... código para manejar la solicitud
});
```

En una aplicación web con plantillas Pug, este middleware debería ser utilizado para proteger las páginas que requieran autenticación. Por ejemplo:
```javascript
app.get('/dashboard', verifyToken, (req, res) => {
  // ... código para manejar la solicitud
  res.render('dashboard', { user: req.user });
});
```

En este caso, el middleware `verifyToken` se ejecutará antes de que se renderice la plantilla `dashboard.pug`, y solo si el token JWT es válido, el objeto `user` estará disponible para ser utilizado en la plantilla.

Estos son solo los pasos básicos para implementar autenticación JWT en un servidor Node.js. Cabe resaltar que no es una solución de seguridad completa, pero es un punto de partida para mejorar la seguridad en aplicaciones web y APIs. Además, es importante considerar diferentes escenarios como la renovación del token, la revocación del token, la implementación de rate limiting, entre otros.

---

