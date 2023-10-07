# Dockerfiles

**¿Qué es un Dockerfile?**

Un Dockerfile es un archivo de texto que contiene los comandos y configuraciones necesarias para construir una imagen de Docker. En otras palabras, es una especie de receta que se utiliza para construir un contenedor de Docker. 

**Sintaxis básica de un Dockerfile**

Un archivo de Dockerfile consta principalmente de dos partes: la primera, donde se especifica la imagen base (una imagen de Docker preexistente desde la que se construirá la nueva imagen) y la segunda, donde se definen los comandos y configuraciones para la nueva imagen. La sintaxis básica para ello es la siguiente:

```
FROM <imagen_base>
RUN <comando_1>
RUN <comando_2>
...
```

**Ejemplo de Dockerfile:**

A continuación, se presenta un ejemplo básico de Dockerfile que se utiliza para construir un contenedor que ejecuta una aplicación Node.js:

```
# especificar la imagen base
FROM node:14

# establecer directorio de trabajo
WORKDIR /app

# copiar archivos necesarios
COPY package*.json ./

# instalar dependencias
RUN npm install

# copiar archivos fuente
COPY . .

# exponer puerto
EXPOSE 3000

# definir comando para iniciar la aplicación
CMD ["npm", "start"]
```

**Explicación:**

- `FROM node:14`: Especifica que la imagen base será la más reciente de la versión 14 de Node.js.

- `WORKDIR /app`: Establece el directorio de trabajo para el contenedor en `/app`.

- `COPY package*.json ./`: Copia el archivo package.json y el archivo package-lock.json en el directorio de trabajo del contenedor.

- `RUN npm install`: Ejecuta el comando `npm install` para instalar las dependencias de la aplicación.

- `COPY . .`: Copia todo el contenido del directorio actual de trabajo en el directorio de trabajo del contenedor.

- `EXPOSE 3000`: Especifica que el contenedor expondrá el puerto 3000.

- `CMD ["npm", "start"]`: Define el comando que se ejecutará cuando se inicie el contenedor. En este caso, se ejecutará `npm start` para iniciar la aplicación.

**Casos de uso de Dockerfile:**

- Construcción de contenedores de aplicaciones: Al contar con un archivo Dockerfile que contiene todas las especificaciones de construcción de un contenedor, se puede replicar fácilmente el entorno de la aplicación en cualquier sistema.

- Despliegue de aplicaciones: Al definir cuidadosamente el entorno de la aplicación en un archivo Dockerfile, se puede asegurar que la aplicación se ejecutará de manera consistente en diferentes sistemas.

- Pruebas de integración continua: Los Dockerfiles se pueden utilizar en las herramientas de CI / CD para construir y probar imágenes de Docker como parte de la fase de compilación.