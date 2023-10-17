import os

def cargar_perfiles():
    if os.path.exists('perfiles.txt'):
        return
    else:
        print("No se encontró ningún archivo de perfiles.")
        nombre = input("Por favor, introduce tu nombre: ")
        fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
        contraseña = input("Crea una contraseña: ")

        with open('perfiles.txt', 'a') as archivo:
            archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
        print(f"Perfil de {nombre} guardado correctamente.")
        print('-'*30)  # Línea divisoria

def guardar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    contraseña = input("Crea una contraseña: ")

    with open('perfiles.txt', 'a') as archivo:
        archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
    print(f"Perfil de {nombre} guardado correctamente.")
    print('-'*30)  # Línea divisoria
    

def recuperar_perfil(ultimo_perfil):
    nombre = ultimo_perfil
    with open('perfiles.txt', 'r') as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if datos[0] == nombre:
                print(f"Nombre: {datos[0]}")
                print(f"Fecha de Nacimiento: {datos[1]}")
                print(f"Contraseña: {datos[2]}")
                return
        print(f"No se encontró un perfil para {nombre}.")
    print('-'*30)  # Línea divisoria

def modificar_perfil(ultimo_perfil):
    while True:
        nombre = ultimo_perfil
        with open('perfiles.txt', 'r') as archivo:
            lineas = archivo.readlines()

        encontrado = False
        with open('perfiles.txt', 'w') as archivo:
            for linea in lineas:
                datos = linea.strip().split(',')
                if datos[0] == nombre:
                    print(f"1. Modificar Fecha de Nacimiento")
                    print(f"2. Modificar Contraseña")
                    print(f"3. Volver al menú principal")
                    opcion = input("Por favor, elige una opción (1, 2 o 3): ")

                    if opcion == '1':
                        fecha_nacimiento = input("Introduce tu nueva fecha de nacimiento (dd/mm/aaaa): ")
                        contraseña = datos[2]
                    elif opcion == '2':
                        contraseña_anterior = input("Introduce tu contraseña anterior: ")
                        if contraseña_anterior == datos[2]:
                            contraseña = input("Introduce tu nueva contraseña: ")
                        else:
                            print("¡Contraseña incorrecta! No se realizaron cambios.")
                            archivo.write(linea)
                            continue
                        fecha_nacimiento = datos[1]
                    elif opcion == '3':
                        return

                    archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
                    print(f"Perfil de {nombre} modificado correctamente.")
                    encontrado = True
                else:
                    archivo.write(linea)

        if not encontrado:
            print(f"No se encontró un perfil para {nombre}.")
        print('-'*30)  # Línea divisoria


def seleccionar_perfil():
    # Verificamos si hay perfiles guardados
    with open('perfiles.txt', 'r') as archivo:
        perfiles = [linea.strip().split(',')[0] for linea in archivo]
    
    if len(perfiles) == 1:
        return perfiles[0]

    nombre = input("Por favor, introduce tu nombre: ")

    if nombre in perfiles:
        print(f"Bienvenido, {nombre}!")
        return nombre
    else:
        print(f"No se encontró un perfil para {nombre}. ¿Deseas crear uno nuevo?")
        crear_nuevo = input("Ingresa 's' para crear un nuevo perfil, o cualquier otra tecla para salir: ")
        if crear_nuevo.lower() == 's':
            fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
            contraseña = input("Crea una contraseña: ")

            with open('perfiles.txt', 'a') as archivo:
                archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
            print(f"Perfil de {nombre} guardado correctamente.")
            print('-'*30)  # Línea divisoria

        return nombre


def cambiar_perfil():
    while True:
        print("Perfiles disponibles:")
        with open('perfiles.txt', 'r') as archivo:
            perfiles = [linea.strip().split(',')[0] for linea in archivo]
            for i, perfil in enumerate(perfiles, start=1):
                print(f"{i}. {perfil}")
            print(f"{len(perfiles)+1}. Agregar nuevo perfil")
            print(f"{len(perfiles)+2}. Volver al menú principal")

        opcion = input("Por favor, elige una opción: ")

        if opcion.isnumeric():
            opcion = int(opcion)
            if 1 <= opcion <= len(perfiles):
                return perfiles[opcion-1]
            elif opcion == len(perfiles) + 1:
                nombre = input("Por favor, introduce tu nombre: ")
                fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
                contraseña = input("Crea una contraseña: ")

                with open('perfiles.txt', 'a') as archivo:
                    archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
                print(f"Perfil de {nombre} guardado correctamente.")
                print('-'*30)  # Línea divisoria
                return nombre
            elif opcion == len(perfiles) + 2:
                return None

        print("Opción inválida. Volviendo al menú principal.")


def cerrar_aplicacion(perfil):
    print(f"¡Hasta luego, {perfil}! ¡Espero verte pronto!")
    exit()

def guardar_ultimo_perfil(perfil):
    with open('ultimo_perfil.txt', 'w') as archivo:
        archivo.write(perfil)

def obtener_ultimo_perfil():
    if os.path.exists('ultimo_perfil.txt'):
        with open('ultimo_perfil.txt', 'r') as archivo:
            return archivo.read().strip()
    return None

def menu_principal(perfil):
    print('-'*30)
    print(f"Bienvenido a la aplicación de perfiles, {perfil}!")

    if perfil:
        print(f"1. Recuperar perfil")
        print(f"2. Modificar perfil")
        print(f"3. Cambiar perfil")
        print(f"4. Cerrar aplicación")
    else:
        print(f"1. Guardar perfil")
        print(f"2. Recuperar perfil")
        print(f"3. Modificar perfil")
        print(f"4. Cerrar aplicación")

    opcion = input("Por favor, elige una opción (1, 2, 3 o 4): ")

    if perfil and opcion == '1':
        recuperar_perfil(perfil)
    elif perfil and opcion == '2':
        modificar_perfil(perfil)
    elif perfil and opcion == '3':
        nuevo_perfil = cambiar_perfil()
        if nuevo_perfil:
            return nuevo_perfil
    elif perfil and opcion == '4':
        cerrar_aplicacion(perfil)
    elif not perfil and opcion == '1':
        guardar_perfil()
    elif not perfil and opcion == '2':
        recuperar_perfil(perfil)
    elif not perfil and opcion == '3':
        modificar_perfil(perfil)
    elif not perfil and opcion == '4':
        cerrar_aplicacion(perfil)
    else:
        print("Opción inválida. Por favor, elige 1, 2, 3 o 4.")
    return perfil

if __name__ == '__main__':
    cargar_perfiles()
    perfil = seleccionar_perfil()
    
    while True:
        perfil = menu_principal(perfil)