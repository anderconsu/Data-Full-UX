# Ejercicios con Firebase
## Ejercicio 1:

Crear un formulario que permita a los usuarios registrarse con su correo electrónico y una contraseña en Firebase. Al hacer clic en el botón de enviar, se debe crear un usuario en Firebase Authentication y guardar su información en Firestore.


```html
<!DOCTYPE html>
<html>
  <head>
    <title>Registro de usuario en Firebase</title>
  </head>
  <body>
    <h1>Registro de usuario en Firebase</h1>
    <form>
      <label for="email">Correo electrónico:</label>
      <input type="email" id="email" name="email"><br><br>
      <label for="password">Contraseña:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Registrarse">
    </form>

    <!-- Firebase App (the core Firebase SDK) is always required and must be listed first -->
    <script src="https://www.gstatic.com/firebasejs/8.6.1/firebase-app.js"></script>

    <!-- Add Firebase products that you want to use -->
    <script src="https://www.gstatic.com/firebasejs/8.6.1/firebase-auth.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.6.1/firebase-firestore.js"></script>

    <!-- Firebase configuration -->
    <script>
      var firebaseConfig = {
        apiKey: "API_KEY",
        authDomain: "PROJECT_ID.firebaseapp.com",
        projectId: "PROJECT_ID",
        storageBucket: "PROJECT_ID.appspot.com",
        messagingSenderId: "SENDER_ID",
        appId: "APP_ID"
      };

      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);

      // Get a reference to the Firebase Authentication service
      var auth = firebase.auth();

      // Get a reference to the Firestore service
      var db = firebase.firestore();

      // Add an event listener to the form submit button
      document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault();
        
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;

        // Create a user in Firebase Authentication
        auth.createUserWithEmailAndPassword(email, password)
          .then(function(userCredential) {
            var user = userCredential.user;

            // Save the user information in Firestore
            db.collection("users").doc(user.uid).set({
              email: email
            })
              .then(function() {
                alert("Usuario creado correctamente");
              })
              .catch(function(error) {
                console.error("Error adding document: ", error);
              });
          })
          .catch(function(error) {
            console.error("Error creating user: ", error);
          });
      });
    </script>
  </body>
</html>
```

## Ejercicio 2:

Crear un chat en tiempo real con Firebase Realtime Database y Cloud Functions. Al enviar un mensaje desde el formulario, se debe guardar en la base de datos y ser mostrado automáticamente en la lista de mensajes.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Chat en tiempo real con Firebase</title>
  </head>
  <body>
    <h1>Chat en tiempo real con Firebase</h1>
    <form>
      <label for="message">Mensaje:</label>
      <input type="text" id="message" name="message"><br><br>
      <input type="submit" value="Enviar">
    </form>

    <ul id="messages"></ul>

    <!-- Firebase App (the core Firebase SDK) is always required and must be listed first -->
    <script src="https://www.gstatic.com/firebasejs/8.6.1/firebase-app.js"></script>

    <!-- Add Firebase products that you want to use -->
    <script src="https://www.gstatic.com/firebasejs/8.6.1/firebase-database.js"></script>

    <!-- Firebase configuration -->
    <script>
      var firebaseConfig = {
        apiKey: "API_KEY",
        authDomain: "PROJECT_ID.firebaseapp.com",
        databaseURL: "https://PROJECT_ID.firebaseio.com",
        projectId: "PROJECT_ID",
        storageBucket: "PROJECT_ID.appspot.com",
        messagingSenderId: "SENDER_ID",
        appId: "APP_ID"
      };

      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);

      // Get a reference to the Firebase Realtime Database service
      var db = firebase.database();

      // Get a reference to the "messages" node in the database
      var messagesRef = db.ref("messages");

      // Add an event listener to the form submit button
      document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault();
        
        var message = document.getElementById("message").value;

        // Save the message in the database
        messagesRef.push({
          text: message
        })
          .then(function() {
            alert("Mensaje enviado correctamente");
          })
          .catch(function(error) {
            console.error("Error adding message: ", error);
          });
      });

      // Add an event listener to the "child_added" event in the database
      messagesRef.on("child_added", function(snapshot) {
        var message = snapshot.val();
        
        // Create a new list item with the message text
        var li = document.createElement("li");
        li.textContent = message.text;

        // Add the list item to the messages ul
        document.getElementById("messages").appendChild(li);
      });
    </script>
  </body>
</html>
```