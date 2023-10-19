import os
from cryptography.fernet import Fernet


def generar_key():
    if not os.path.exists("filekey.key"):
        key = Fernet.generate_key()
        # string the key in a file
        with open("filekey.key", "wb") as filekey:
            filekey.write(key)


def encriptar_perfil():
    # opening the key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open("perfiles.txt", "rb") as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open("perfiles.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def desencriptar_perfil():
    # opening the key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the encrypted file
    with open("perfiles.txt", "rb") as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open("perfiles.txt", "wb") as dec_file:
        dec_file.write(decrypted)


def encriptar_datos(perfil):
    # opening the key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the original file to encrypt
    with open(f"{perfil}_bloques.txt", "rb") as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    # opening the file in write mode and
    # writing the encrypted data
    with open(f"{perfil}_bloques.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


def desencriptar_datos(perfil):
    # opening the key
    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # opening the encrypted file
    with open(f"{perfil}_bloques.txt", "rb") as enc_file: 
        encrypted = enc_file.read()

    # Only decrypt if the file is not empty
    if encrypted:
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(f"{perfil}_bloques.txt", "wb") as dec_file: 
            dec_file.write(decrypted)


def cargar_perfiles():
    if os.path.exists("perfiles.txt"):
        desencriptar_perfil()
        return
    else:
        print("No se encontró ningún archivo de perfiles.")
        nombre = input("Por favor, introduce tu nombre: ")
        contraseña = input("Crea una contraseña: ")

        with open("perfiles.txt", "a") as archivo:
            archivo.write(f"{nombre},{contraseña}\n")
        with open(f"{nombre}_bloques.txt", "a") as archivo:
            pass
        print(f"Perfil de {nombre} guardado correctamente.")
        print("-" * 30)  # Línea divisoria


def guardar_perfil():
    nombre = input("Por favor, introduce tu nombre: ")
    contraseña = input("Crea una contraseña: ")

    with open("perfiles.txt", "a") as archivo:
        archivo.write(f"{nombre},{contraseña}\n")
    print(f"Perfil de {nombre} guardado correctamente.")
    print("-" * 30)  # Línea divisoria


def recuperar_perfil(ultimo_perfil):
    nombre = ultimo_perfil
    with open("perfiles.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")
            if datos[0] == nombre:
                print(f"Nombre: {datos[0]}")
                print(f"Contraseña: {datos[1]}")
                return
        print(f"No se encontró un perfil para {nombre}.")
    print("-" * 30)  # Línea divisoria


def modificar_perfil(ultimo_perfil):
    while True:
        nombre = ultimo_perfil
        with open("perfiles.txt", "r") as archivo:
            lineas = archivo.readlines()

        encontrado = False
        for i, linea in enumerate(lineas):
            datos = linea.strip().split(",")
            if datos[0] == nombre:
                print(f"1. Modificar Contraseña")
                print(f"2. Volver al menú principal")
                opcion = input("Por favor, elige una opción (1 o 2): ")

                if opcion == "1":
                    contraseña_actual = input("Introduce tu contraseña actual: ")
                    if contraseña_actual != datos[1]:
                        print("Contraseña incorrecta. Volviendo al menú principal.")
                        return

                    contraseña_nueva = input("Introduce tu nueva contraseña: ")
                elif opcion == "2":
                    encontrado = True
                    break
                else:
                    print("Opción inválida. Por favor, elige 1 o 2.")
                    continue

                lineas[i] = f"{nombre},{contraseña_nueva}\n"
                print(f"Perfil de {nombre} modificado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró un perfil para {nombre}.")
        else:
            with open("perfiles.txt", "w") as archivo:
                archivo.writelines(lineas)
        print("-" * 30)  # Línea divisoria

        if encontrado or opcion == "2":
            break


def seleccionar_perfil():
    # Verificamos si hay perfiles guardados
    with open("perfiles.txt", "r") as archivo:
        perfiles = [linea.strip().split(",")[0] for linea in archivo]

    if len(perfiles) == 1:
        return perfiles[0]

    nombre = input("Por favor, introduce tu nombre: ")

    if nombre in perfiles:
        print(f"Bienvenido, {nombre}!")
        return nombre
    else:
        print(f"No se encontró un perfil para {nombre}. ¿Deseas crear uno nuevo?")
        crear_nuevo = input(
            "Ingresa 's' para crear un nuevo perfil, o cualquier otra tecla para salir: "
        )
        if crear_nuevo.lower() == "s":
            contraseña = input("Crea una contraseña: ")

            with open("perfiles.txt", "a") as archivo:
                archivo.write(f"{nombre},{contraseña}\n")
            with open(f"{nombre}_bloques.txt", "a") as archivo:
                pass
            print(f"Perfil de {nombre} guardado correctamente.")
            print("-" * 30)  # Línea divisoria

        return nombre


def cambiar_perfil():
    while True:
        print("Perfiles disponibles:")
        with open("perfiles.txt", "r") as archivo:
            perfiles = [linea.strip().split(",")[0] for linea in archivo]
            for i, perfil in enumerate(perfiles, start=1):
                print(f"{i}. {perfil}")
            print(f"{len(perfiles)+1}. Agregar nuevo perfil")
            print(f"{len(perfiles)+2}. Volver al menú principal")

        opcion = input("Por favor, elige una opción: ")

        if opcion.isnumeric():
            opcion = int(opcion)
            if 1 <= opcion <= len(perfiles):
                return perfiles[opcion - 1]
            elif opcion == len(perfiles) + 1:
                nombre = input("Por favor, introduce tu nombre: ")
                contraseña = input("Crea una contraseña: ")

                with open("perfiles.txt", "a") as archivo:
                    archivo.write(f"{nombre},{contraseña}\n")
                with open(f"{nombre}_bloques.txt", "a") as archivo:
                    pass
                print(f"Perfil de {nombre} guardado correctamente.")
                print("-" * 30)  # Línea divisoria
                return nombre
            elif opcion == len(perfiles) + 2:
                return None

        print("Opción inválida. Volviendo al menú principal.")


def gestionar_bloques_datos(perfil):
    desencriptar_datos(perfil)
    while True:
        print(f"Bloques de datos de {perfil}:")
        # Leer y mostrar bloques de datos
        with open(f"{perfil}_bloques.txt", "r") as archivo:
            bloques = [linea.strip().split(",") for linea in archivo]
            for i, bloque in enumerate(bloques, start=1):
                print(f"{i}. {bloque[0]} - {bloque[1]}")
            print(f"{len(bloques)+1}. Agregar nuevo bloque")
            print(f"{len(bloques)+2}. Volver al perfil")

        opcion_bloque = input(f"Por favor, elige una opción (1 al {len(bloques)+2}): ")

        if opcion_bloque.isnumeric():
            opcion_bloque = int(opcion_bloque)
            if 1 <= opcion_bloque <= len(bloques):
                # Modificar bloque existente
                indice = opcion_bloque - 1
                bloque = bloques[indice]
                print(f"Nombre de Entidad: {bloque[0]}")
                print(f"Usuario de Entidad: {bloque[1]}")
                print(f"Contraseña: {bloque[2]}")
                print(f"Anotaciones: {bloque[3]}")

                print("¿Qué deseas hacer?")
                print("1. Modificar un dato")
                print("2. Volver al gestor de bloques de datos")

                opcion_modificar = input("Por favor, elige una opción (1 o 2): ")

                if opcion_modificar == "1":
                    print("¿Qué dato deseas modificar?")
                    print("1. Nombre de Entidad")
                    print("2. Usuario de Entidad")
                    print("3. Contraseña")
                    print("4. Anotaciones")
                    print("5. Modificar todos los datos")
                    print("6. Volver")

                    opcion_modificar_dato = input(
                        "Por favor, elige una opción (1 al 6): "
                    )

                    if opcion_modificar_dato == "1":
                        nombre_entidad = input("Introduce el nuevo Nombre de Entidad: ")
                        bloque[0] = nombre_entidad
                    elif opcion_modificar_dato == "2":
                        usuario_entidad = input(
                            "Introduce el nuevo Usuario de Entidad: "
                        )
                        bloque[1] = usuario_entidad
                    elif opcion_modificar_dato == "3":
                        contraseña_actual = input("Introduce tu contraseña actual: ")
                        if contraseña_actual != bloque[2]:
                            print(
                                "Contraseña incorrecta. Volviendo al gestor de bloques de datos."
                            )
                            continue
                        contraseña_nueva = input("Introduce la nueva Contraseña: ")
                        bloque[2] = contraseña_nueva
                    elif opcion_modificar_dato == "4":
                        anotaciones = input("Introduce las nuevas Anotaciones: ")
                        bloque[3] = anotaciones
                    elif opcion_modificar_dato == "5":
                        print(
                            "Por motivos de seguridad, se le pedira su contraseña actual antes de proseguir."
                        )
                        contraseña_actual = input("Introduce tu contraseña actual: ")
                        if contraseña_actual != bloque[2]:
                            print(
                                "Contraseña incorrecta. Volviendo al gestor de bloques de datos."
                            )
                            continue
                        nombre_entidad = input("Introduce el nuevo Nombre de Entidad: ")
                        usuario_entidad = input(
                            "Introduce el nuevo Usuario de Entidad: "
                        )
                        contraseña_nueva = input("Introduce la nueva Contraseña: ")
                        anotaciones = input("Introduce las nuevas Anotaciones: ")

                        bloque = [
                            nombre_entidad,
                            usuario_entidad,
                            contraseña_nueva,
                            anotaciones,
                        ]
                    elif opcion_modificar_dato == "6":
                        continue

                    bloques[indice] = bloque

                    with open(f"{perfil}_bloques.txt", "w") as archivo:
                        for bloque in bloques:
                            archivo.write(f"{','.join(bloque)}\n")

                    print(f"Bloque modificado correctamente.")
                elif opcion_modificar == "2":
                    continue
            elif opcion_bloque == len(bloques) + 1:
                # Agregar nuevo bloque
                nombre_entidad = input("Introduce el Nombre de Entidad: ")
                usuario_entidad = input("Introduce el Usuario de Entidad: ")
                contraseña = input("Introduce la Contraseña: ")
                anotaciones = input("Introduce las Anotaciones: ")

                bloques.append(
                    [nombre_entidad, usuario_entidad, contraseña, anotaciones]
                )

                with open(f"{perfil}_bloques.txt", "a") as archivo:
                    archivo.write(f"{','.join(bloques[-1])}\n")

                print(f"Bloque agregado correctamente.")
            elif opcion_bloque == len(bloques) + 2:
                # Volver al perfil
                break
        else:
            print("Opción inválida. Volviendo al perfil.")
    encriptar_datos(perfil)


def cerrar_aplicacion(perfil):
    print(f"¡Hasta luego, {perfil}! ¡Espero verte pronto!")
    encriptar_perfil()
    exit()


def guardar_ultimo_perfil(perfil):
    with open("ultimo_perfil.txt", "w") as archivo:
        archivo.write(perfil)


def obtener_ultimo_perfil():
    if os.path.exists("ultimo_perfil.txt"):
        with open("ultimo_perfil.txt", "r") as archivo:
            return archivo.read().strip()
    return None


def menu_principal(perfil):
    print("-" * 30)
    print(f"Bienvenido a la aplicación de perfiles, {perfil}!")

    if perfil:
        print(f"1. Gestionar bloques de datos")
        print(f"2. Recuperar perfil")
        print(f"3. Modificar perfil")
        print(f"4. Cambiar perfil")
        print(f"5. Cerrar aplicación")
    else:
        print(f"1. Guardar perfil")
        print(f"2. Recuperar perfil")
        print(f"3. Modificar perfil")
        print(f"4. Cerrar aplicación")

    opcion = input("Por favor, elige una opción (1, 2, 3, 4 o 5): ")

    if perfil and opcion == "1":
        gestionar_bloques_datos(perfil)
    elif perfil and opcion == "2":
        recuperar_perfil(perfil)
    elif perfil and opcion == "3":
        modificar_perfil(perfil)
    elif perfil and opcion == "4":
        nuevo_perfil = cambiar_perfil()
        if nuevo_perfil:
            return nuevo_perfil
    elif perfil and opcion == "5":
        cerrar_aplicacion(perfil)
    elif not perfil and opcion == "1":
        guardar_perfil()
    elif not perfil and opcion == "2":
        recuperar_perfil(perfil)
    elif not perfil and opcion == "3":
        modificar_perfil(perfil)
    elif not perfil and opcion == "4":
        cerrar_aplicacion(perfil)
    else:
        print("Opción inválida. Por favor, elige 1, 2, 3, 4 o 5.")
    return perfil


if __name__ == "__main__":
    generar_key()
    cargar_perfiles()
    perfil = seleccionar_perfil()

    while True:
        perfil = menu_principal(perfil)
