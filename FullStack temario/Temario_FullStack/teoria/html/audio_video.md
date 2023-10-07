# Audio y video

HTML proporciona dos elementos para incrustar contenido multimedia en una página web: el elemento `audio` y el elemento `video`.

### Elemento audio

El elemento `audio` se utiliza para incrustar contenido de audio en una página web. Para usarlo se debe agregar la etiqueta de apertura `<audio>`, especificar la fuente del archivo de audio usando el atributo `src`, y agregar una descripción del contenido usando el atributo `controls`.

```html
<audio src="mi-audio.mp3" controls>
  Tu navegador no soporta la etiqueta de audio.
</audio>
```

En este ejemplo, el archivo de audio "mi-audio.mp3" se incrusta en la página y el usuario puede reproducirlo, pausarlo, ajustar el volumen y detenerlo utilizando los controles de audio nativos del navegador.

### Elemento video

El elemento `video` se utiliza para incrustar contenido de video en una página web. Para usarlo se debe agregar la etiqueta de apertura `<video>`, especificar la fuente del archivo de video usando el atributo `src`, y agregar una descripción del contenido usando el atributo `controls`.

```html
<video src="mi-video.mp4" controls>
  Tu navegador no soporta la etiqueta de video.
</video>
```

En este ejemplo, el archivo de video "mi-video.mp4" se incrusta en la página y el usuario puede reproducirlo, pausarlo, ajustar el volumen y detenerlo utilizando los controles de video nativos del navegador.

### Casos de uso

Los elementos `audio` y `video` son útiles cuando se desea proporcionar contenido multimedia en una página web. Son ideales para incrustar videos tutoriales, demostraciones de producto o clips de audio.

Los elementos también son particularmente útiles para ofrecer contenido multimedia "en el flujo" de la experiencia de la página web. Esto significa que el contenido multimedia se integra con el contenido textual de la página y no requiere que el usuario navegue a una página separada o abra un reproductor multimedia externo.

Otro caso de uso es la creación de una galería de medios. Esto puede hacerse simplemente agregando varios elementos `audio` o `video` juntos.

```html
<div>
  <video src="video-1.mp4" controls></video>
  <p>Descripción del video 1.</p>
</div>

<div>
  <video src="video-2.mp4" controls></video>
  <p>Descripción del video 2.</p>
</div>

<div>
  <audio src="audio-1.mp3" controls></audio>
  <p>Descripción del audio 1.</p>
</div>
```

En este ejemplo, se agregan dos videos y un archivo de audio a una página web con descripciones apropiadas debajo de cada elemento.