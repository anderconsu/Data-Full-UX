# Entidad Relación


El modelo entidad-relación es una herramienta de modelamiento de datos que permite representar de manera gráfica las entidades (objetos o conceptos) y las relaciones que existen entre ellos. Este modelo se basa en el concepto de entidad, que es un objeto concreto o abstracto que existe en el mundo real. También se consideran las relaciones, que representan la interacción entre las entidades.

Un modelo entidad-relación consiste en una serie de cuadros, cada uno de los cuales representa una entidad, y conectores que unen estos cuadros para representar las relaciones entre ellas. Cada cuadro representa una entidad y contiene información como su nombre, atributos y características. Los conectores representan diferentes relaciones, como uno a uno, uno a muchos y muchos a muchos.

Wikipedia: https://es.wikipedia.org/wiki/Modelo_entidad-relaci%C3%B3n.
![Diagrama E-R](https://upload.wikimedia.org/wikipedia/commons/7/72/ER_Diagram_MMORPG.png)

Existen tres tipos de entidades en el modelo entidad-relación:

1. Entidades concretas: son objetos físicos que pueden ser tocados o vistos en el mundo real, como por ejemplo una persona, un auto, una casa, un libro, entre otros.

2. Entidades abstractas: son objetos que no podemos tocar o ver, pero que existen en el mundo real, como por ejemplo un pedido, una venta, una factura, entre otros.

3. Entidades asociativas: son objetos que se utilizan para representar relaciones de muchos a muchos entre otras entidades. Por ejemplo, en una base de datos de una tienda, se podría tener una entidad asociativa llamada “compra”, la cual estaría relacionada con las entidades “cliente” y “producto”.

Por otro lado, las relaciones que representa este modelo pueden ser de varios tipos:

1. Relaciones uno a uno: ocurre cuando una entidad se relaciona directamente con otra entidad y no hay más entidades involucradas. 

2. Relaciones uno a muchos: ocurre cuando una entidad se relaciona con varias entidades de otro tipo, pero estas últimas solo tienen una relación con la entidad en cuestión.

3. Relaciones muchos a uno: ocurre cuando varias entidades se relacionan con otra entidad de otro tipo. 

4. Relaciones muchos a muchos: cuando varias entidades se relacionan con varias entidades de otro tipo.

Para representar gráficamente estas relaciones, se utilizan símbolos específicos, como por ejemplo una línea simple para las relaciones uno a uno, una línea doble para las relaciones uno a muchos y una línea con asterisco para las relaciones muchos a muchos.

A continuación, se presenta un ejemplo de modelo entidad-relación para una base de datos de una tienda de libros. Tenemos dos entidades, “libro” y “autor”, donde libro tiene una relación con autor (cade un libro tiene un unico autor y cada autor puede publicar varios libros). Podemos representar esto en el modelo conceptual de la siguiente manera:

```
+-----------------------+        +-------------+
|        libro          |        |    autor    |
+-----------------------+        +-------------+
|      ISBN (PK)        |        |     ID (PK) |
|        titulo         |        |    nombre   |
|      descripcion      |        |  apellido  |
|        precio         |        +-------------+
|       stock           |
|   autor_id (FK)       |
+-----------------------+
```

En este ejemplo, la entidad “libro” tiene una relación con “autor” mediante el atributo “autor_id”. La clave primaria de la entidad “libro” es el campo “ISBN”, mientras que la clave primaria de la entidad “autor” es “ID”. Además, el campo “autor_id” de la entidad “libro” es una clave foránea que hace referencia al campo “ID” de la entidad “autor”.


Un caso de uso común para el modelo entidad-relación es en el diseño de sistemas de gestión. En el siguiente ejemplo podemos ver un diagrama entidad-relación que representa un sistema de gestión de facturación de un hospital. https://www.smartdraw.com/entity-relationship-diagram/examples/hospital-billing-entity-relationship-diagram/. 


En resumen, el modelo entidad-relación es una herramienta muy importante para el diseño y la creación de bases de datos. Permite representar de manera clara las relaciones entre entidades y su uso es fundamental para entender cómo funciona una base de datos.