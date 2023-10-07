# WebScraping
El webscraping es una técnica de programación utilizada para obtener datos de un sitio web de forma automatizada. En lugar de acceder manualmente a un sitio web y copiar y pegar información, el webscraping utiliza robots automatizados para obtener información de una página web y agruparla en un conjunto de datos estructurado.

El proceso de webscraping comienza enviando una solicitud HTTP a una página web. Después de recibir una respuesta, el desarrollador puede usar varias herramientas, como la biblioteca BeautifulSoup en Python o Cheerio en Node.js, para extraer los datos necesarios del HTML.

Los datos extraídos pueden ser de diferentes formas, como texto, imágenes, videos o archivos PDF. En algunos casos, los datos incluyen la información necesaria que se encuentra detrás de los formularios de contacto, las consultas de búsqueda y otros elementos de interacción con el usuario.

El webscraping se utiliza en muchos ámbitos, como el marketing digital, la investigación de mercado, la recopilación de datos y la automatización de la adquisición de datos. Para evitar problemas legales, es importante que los desarrolladores verifiquen que tienen permiso para raspar los datos en cada sitio web antes de utilizar el webscraping.

En general, el webscraping es una herramienta poderosa y útil para la recopilación de datos automatizada y puede ahorrar una gran cantidad de tiempo y esfuerzo en la recopilación manual de datos.


```javascript
import puppeteer from 'puppeteer';
import jsdom from 'jsdom';

const url = 'http://ejemplo.com';
const mailSelector = 'body > div:nth-child(2) > h2 > a';

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url);

  const contentHTML = await page.content();
  const JSDOM= jsdom.JSDOM;
  const dom = new JSDOM(contentHTML);
  const mailNode = dom.window.document.querySelector(mailSelector);
  
  console.log(mailNode.innerHTML);

  await browser.close();
})();
```

Este ejemplo muestra cómo utilizar Puppeteer para navegar y obtener el contenido HTML de una página, y luego utilizar JSDom para manipular y obtener información específica del HTML. En este caso, el ejemplo busca dentro del HTML un selector específico que se refiere a un correo electrónico y lo muestra por consola.

Es importante destacar que se debe tener en cuenta la política de webscraping del sitio que se desea obtener información, para evitar posibles problemas legales o bloqueos.

## Referencias

[puppeteer](https://pptr.dev/)

[jsdom](https://www.npmjs.com/package/jsdom)