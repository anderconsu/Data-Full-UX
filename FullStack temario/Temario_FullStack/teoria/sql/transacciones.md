# TRANSACCIONES

En MySQL, una transacción es una secuencia de operaciones que se ejecutan como una sola unidad lógica e indivisible, en la que las operaciones tienen efecto como si se estuvieran ejecutando en el mismo instante de tiempo. En otras palabras, una transacción es una serie de operaciones que deben tratarse como si fueran una sola, de modo que el éxito de la misma implique que todas las operaciones se han completado correctamente, mientras que cualquier fallo en cualquiera de las operaciones debe suponer un rechazo de todas las operaciones. Las transacciones permiten asegurar que la base de datos siempre esté en un estado consistente, y proporcionan mecanismos para recuperarse de posibles errores.

Las transacciones se realizan mediante el uso de las sentencias `START TRANSACTION`, `COMMIT` y `ROLLBACK`. La sentencia `START TRANSACTION` indica que se va a comenzar una transacción, mientras que `COMMIT` indica que se debe confirmar la transacción (es decir, que todas las operaciones se han completado con éxito) y `ROLLBACK` indica que se debe deshacer la transacción (es decir, que alguna de las operaciones ha fallado y se debe revertir el estado de la base de datos a como estaba antes de comenzar la transacción).

```sql
START TRANSACTION;

INSERT INTO tabla1 (campo1, campo2) VALUES ('valor1', 'valor2');
UPDATE tabla2 SET campo3 = 'valor3' WHERE campo4 = 'valor4';

COMMIT;
```

En este ejemplo estamos iniciando una transacción, dentro de la cual se están realizando dos operaciones: la inserción de un registro en `tabla1` y la actualización de un registro en `tabla2`. Si ambas operaciones se completan con éxito, se ejecuta la sentencia `COMMIT`, que confirma la transacción. Si alguna de las operaciones falla, se ejecuta la sentencia `ROLLBACK`, que deshace la transacción.

En resumen, los casos de uso más comunes para las transacciones en MySQL son aquellos en los que se necesite hacer varias operaciones de base de datos juntas, asegurando que si alguna falla, no se apliquen las demás, manteniendo siempre la integridad de los datos. Por ejemplo, se pueden utilizar transacciones en operaciones bancarias, reservas de billetes, compras en línea y otras acciones críticas en las que se necesite garantizar la coherencia de los datos.