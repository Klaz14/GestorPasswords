import os

def guardar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
    fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    contraseña = input("Crea una contraseña: ")

    with open('perfiles.txt', 'a') as archivo:
        archivo.write(f"{nombre},{fecha_nacimiento},{contraseña}\n")
    print(f"Perfil de {nombre} guardado correctamente.")

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

def main():
    print("Bienvenido a la aplicación de perfiles.")
    print("1. Guardar perfil")
    print("2. Recuperar perfil")

    opcion = input("Por favor, elige una opción (1 o 2): ")

    if opcion == '1':
        guardar_perfil()
    elif opcion == '2':
        recuperar_perfil()
    else:
        print("Opción inválida. Por favor, elige 1 o 2.")

if __name__ == '__main__':
    main()
