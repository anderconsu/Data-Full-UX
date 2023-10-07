# MySQL en Docker

Podemos  ejecutar los siguientes comandos en la terminal para descargar y ejecutar la imagen oficial de MySQL en Docker:

```
docker pull mysql
docker run -d -p 3306:3306 --name mi-servidor-mysql -e MYSQL_ROOT_PASSWORD=mi-contraseña mysql
```

Donde "mi-contraseña" es la contraseña que deseamos establecer para la cuenta de root. El primer comando descarga la imagen oficial de MySQL de Docker Hub, mientras que el segundo comando crea y ejecuta un contenedor a partir de esa imagen. El parámetro "-d" indica que el contenedor debe ejecutarse en segundo plano y el parámetro "-p" indica que el puerto 3306 del contenedor (que es el puerto que utiliza MySQL por defecto) debe mapearse al puerto 3306 de nuestra máquina host.

Si deseamos cambiar la contraseña de la cuenta de root que se crea por defecto, podemos utilizar el parámetro "-e MYSQL_ROOT_PASSWORD=mi-contraseña" para establecer una contraseña nueva, tal como se muestra en el ejemplo anterior.

Para crear un usuario que tenga acceso a la base de datos y no tenga que usar la cuenta de root, podemos conectar al contenedor de MySQL usando el comando:

```
docker exec -it mi-servidor-mysql mysql -uroot -p
```

Donde "mi-servidor-mysql" es el nombre que le dimos al contenedor al ejecutar el comando "docker run". Este comando nos permite conectarnos a la instancia de MySQL que se está ejecutando en el contenedor usando la cuenta de root.

Una vez conectados, podemos crear un nuevo usuario y otorgarle los permisos necesarios para acceder a la base de datos. Por ejemplo, para crear un usuario llamado "mi-usuario" con contraseña "mi-contraseña-usuario" y otorgarle acceso a todas las bases de datos, podemos ejecutar los siguientes comandos:

```
CREATE USER 'mi-usuario'@'%' IDENTIFIED BY 'mi-contraseña-usuario';
GRANT ALL PRIVILEGES ON *.* TO 'mi-usuario'@'%';
FLUSH PRIVILEGES;
```

Después de ejecutar estos comandos, el usuario "mi-usuario" debería tener acceso a todas las bases de datos de la instancia de MySQL que se está ejecutando en el contenedor. Es importante tener en cuenta que el parámetro "%" en la definición del usuario indica que puede conectarse desde cualquier dirección IP, por lo que deberíamos restringirlo a una dirección IP específica si deseamos limitar el acceso.