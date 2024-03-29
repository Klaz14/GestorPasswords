Gestor de Contraseñas

V 0.2.1

* Empezado a respetarse los principios SOLID.
* Separada la clase GestorContraseñas en GestorCifrado, GestorPerfiles, GestorTarjetas y MenuGestor.
* Revisados y reemplazados los metodos correspondientes para el funcionamiento correcto de la aplicacion.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.2

* Comenzada la conversion del codigo basado en funciones a OOP.
* Revisados los metodos, todo funciona como en el codigo original.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.9.9

* Reemplazadas palabras de prueba y eliminados comentarios del codigo.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.9.8 (correcciones varias y ultimas implementaciones antes de crear la interfaz)

* Añadido paso de confirmacion antes de realizar una modificacion, creacion o eliminacion de un dato o bloque de datos.
* Eliminada funcion de modificar todos los datos de un bloque de datos al mismo tiempo.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.9.5 (correcciones varias y ultimas implementaciones antes de crear la interfaz grafica)

* Agregada funcionalidad para modificar y eliminar anotaciones en particular.
* Corregido error que hacia que al modificar una anotacion se modificara el token en su lugar.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.9 (correcciones varias y ultimas implementaciones antes de crear la interfaz grafica)

* Agregada funcionalidad para eliminar bloques de datos.
* Eliminada opcion de multiples perfiles, en pos de mayor seguridad.
* Modificadas funciones varias y eliminadas funciones obsoletas.
* Agregado dato "Token" a los datos de los bloques de datos.
* Agregada funcionalidad para poder escribir mas de una anotacion por bloque de dato.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.8

* Implementado un encriptador de archivos, tanto para el .txt de perfiles como para el .txt que guarda los bloques de datos.
* Con la implementacion del encriptador se necesita salir de la aplicacion siempre primero con la opcion de salir del menu, dado que sino no se encriptan los perfiles y hay problemas al reingresar, esto se solucionara al crear la interfaz grafica.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.7.8

* Reimplementada la funcion de checkeo de contraseña actual al querer modificar la contraseña del perfil, del dato contraseña o de todos los datos de un bloque de datos.
* Añadida interfaz para agregar los datos al .txt que guarda los datos.
* Eliminado selector de perfil al momento de ingresar a los datos guardados del perfil actual.
* Corregida la funcion para que sea mas amigable el modificar los datos, pudiendo elegir que dato modificar en particular o si modificar todos juntos.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.7.5

* Eliminada fecha de nacimiento como dato.
* Modificadas funciones para generar .txt para guardar perfiles y otro .txt para guardar los datos de cada perfil por separado.
* Añadida funcion para gestionar los datos del .txt que guarda los datos, falta interfaz en consola.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.7.1

* Solucionado un bug que borraba los datos del .txt al momento de querer modificar los mismos desde el submenu modificar el perfil.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.7

* Añadida funcion para cambiar entre perfiles.
* Movida la opcion de crear perfiles desde el menu principal hacia el submenu de cambiar entre perfiles.
* Ahora, si solo se detecta un perfil guardado, ingresara automaticamente a ese perfil, lo mismo si es la primera vez que se crea un perfil (antes se requeria que ingresara dos veces el nombre del perfil aunque hubiera solamente uno, el recien creado).
* La verificacion del perfil solo se hace la primera vez que se entra a la aplicacion.
* Eliminado el uso de un archivo .txt que guardaba el ultimo usuario registrado.
* Agregadas funciones para regresar al menu desde los submenus de cambiar de perfil y de modificar el perfil.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.6

* Añadida funcion que detecta si existe o no archivo de guardado de perfiles y en caso de no existir crea uno.
* Añadida funcion que permite crear un nuevo perfil en caso de no existir el nombre del perfil en el archivo de guardado.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.5

* Añadido saludo de despedida al cerrar la aplicacion.
* Añadida verificacion de contraseña anterior al momento de cambiar la contraseña.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.4

* Añadida una funcion que permite recordar el ultimo usuario que utilizo la aplicacion antes de su cierre.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.3

* Añadidas lineas divisorias entre usos de la aplicacion (eliminables cuando se tenga interfaz grafica).
* En las opciones de modificacion se permite modificar cada dato por separado en lugar de todos juntos.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.2

* Añadidas opciones de modificacion de datos y de cierre de aplicacion.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1.1

* Se modifico la forma de entrada de datos para poder almacenar mas de un tipo de dato.
* Se permite la consulta de los datos a traves de perfiles, que toman como referencia para mostrar los datos el nombre del primer dato introducido.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

V 0.1

* Interfaz basica creada, se manipula la aplicacion mediante la consola.
* Se permite introducir un dato que sera almacenado en un archivo .txt.
* Se permite la consulta de dicho dato.