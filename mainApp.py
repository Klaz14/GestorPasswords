import os

def guardar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    contraseña = input("Crea una contraseña: ")

    with open('perfiles.txt', 'a') as archivo:
        archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
    print(f"Perfil de {nombre} guardado correctamente.")
    print('-'*30)  # Línea divisoria

def recuperar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
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

def modificar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
    with open('perfiles.txt', 'r') as archivo:
        lineas = archivo.readlines()

    encontrado = False
    with open('perfiles.txt', 'w') as archivo:
        for linea in lineas:
            datos = linea.strip().split(',')
            if datos[0] == nombre:
                print(f"1. Modificar Fecha de Nacimiento")
                print(f"2. Modificar Contraseña")
                opcion = input("Por favor, elige una opción (1 o 2): ")
                if opcion == '1':
                    fecha_nacimiento = input("Introduce tu nueva fecha de nacimiento (dd/mm/aaaa): ")
                    contraseña = datos[2]
                elif opcion == '2':
                    fecha_nacimiento = datos[1]
                    contraseña = input("Introduce tu nueva contraseña: ")
                else:
                    print("Opción inválida. No se realizaron cambios.")
                    archivo.write(linea)
                    continue
                archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
                print(f"Perfil de {nombre} modificado correctamente.")
                encontrado = True
            else:
                archivo.write(linea)

    if not encontrado:
        print(f"No se encontró un perfil para {nombre}.")
    print('-'*30)  # Línea divisoria

def cerrar_aplicacion():
    exit()

def obtener_ultimo_perfil():
    if os.path.exists('ultimo_perfil.txt'):
        with open('ultimo_perfil.txt', 'r') as archivo:
            return archivo.read().strip()
    return None

def guardar_ultimo_perfil(perfil):
    with open('ultimo_perfil.txt', 'w') as archivo:
        archivo.write(perfil)

def menu_principal():
    ultimo_perfil = obtener_ultimo_perfil()

    if ultimo_perfil:
        respuesta = input(f"¿Eres {ultimo_perfil}? (s/n): ")
        if respuesta.lower() == 's':
            print(f"Bienvenido de nuevo, {ultimo_perfil}!")
        else:
            ultimo_perfil = None

    if not ultimo_perfil:
        nombre = input("Por favor, introduce tu nombre: ")
        guardar_ultimo_perfil(nombre)

    print('-'*30)
    print("Bienvenido a la aplicación de perfiles.")
    print("1. Guardar perfil")
    print("2. Recuperar perfil")
    print("3. Modificar perfil")
    print("4. Cerrar aplicación")

    opcion = input("Por favor, elige una opción (1, 2, 3 o 4): ")

    if opcion == '1':
        guardar_perfil()
    elif opcion == '2':
        recuperar_perfil()
    elif opcion == '3':
        modificar_perfil()
    elif opcion == '4':
        cerrar_aplicacion()
    else:
        print("Opción inválida. Por favor, elige 1, 2, 3 o 4.")
    print('-'*30)

if __name__ == '__main__':
    while True:
        menu_principal()