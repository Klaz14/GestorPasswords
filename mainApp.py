import os

def guardar_datos():
    nombre = input("Por favor, introduce tu nombre: ")
    with open('datos.txt', 'w') as archivo:
        archivo.write(nombre)

def recuperar_datos():
    if os.path.exists('datos.txt'):
        with open('datos.txt', 'r') as archivo:
            nombre = archivo.read()
            print(f"Hola, {nombre}!")
    else:
        print("No se encontraron datos guardados.")

def main():
    print("Bienvenido a la aplicación de guardado de datos.")
    print("1. Guardar datos")
    print("2. Recuperar datos")

    opcion = input("Por favor, elige una opción (1 o 2): ")

    if opcion == '1':
        guardar_datos()
    elif opcion == '2':
        recuperar_datos()
    else:
        print("Opción inválida. Por favor, elige 1 o 2.")

if __name__ == '__main__':
    main()
