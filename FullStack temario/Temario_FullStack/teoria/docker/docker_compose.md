# Docker Compose

Docker Compose es una herramienta que se utiliza para definir y ejecutar aplicaciones Docker con múltiples contenedores. Permite definir los servicios, las redes y los volúmenes que son necesarios para una aplicación y ejecutarlos en conjunto de manera sencilla. Al utilizar Docker Compose, se realiza la configuración de varias aplicaciones y se administra su ciclo de vida en un solo archivo docker-compose.yml.

Docker Compose permite definir los servicios de una aplicación con Docker, en un archivo YAML. En este archivo se describen todos los detalles necesarios para crear y ejecutar una aplicación en un entorno de varios contenedores. Además, Docker Compose permite escalar los servicios de manera transparente y también proporciona control sobre el estado de la aplicación en su conjunto.

### Sintaxis

La sintaxis de Docker Compose es sencilla y está basada en archivos YAML. En el archivo `docker-compose.yml` puedes incluir los siguientes campos:

1. version
2. services
3. networks
4. volumes

Ejemplo:

```
version: '3'

services:
  web:
    build: .
    ports:
      - "5000:5000"
  redis:
    image: "redis:alpine"
networks:
  webnet:
```

### Casos de uso

1. Desarrollo de aplicaciones.

Una de las principales ventajas de Docker Compose es que los desarrolladores pueden trabajar en contenedores que replican la configuración de producción sin necesidad de configurar cada uno de los servicios. Así, se asegura que el software funcionará de la misma forma en todos los ambientes.

Ejemplo:

El siguiente Docker Compose crea dos servicios, uno es una aplicación creada a partir de un archivo Dockerfile y otro es una base de datos creada utilizando una imagen de MongoDB. Además, se crea una red privada en la que se conectan ambos servicios:

```
version: '3.1'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      MONGO_URI: mongodb://mongo:27017/items-db
    depends_on:
      - mongo
  mongo:
    image: mongo:4.0
    networks:
      - items-net

networks:
  items-net:
```

2. Integración y pruebas.

Docker Compose es una herramienta muy útil para realizar pruebas de integración de aplicaciones. Se pueden crear redes dedicadas para pruebas que simulan el funcionamiento de toda la aplicación.

Ejemplo:

Aquí se muestra un archivo de Docker Compose que crea dos servicios comunicados mediante una red privada. Se utiliza Redis para almacenar la cola y NGINX para manejar el balanceo de carga.

```
version: '3'

services:
  frontend:
    build: ./frontend
    volumes:
      - ./frontend:/usr/src/app
    links:
      - backend
    ports:
      - "8080:80"

  backend:
    build: ./backend
    volumes:
      - ./backend:/usr/src/app
    links:
      - redis
    env_file: .env
    depends_on:
      - redis
    expose:
      - "3000"

  redis:
    image: "redis:alpine"

  nginx:
    image: "nginx:alpine"
    volumes:
      - "./nginx.conf:/etc/nginx/nginx.conf:ro"
    ports:
      - "80:80"
    links:
      - frontend

networks:
  default:
    external:
      name: frontend_network
```

En conclusión, Docker Compose facilita el trabajo con contenedores Docker y permite definir varios servicios a través de un archivo YAML. Es una herramienta útil para trabajar con aplicaciones complejas y que involucren varios contenedores.