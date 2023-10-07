# PassportJS

Passport es un middleware de autenticación para Node.js. Se utiliza para implementar una variedad de esquemas de autenticación, como autenticación local (nombre de usuario/contraseña), autenticación social (Google, Facebook, Twitter, etc.), autenticación de token (JWT, OAuth, etc.) y muchas más. 

Passport simplifica el proceso de autenticación en Node.js al proporcionar una estructura flexible y modular. También permite crear APIs RESTful seguras al integrar con diferentes plataformas de autenticación.

Para usar PassportJS, es necesario instalarlo a través del comando `npm install passport`, y luego configurar su estrategia de autenticación según se requiera en el proyecto.

---

En Passport, una estrategia se refiere a la forma en que se autentican los usuarios en una aplicación. Passport tiene una amplia variedad de estrategias, desde autenticación local con nombre de usuario y contraseña hasta autenticación de terceros usando Google, Facebook, Twitter, y más.

Una estrategia de Passport es un objeto que define cómo Passport autenticará las solicitudes. Para cada tipo de autenticación que se quiera implementar en una aplicación, se debe crear una estrategia. Cada estrategia de autenticación suele tener su propia estrategia de Passport.

Aquí hay un ejemplo de una estrategia local usando express-session:

```
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const session = require('express-session');

// Configuración de la sesión
app.use(session({
  secret: 'mysecret', // Clave secreta para generar cookies
  resave: false,
  saveUninitialized: false,
}));

// Configuración de Passport
app.use(passport.initialize());
app.use(passport.session());

// Configuración de la estrategia local
passport.use(new LocalStrategy(
  (username, password, done) => {
    User.findOne({ username: username }, (err, user) => {
      if (err) { return done(err); }
      if (!user) {
        return done(null, false, { message: 'Usuario no encontrado' });
      }
      if (!user.isValidPassword(password)) {
        return done(null, false, { message: 'Contraseña incorrecta' });
      }
      return done(null, user);
    });
  }
));

// Serialización y deserialización de usuarios
passport.serializeUser((user, done) => {
  done(null, user.id);
});

passport.deserializeUser((id, done) => {
  User.findById(id, (err, user) => {
    done(err, user);
  });
});

// Ruta de inicio de sesión
app.post('/login', passport.authenticate('local', {
  successRedirect: '/dashboard',
  failureRedirect: '/login',
}));
```

En este ejemplo, se utiliza la estrategia local de Passport para autenticar a los usuarios utilizando un nombre de usuario y una contraseña. Se define la estrategia usando `passport.use()`, que toma una instancia de `LocalStrategy` como argumento.

En `passport.serializeUser()` y `passport.deserializeUser()`, se define cómo se manejarán los objetos de usuario para las solicitudes entrantes y salientes. En el caso de este ejemplo, la información del usuario se guardará en la sesión para futuras solicitudes.

Finalmente, se utiliza `passport.authenticate()` en la ruta `/login` para validar los datos del usuario. Si los datos son correctos, el usuario será redirigido a su dashboard. De lo contrario, volverá a la página de inicio de sesión.

---

Aquí un ejemplo de cómo usar la estrategia de autenticación de Google en una API RESTful en Express y Passport:

```
const passport = require("passport");
const GoogleStrategy = require("passport-google-oauth20").Strategy;

// Configuraciones para la estrategia de Google
const GOOGLE_CLIENT_ID = "tu-client-id-de-google";
const GOOGLE_CLIENT_SECRET = "tu-client-secret-de-google";
const CALLBACK_URL = "http://localhost:3000/auth/google/callback" // URL de redireccionamiento despues de la autenticación de Google

// Configuración de la estrategia de Google en Passport
passport.use(new GoogleStrategy({
    clientID: GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET,
    callbackURL: CALLBACK_URL
  },
  // Callback de autenticación
  (accessToken, refreshToken, profile, done) => {
    // El perfil contiene el usuario autenticado de Google
    // Aquí se realiza la búsqueda del usuario en la aplicación
    // Si el usuario no existe, se crea uno
    User.findOrCreate({ googleId: profile.id }, (err, user) => {
      return done(err, user);
    });
  }
));

// Ruta de autenticación de Google
app.get('/auth/google', passport.authenticate('google', { scope: ['profile'] }));

// Ruta de callback de autenticación de Google
app.get('/auth/google/callback', passport.authenticate('google', { failureRedirect: '/login' }), (req, res) => {
  // Si la autenticación es correcta, se redirige a la página principal de la aplicación
  res.redirect('/');
});
```

En esta configuración, la estrategia de autenticación de Google se utiliza para realizar una autenticación de Google en una API RESTful con Node.js, Express y Passport. La API utiliza el módulo "passport-google-oauth20" de Node.js para proporcionar la estrategia de autenticación de Google. Para utilizar la estrategia de autenticación de Google, es necesario definir el ID del cliente, el secreto del cliente, la URL de redirección de autenticación y el callback de autenticación. A continuación, se define la función de autenticación que se ejecutará después de la autenticación de Google en la que se busca al usuario en la aplicación y se realiza la creación del usuario si no existe. Finalmente, se definen las rutas de autenticación de Google y las rutas de callback de autenticación de Google.

---

## Referencias

[PassportJS](http://www.passportjs.org/)
[Tutorial Google](https://www.passportjs.org/tutorials/google/)