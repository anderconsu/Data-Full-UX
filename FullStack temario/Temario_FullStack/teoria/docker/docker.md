
# Docker

Docker es una herramienta de virtualización a nivel de sistema operativo que permite crear y administrar contenedores de software. Los contenedores son entornos aislados que incluyen todas las dependencias necesarias para que una aplicación pueda ejecutarse de manera consistente en cualquier entorno, independientemente de la infraestructura subyacente.

A diferencia de las máquinas virtuales, que requieren un hipervisor para ejecutar un sistema operativo completo para cada aplicación, Docker utiliza recursos del sistema host y el kernel subyacente para crear entornos de aplicación aislados y autocontenido (con su propia memoria, procesos y espacio de almacenamiento). Esto hace que Docker sea mucho más eficiente a la hora de utilizar recursos y mucho más rápido para iniciar y detener los contenedores. Además, los contenedores Docker son portables y pueden ser fácilmente movidos de una computadora a otra, en diferentes sistemas operativos o nubes.

Entre las principales ventajas de usar Docker, destacan:

- **Facilidad de gestión**: Docker permite crear y administrar contenedores de manera sencilla e intuitiva, con herramientas que facilitan la creación, despliegue y escalamiento de aplicaciones.
- **Eficiencia de recursos**: Al compartir el kernel del sistema host, los contenedores Docker son mucho más eficientes en términos de utilización de recursos que las máquinas virtuales.
- **Portabilidad**: Los contenedores Docker pueden ser fácilmente movidos entre diferentes entornos, en cualquier sistema operativo o nube, lo que hace que sean una herramienta muy útil para despliegues en diferentes entornos.
- **Flexibilidad**: Docker permite crear diferentes entornos de aplicaciones, cada uno con su propia configuración y dependencias, lo que simplifica el proceso de despliegue de aplicaciones y permite un mayor grado de flexibilidad.

Si quieres profundizar en el uso de Docker, puedes consultar los siguientes recursos:

- [Documentación oficial de Docker](https://docs.docker.com/)
- [Introducción a Docker](https://www.docker.com/what-docker)
- [Curso básico de Docker](https://www.udemy.com/course/docker-fundamentals/)
- [Video tutorial de Docker](https://www.youtube.com/watch?v=YFl2mCHdv24)
- [Guía de Docker en castellano](https://www.freecodecamp.org/espanol/news/guia-de-docker-para-principiantes-como-crear-tu-primera-aplicacion-docker/)

Un ejemplo de código y caso de uso sería el siguiente:

Supongamos que queremos crear una aplicación web utilizando Node.js. Podemos utilizar Docker para crear un entorno aislado con todas las dependencias necesarias para ejecutar nuestra aplicación. Para ello, podemos crear un archivo llamado "Dockerfile" que defina la configuración necesaria:

```
FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

En este archivo, se indica que se utilizará una imagen base de Node.js 14, se define el directorio de trabajo y se copian los archivos necesarios para instalar las dependencias de nuestra aplicación. Luego, se expondrá el puerto 3000 y se ejecutará el comando "npm start" para iniciar la aplicación cuando se ejecute el contenedor.

Para crear el contenedor, podemos utilizar el siguiente comando:

```
docker build -t mi-aplicacion .
```

Este comando creará una imagen de Docker a partir del archivo Dockerfile que definimos antes. Luego, podemos ejecutar la aplicación en un contenedor de Docker utilizando el siguiente comando:

```
docker run -p 3000:3000 mi-aplicacion
```

Este comando iniciará el contenedor y expondrá el puerto 3000 en nuestra máquina host, permitiendo acceder a la aplicación desde el navegador.

Todo esto se puede realizar sin necesidad de instalar Node.js en nuestra computadora, ya que Docker es capaz de crear un entorno aislado con todas las dependencias necesarias. Además, este contenedor se puede ejecutar en cualquier sistema operativo o en la nube, lo que hace que sea muy fácil de desplegar y compartir en diferentes entornos.