# Git
Git es un sistema de control de versiones distribuido, diseñado para gestionar proyectos de software de cualquier tamaño. Se utiliza para controlar y gestionar cambios en el código fuente y en los archivos de un proyecto.

### Funcionamiento básico de git

El funcionamiento básico de git es el siguiente:

1. Crear un repositorio: Se crea una carpeta que servirá como repositorio, donde se alojarán todos los archivos y el historial de cambios del proyecto. Para crear un nuevo repositorio se utiliza el siguiente comando:

```
git init
```

2. Añadir archivos al repositorio: Se agregan los archivos al repositorio utilizando el comando add, que les permite ser rastreados por git:

```
git add archivo1 archivo2 ...
```

3. Confirmar cambios: Se confirman los cambios realizados en los archivos rastreados para que queden registrados en el repositorio:

```
git commit -m "Mensaje del commit"
```

4. Enviar cambios al repositorio remoto: Los cambios confirmados se envían al repositorio en línea (como GitHub) para que todos los colaboradores tengan acceso y puedan actualizar su versión del proyecto.

```
git push origin master
```

### Comandos útiles de git

- `git status`: Muestra el estado de los archivos que han sido modificados en tu directorio local.

- `git log`: Muestra el historial de commits del proyecto.

- `git branch`: Muestra las ramas del repositorio.

- `git checkout`: Cambia la rama en la que se está trabajando.

- `git merge`: Fusiona dos ramas del repositorio.

- `git clone`: Clona un repositorio remoto a una carpeta local.

### Ejemplo de caso de uso

Supongamos que dos desarrolladores están trabajando en un mismo proyecto. Para asegurarse de que ambos estén actualizados con los cambios del otro, utilizan Git de la siguiente manera:

1. Después de crear y clonar el repositorio, hacen los cambios correspondientes en sus respectivos archivos.

2. Agregan los archivos al repositorio utilizando `git add`.

3. Confirman los cambios realizados utilizando `git commit -m "Mensaje del commit"`.

4. Actualizan su repositorio local utilizando `git pull`.

5. Si hay conflictos, los resuelven y actualizan nuevamente el repositorio local.

6. Por último, envían los cambios al repositorio remoto utilizando `git push origin master`.

De esta manera, ambos desarrolladores tienen una versión actualizada del proyecto y se aseguran de que no se sobreescriban los cambios del otro.
Resolución de Conflictos en Git

## Resolución de Conflictos en Git
Cuando varias personas trabajan en el mismo proyecto, puede haber casos en los que se produzcan conflictos al fusionar cambios. Para resolver estos conflictos, Git ofrece varias herramientas y técnicas que nos permiten trabajar de forma colaborativa y mantenemr el flujo de trabajo constante. 

A continuación, describimos los pasos para resolver conflictos en Git:

### Paso 1: Identificar el conflicto

 El primer paso es identificar y comprender el conflicto. Un conflicto ocurre cuando dos o más usuarios han editado la misma parte de un archivo y han realizado cambios distintos que Git no puede fusionar automáticamente. El siguiente comando nos muestra una lista de archivos en conflicto:

```bash
$ git status
```

### Paso 2: Visualizar el conflicto

El siguiente paso es visualizar el conflicto. Esto nos permitirá entender lo que ha sucedido y tomar una decisión informada acerca de cuál versión debemos seleccionar. Podemos utilizar el siguiente comando para mostrar los cambios en el archivo que han causado el conflicto:

```bash
$ git diff
```

### Paso 3: Seleccionar la versión a mantener

Una vez comprendemos el conflicto, debemos seleccionar la versión que queremos mantener. Esto dependerá de la naturaleza del conflicto y de la decisión que tome el equipo de desarrollo. Supongamos que nuestro conflicto se encuentra en el archivo "archivo.txt". Tendremos que editar el archivo manualmente y seleccionar qué cambios queremos mantener. 

### Paso 4: Agregar los cambios realizados 

Una vez que hemos seleccionado la versión que queremos mantener, debemos agregar los cambios al commit. Podemos hacer esto con el siguiente comando:

```bash
$ git add archivo.txt
```

### Paso 5: Realizar el commit

Ahora, podemos hacer el commit de los cambios seleccionados:

```bash
$ git commit -m "Resolución de conflictos"
```

### Ejemplo de Resolución de Conflictos

Supongamos que tenemos un archivo llamado "archivo.txt" que contiene la siguiente información:

```
Este es un archivo de texto. 
Aquí se realizó un cambio por el usuario A. 
Aquí se hizo otro cambio por el usuario B.
```

Ahora, supongamos que tanto el usuario A como el usuario B han hecho cambios en el mismo archivo. Digamos que el usuario A cambió la línea 2 a "Este es un archivo de texto modificado por el usuario A". Por otro lado, el usuario B cambió la línea 3 a "Aquí se hizo otro cambio por el usuario B, y otro cambio más".

Cuando ambos intenten hacer un push a la rama principal, Git detectará un conflicto y les informará que deben resolverlo antes de poder hacer el push. En este caso, el conflicto está en la línea 2 y la línea 3 del archivo "archivo.txt".

Para resolver el conflicto, los usuarios deberán seguir los pasos mencionados previamente, es decir, identificar el conflicto, visualizar el archivo, seleccionar la versión a mantener, agregar los cambios seleccionados y hacer el commit.

Por ejemplo, el usuario A puede decidir mantener su cambio en la línea 2 y eliminar el cambio hecho por el usuario B en la línea 3. Por otro lado, el usuario B puede decidir mantener su cambio en la línea 3 y eliminar el cambio hecho por el usuario A en la línea 2.

Una vez que ambos hayan seleccionado la versión que quieren mantener, podrán agregar los cambios con el comando `git add` y realizar el commit con el comando `git commit`. Después de esto, podrán hacer el push a la rama principal sin ningún problema.

## Ramas en Git

Las ramas en Git son una forma de separar el código en diferentes versiones. Esto permite que los desarrolladores trabajen en diferentes partes del proyecto de forma independiente y que puedan fusionar sus cambios cuando sea necesario.

### Funcionamiento básico de las ramas

El funcionamiento básico de las ramas en Git es el siguiente:

1. Crear una rama: Se crea una rama nueva utilizando el comando `git branch nombre_rama`.

2. Cambiar de rama: Se cambia de rama utilizando el comando `git checkout nombre_rama`.

3. Fusionar ramas: Se fusionan dos ramas utilizando el comando `git merge nombre_rama`.

4. Eliminar una rama: Se elimina una rama utilizando el comando `git branch -d nombre_rama`.

### Ejemplo de caso de uso

Supongamos que tenemos un proyecto en el que trabajan dos desarrolladores. Para asegurarse de que ambos estén actualizados con los cambios del otro, utilizan Git de la siguiente manera:

1. Después de crear y clonar el repositorio, van a la rama principal utilizando `git checkout rama_principal`. ("main","master","develop",...)

2. crean una rama nueva utilizando `git branch nombre_rama`.

3. Cambian a la rama nueva utilizando `git checkout nombre_rama`.

4. Hacen los cambios correspondientes en sus respectivos archivos.

5. Agregan los archivos al repositorio utilizando `git add`.

6. Confirman los cambios realizados utilizando `git commit -m "Mensaje del commit"`.

7. Fusionan los cambios de la rama principal a la rama nueva utilizando `git merge rama_principal`.

8. Cambian a la rama principal utilizando `git checkout rama_principal`.

9. Actualizan la rama principal utilizando `git pull`.

10. Fusionan los cambios de la rama nueva a la rama principal utilizando `git merge nombre_rama`.

11. Eliminan la rama nueva utilizando `git branch -d nombre_rama`.

12. Por último, envían los cambios al repositorio remoto utilizando `git push origin rama_principal`.

De esta manera, ambos desarrolladores tienen una versión actualizada del proyecto y se aseguran de que no se sobreescriban los cambios del otro.

## Recursos

- [Git](https://git-scm.com/)
- [Git - Documentación](https://git-scm.com/doc)
- [Git - Documentación - Español](https://git-scm.com/book/es/v2)
- [Git - Cheat Sheet Español](https://training.github.com/downloads/es_ES/github-git-cheat-sheet/)


