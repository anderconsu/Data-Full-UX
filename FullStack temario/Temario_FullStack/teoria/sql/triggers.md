# Triggers

Los triggers son objetos de bases de datos que se utilizan para ejecutar acciones automáticas en respuesta a ciertos eventos que se producen en una tabla en particular. En MySQL, los triggers se ejecutan antes o después de que se realice una de las siguientes acciones: INSERT, UPDATE o DELETE.

Un trigger está compuesto principalmente por dos elementos: (1) el evento que activa el trigger, o sea, la acción en la tabla que dispara el trigger, y (2) el procedimiento que se ejecuta como respuesta al evento.

A continuación, un ejemplo de cómo crear un trigger para que se activen ciertas acciones automáticas en una tabla:

```mysql
CREATE TRIGGER trig_nombre_trigger 
AFTER INSERT ON nombre_tabla
FOR EACH ROW 
BEGIN
 // acciones a realizar
END;
```

* `trig_nombre_trigger`: nombre del trigger que se va a crear.
* `AFTER INSERT ON nombre_tabla`: indica que el trigger se ejecutará después de que se realice una operación de inserción en la tabla `nombre_tabla`. 
* `FOR EACH ROW`: significa que el trigger se ejecutará una vez para cada registro afectado por la operación de inserción.
* `BEGIN...END`: el código que se desea ejecutar cuando se active el trigger.

En cuanto a los casos de uso más comunes, se pueden mencionar los siguientes:

1. Verificación de datos: un trigger puede ser utilizado para llevar a cabo una comprobación de los datos que se están insertando en una tabla, para garantizar que cumplan con ciertas reglas o restricciones.

```mysql
CREATE TRIGGER verificar_datos 
BEFORE INSERT ON nombre_tabla
FOR EACH ROW
BEGIN
    IF NEW.nombre IS NULL THEN
        SET NEW.nombre = 'Nombre desconocido';
    END IF;
END;
```

* Este trigger verifica si el dato del nombre está vacío. En caso de que sea así, reemplaza ese valor por 'Nombre desconocido'.

2. Auditoría: se puede utilizar un trigger para registrar información sobre alteraciones realizadas en una tabla en un log de auditoría.

```mysql
CREATE TRIGGER auditar_cambios 
AFTER INSERT ON nombre_tabla
FOR EACH ROW
BEGIN
    INSERT INTO log (usuario, fecha, tabla, accion)
    VALUES (USER(), NOW(), 'nombre_tabla', 'INSERT');
END;
```

* El trigger registra el nombre de usuario, fecha y hora de la acción, el nombre de la tabla afectada y la acción realizada.

3. Sincronización de datos: los triggers también se pueden utilizar para sincronizar los datos en diferentes tablas.

```mysql
CREATE TRIGGER sincronizar_datos 
AFTER INSERT ON tabla_origen 
FOR EACH ROW
BEGIN
    INSERT INTO tabla_destino (campo1, campo2, campo3)
    VALUES (NEW.valor1, NEW.valor2, NEW.valor3);
END;
```

* Este trigger inserta los mismos valores que se acaban de insertar en `tabla_origen` en la `tabla_destino`.

En resumen, los triggers son una herramienta muy útil para automatizar tareas y garantizar que los datos en la base de datos cumplan con ciertas reglas o restricciones. También se pueden utilizar para llevar a cabo la auditoría de las acciones realizadas.