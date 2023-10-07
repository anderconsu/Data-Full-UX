# Manipulación de fechas en MySQL

En MySQL, la manipulación de fechas se lleva a cabo mediante una serie de funciones y operadores integrados en el sistema. Antes de empezar a trabajar con fechas, es importante asegurarse de que el tipo de dato utilizado en la tabla sea "date", "datetime" o "timestamp".

Las funciones más comunes son:

1. CURDATE(): devuelve la fecha actual del sistema en formato YYYY-MM-DD.

2. NOW(): devuelve la fecha actual con hora y minutos en formato YYYY-MM-DD HH:MI:SS.

3. DATE(): extrae la fecha de un campo datetime o timestamp.

4. DATE_ADD(): agrega una cantidad determinada de días, meses o años a una fecha.

5. DATE_SUB(): resta una cantidad determinada de días, meses o años a una fecha.

6. DATEDIFF(): devuelve la diferencia en días entre dos fechas.

7. DATE_FORMAT(): formatea la fecha según el formato deseado (por ejemplo, DD/MM/YYYY).

Veamos algunos ejemplos de código para manipular fechas en MySQL:

1. Obtener la edad de una persona a partir de su fecha de nacimiento

    SELECT YEAR(CURDATE()) - YEAR(fecha_nacimiento) AS edad FROM personas;

2. Listar los empleados que cumplieron años este mes

    SELECT * FROM empleados WHERE MONTH(fecha_nacimiento) = MONTH(CURDATE());

3. Calcular la fecha de vencimiento de una factura a partir de su fecha de emisión y plazo de pago

    SELECT DATE_ADD(fecha_emision, INTERVAL 30 DAY) AS fecha_vencimiento FROM facturas WHERE id_factura = 1;

4. Obtener el número de días que faltan para el fin de año

    SELECT DATEDIFF('2019-12-31', CURDATE()) AS dias_para_fin_de_ano;

5. Obtener la fecha del próximo miércoles

    SELECT DATE_ADD(CURDATE(), INTERVAL 1 WEEKDAY) AS proximo_miercoles;

En resumen, la manipulación de fechas en MySQL es una tarea relativamente sencilla una vez que se conocen las funciones y operaciones disponibles. Es importante familiarizarse con estas herramientas para poder trabajar con fechas de manera eficiente en la base de datos.