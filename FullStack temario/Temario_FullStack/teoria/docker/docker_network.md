# Docker Network

**¿Qué son las redes en Docker?**

Las redes de Docker son una forma de proporcionar conectividad entre distintos servicios que se ejecutan en contenedores distintos. Podemos considerar a las redes de docker como un switch virtual para los contenedores, que permite a los distintos contenedores comunicarse entre ellos y con el host al que están conectados.

Algunos ejemplos de redes de Docker son:

- Bridge: Se trata de la red predeterminada que usa Docker si no especificamos ninguna otra.

- Host: Si utilizamos la red de tipo host, el contenedor se conectará directamente a la red externa del sistema, pasando a formar parte de ella.

- Overlay: Red que permite a los nodos de Docker que se ejecutan en diferentes hosts comunicarse entre ellos. Esta funcionalidad se usa principalmente en despliegues de Docker Swarm.

**Creación de una red en Docker:**

Para crear una nueva red de Docker usamos el siguiente comando:

```
docker network create <nombre-de-la-red>
```

**Ejemplos de Comandos:**

A continuación, se presentan algunos ejemplos de comandos que podemos utilizar para trabajar con Docker y las redes creadas:

1. Listar las redes disponibles:
```
docker network ls
```

2. Ver detalles de una red en concreto:
```
docker network inspect <nombre-de-la-red>
```

3. Establecer una red por defecto para ejecutar nuevos contenedores:
```
docker network connect <nombre-de-la-red> <nombre-del-contenedor>
```

4. Asignar una IP a un contenedor:
```
docker run --name <nombre-del-contenedor> --network=<nombre-de-la-red> --ip <ip-deseada> -itd <nombre-de-la-imagen>
```

Por último, para eliminar una red previamente creada podemos usar el comando `docker network rm <nombre-de-la-red>`.

**Caso de uso:**

Un ejemplo de caso de uso práctico para las redes de Docker podría ser la construcción de una aplicación formada por varios servicios, cada uno de los cuales se ejecuta dentro de un contenedor. Al configurar correctamente las redes, cada servicio puede interactuar con los demás contenedores, lo que nos permite construir aplicaciones más complejas.

Por ejemplo, podemos crear una red llamada `app_net` y hacer que todos los contenedores de servicio se unan a ella:

```
$ docker network create app_net

$ docker run -itd --name redis --network app_net redis

$ docker run -itd --name db --network app_net mongo

$ docker run -itd --name app --network app_net myapp
```

De esta forma, cada contenedor puede comunicarse con los otros en la misma red, lo que nos permite transmitir datos de una forma mucho más eficiente.