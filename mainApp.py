import os
from cryptography.fernet import Fernet


class GestorContraseñas:
    @staticmethod
    def generar_key():
        if not os.path.exists("filekey.key"):
            key = Fernet.generate_key()

            with open("filekey.key", "wb") as filekey:
                filekey.write(key)
    
    @staticmethod
    def encriptar_perfil():
        with open("filekey.key", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open("perfiles.txt", "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open("perfiles.txt", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    @staticmethod
    def desencriptar_perfil():
        with open("filekey.key", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open("perfiles.txt", "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open("perfiles.txt", "wb") as dec_file:
            dec_file.write(decrypted)

    @staticmethod
    def encriptar_datos(perfil):
        with open("filekey.key", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(f"{perfil}_bloques.txt", "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open(f"{perfil}_bloques.txt", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    @staticmethod
    def desencriptar_datos(perfil):
        with open("filekey.key", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(key)

        with open(f"{perfil}_bloques.txt", "rb") as enc_file:
            encrypted = enc_file.read()

        if encrypted:
            decrypted = fernet.decrypt(encrypted)

            with open(f"{perfil}_bloques.txt", "wb") as dec_file:
                dec_file.write(decrypted)

    @staticmethod
    def cargar_perfiles():
        if os.path.exists("perfiles.txt"):
            GestorContraseñas.desencriptar_perfil()
            return
        else:
            print("No se encontró ningún perfil.")
            nombre = input("Por favor, introduce tu nombre: ")
            contraseña = input("Crea una contraseña: ")

            with open("perfiles.txt", "a") as archivo:
                archivo.write(f"{nombre},{contraseña}\n")

            with open(f"{nombre}_bloques.txt", "a") as archivo:
                pass

            print(f"Perfil de {nombre} guardado correctamente.")

    @staticmethod
    def recuperar_perfil(ultimo_perfil):
        nombre = ultimo_perfil

        with open("perfiles.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if datos[0] == nombre:
                    print(f"Nombre: {datos[0]}")
                    print(f"Contraseña: {datos[1]}")

                    while True:
                        print("1. Volver al menú principal")
                        opcion = input("Ingresa 1: ")

                        if opcion == "1":
                            return
                        else:
                            print("Opción inválida. Por favor, elige 1.")

    @staticmethod
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
                        print("¿Estás seguro de que deseas modificar tu contraseña??")
                        print("1. Sí")
                        print("2. No")

                        opcion_confirmacion = input(
                            "Por favor, elige una opción (1 o 2): "
                        )

                        if opcion_confirmacion == "1":
                            # Realizar la modificación o eliminación
                            contraseña_actual = input(
                                "Introduce tu contraseña actual: "
                            )

                            if contraseña_actual != datos[1]:
                                print(
                                    "Contraseña incorrecta. Volviendo al menú principal."
                                )
                                return

                            contraseña_nueva = input("Introduce tu nueva contraseña: ")
                            lineas[i] = f"{nombre},{contraseña_nueva}\n"

                            print(f"Perfil de {nombre} modificado correctamente.")

                            encontrado = True

                            with open("perfiles.txt", "w") as archivo:
                                archivo.writelines(lineas)

                        elif opcion_confirmacion == "2":
                            encontrado = True
                            break
                        else:
                            print("Opción inválida. Por favor elige 1 o 2.")
                            continue

            if encontrado or opcion == "2":
                break

    @staticmethod
    def seleccionar_perfil():
        with open("perfiles.txt", "r") as archivo:
            perfiles = [linea.strip().split(",")[0] for linea in archivo]

        if len(perfiles) == 1:
            return perfiles[0]

    @staticmethod
    def gestionar_bloques_datos(perfil):
        GestorContraseñas.desencriptar_datos(perfil)

        while True:
            os.system("cls" if os.name == "nt" else "clear")

            print(f"Tarjetas de {perfil}:")

            with open(f"{perfil}_bloques.txt", "r") as archivo:
                bloques = [linea.strip().split(",") for linea in archivo]

                for i, bloque in enumerate(bloques, start=1):
                    print(f"{i}. {bloque[0]} - {bloque[1]}")

                print(f"{len(bloques)+1}. Agregar nueva tarjeta")
                print(f"{len(bloques)+2}. Eliminar tarjeta")
                print(f"{len(bloques)+3}. Volver al perfil")

            opcion_bloque = input(
                f"Por favor, elige una opción (1 al {len(bloques)+3}): "
            )

            if opcion_bloque.isnumeric():
                opcion_bloque = int(opcion_bloque)

                if 1 <= opcion_bloque <= len(bloques):
                    indice = opcion_bloque - 1
                    bloque = bloques[indice]

                    print(f"Nombre de Entidad: {bloque[0]}")
                    print(f"Usuario de Entidad: {bloque[1]}")
                    print(f"Contraseña: {bloque[2]}")
                    print(f"Token: {bloque[3]}")

                    anotaciones = bloque[4:]

                    for i, anotacion in enumerate(anotaciones, start=1):
                        print(f"Anotacion {i}: {anotacion}")

                    print("¿Qué deseas hacer?")
                    print("1. Modificar un dato")
                    print("2. Agregar anotacion")
                    print("3. Eliminar anotacion")
                    print("4. Volver al gestor de contraseñas")

                    opcion_modificar = input("Por favor, elige una opción (1 a 4): ")

                    if opcion_modificar == "1":
                        print("¿Qué dato deseas modificar?")
                        print("1. Nombre de Entidad")
                        print("2. Usuario de Entidad")
                        print("3. Contraseña")
                        print("4. Token")
                        print("5. Anotaciones")
                        print("6. Volver")

                        opcion_modificar_dato = input(
                            "Por favor, elige una opción (1 al 6): "
                        )

                        if opcion_modificar_dato == "1":
                            print(
                                "¿Estás seguro de que deseas modificar el Nombre de Entidad?"
                            )
                            print("1. Sí")
                            print("2. No")

                            opcion_confirmacion = input(
                                "Por favor, elige una opción (1 o 2): "
                            )

                            if opcion_confirmacion == "1":
                                nombre_entidad = input(
                                    "Introduce el nuevo Nombre de Entidad: "
                                )
                                bloque[0] = nombre_entidad

                                with open(f"{perfil}_bloques.txt", "w") as archivo:
                                    for bloque in bloques:
                                        archivo.write(f"{','.join(bloque)}\n")

                            elif opcion_confirmacion == "2":
                                continue

                            else:
                                print(
                                    "Opción inválida. Volviendo al menú de gestión de contraseñas."
                                )
                                continue

                        elif opcion_modificar_dato == "2":
                            print(
                                "¿Estás seguro de que deseas modificar el Usuario de Entidad?"
                            )
                            print("1. Sí")
                            print("2. No")

                            opcion_confirmacion = input(
                                "Por favor, elige una opción (1 o 2): "
                            )

                            if opcion_confirmacion == "1":
                                usuario_entidad = input(
                                    "Introduce el nuevo Usuario de Entidad: "
                                )
                                bloque[1] = usuario_entidad

                                with open(f"{perfil}_bloques.txt", "w") as archivo:
                                    for bloque in bloques:
                                        archivo.write(f"{','.join(bloque)}\n")

                            elif opcion_confirmacion == "2":
                                continue

                            else:
                                print(
                                    "Opción inválida. Volviendo al menú de gestión de contraseñas."
                                )
                                continue

                        elif opcion_modificar_dato == "3":
                            print(
                                "¿Estás seguro de que deseas modificar la Contraseña?"
                            )
                            print("1. Sí")
                            print("2. No")

                            opcion_confirmacion = input(
                                "Por favor, elige una opción (1 o 2): "
                            )

                            if opcion_confirmacion == "1":
                                contraseña_actual = input(
                                    "Introduce tu contraseña actual: "
                                )

                                if contraseña_actual != bloque[2]:
                                    print(
                                        "Contraseña incorrecta. Volviendo al gestor de contraseñas."
                                    )
                                    continue

                                contraseña_nueva = input(
                                    "Introduce la nueva Contraseña: "
                                )
                                bloque[2] = contraseña_nueva

                                with open(f"{perfil}_bloques.txt", "w") as archivo:
                                    for bloque in bloques:
                                        archivo.write(f"{','.join(bloque)}\n")

                            elif opcion_confirmacion == "2":
                                continue

                            else:
                                print(
                                    "Opción inválida. Volviendo al menú de gestión de contraseñas."
                                )
                                continue

                        elif opcion_modificar_dato == "4":
                            print("¿Estás seguro de que deseas modificar el Token?")
                            print("1. Sí")
                            print("2. No")

                            opcion_confirmacion = input(
                                "Por favor, elige una opción (1 o 2): "
                            )

                            if opcion_confirmacion == "1":
                                token = input("Introduce el nuevo Token: ")
                                bloque[3] = token

                                with open(f"{perfil}_bloques.txt", "w") as archivo:
                                    for bloque in bloques:
                                        archivo.write(f"{','.join(bloque)}\n")

                            elif opcion_confirmacion == "2":
                                continue

                            else:
                                print(
                                    "Opción inválida. Volviendo al menú de gestión de contraseñas."
                                )
                                continue

                        elif opcion_modificar_dato == "5":
                            print(
                                "¿Estás seguro de que deseas modificar las Anotaciones?"
                            )
                            print("1. Sí")
                            print("2. No")

                            opcion_confirmacion = input(
                                "Por favor, elige una opción (1 o 2): "
                            )

                            if opcion_confirmacion == "1":
                                print("¿Qué anotación deseas modificar?")

                                for i, anotacion in enumerate(anotaciones, start=1):
                                    print(f"{i}. {anotacion}")

                                opcion_modificar_anotacion = input(
                                    f"Por favor, elige una anotación para modificar (1 al {len(anotaciones)}): "
                                )

                                if opcion_modificar_anotacion.isnumeric():
                                    opcion_modificar_anotacion = int(
                                        opcion_modificar_anotacion
                                    )

                                    if (
                                        1
                                        <= opcion_modificar_anotacion
                                        <= len(anotaciones)
                                    ):
                                        indice_anotacion = (
                                            opcion_modificar_anotacion - 1
                                        )
                                        nueva_anotacion = input(
                                            "Introduce la nueva Anotación: "
                                        )
                                        anotaciones[indice_anotacion] = nueva_anotacion
                                        bloque[4:] = anotaciones
                                        bloques[indice] = bloque

                                        with open(
                                            f"{perfil}_bloques.txt", "w"
                                        ) as archivo:
                                            for bloque in bloques:
                                                archivo.write(f"{','.join(bloque)}\n")

                                        print(f"Anotación modificada correctamente.")

                                    else:
                                        print(
                                            "Opción inválida. Por favor, elige una opción válida."
                                        )

                                else:
                                    print(
                                        "Opción inválida. Por favor, elige una opción numérica."
                                    )

                            elif opcion_confirmacion == "2":
                                continue

                            else:
                                print(
                                    "Opción inválida. Volviendo al menú de gestión de contraseñas."
                                )
                                continue

                        elif opcion_modificar_dato == "6":
                            continue

                    elif opcion_modificar == "2":
                        print("¿Estás seguro de que deseas agregar una Anotacion?")
                        print("1. Sí")
                        print("2. No")

                        opcion_confirmacion = input(
                            "Por favor, elige una opción (1 o 2): "
                        )

                        if opcion_confirmacion == "1":
                            nueva_anotacion = input("Introduce la nueva Anotación: ")
                            bloque.extend([nueva_anotacion])
                            bloques[indice] = bloque

                            with open(f"{perfil}_bloques.txt", "w") as archivo:
                                for bloque in bloques:
                                    archivo.write(f"{','.join(bloque)}\n")

                            print(f"Anotación agregada correctamente.")
                            continue

                        elif opcion_confirmacion == "2":
                            continue

                        else:
                            print(
                                "Opción inválida. Volviendo al menú de gestión de contraseñas."
                            )
                            continue

                    elif opcion_modificar == "3":
                        print("¿Estás seguro de que deseas eliminar una Anotacion?")
                        print("1. Sí")
                        print("2. No")

                        opcion_confirmacion = input(
                            "Por favor, elige una opción (1 o 2): "
                        )

                        if opcion_confirmacion == "1":
                            GestorContraseñas.eliminar_anotacion(bloque)

                            with open(f"{perfil}_bloques.txt", "w") as archivo:
                                for bloque in bloques:
                                    archivo.write(f"{','.join(bloque)}\n")

                        elif opcion_confirmacion == "2":
                            continue

                        else:
                            print(
                                "Opción inválida. Volviendo al menú de gestión de contraseñas."
                            )
                            continue

                    elif opcion_modificar == "4":
                        continue

                elif opcion_bloque == len(bloques) + 1:
                    print("¿Estás seguro de que deseas agregar una nueva tarjeta?")
                    print("1. Sí")
                    print("2. No")

                    opcion_confirmacion = input("Por favor, elige una opción (1 o 2): ")

                    if opcion_confirmacion == "1":
                        nombre_entidad = input("Introduce el Nombre de Entidad: ")
                        usuario_entidad = input("Introduce el Usuario de Entidad: ")
                        contraseña = input("Introduce la Contraseña: ")
                        token = input("Introduce el Token: ")
                        anotaciones = input("Introduce una Anotacion: ")

                        bloques.append(
                            [
                                nombre_entidad,
                                usuario_entidad,
                                contraseña,
                                token,
                                anotaciones,
                            ]
                        )

                        with open(f"{perfil}_bloques.txt", "a") as archivo:
                            archivo.write(f"{','.join(bloques[-1])}\n")

                        print(f"Tarjeta agregada correctamente.")

                    elif opcion_confirmacion == "2":
                        continue

                    else:
                        print(
                            "Opción inválida. Volviendo al menú de gestión de contraseñas."
                        )
                        continue

                elif opcion_bloque == len(bloques) + 2:
                    while True:
                        print(f"Selecciona la tarjeta que deseas eliminar:")

                        for i, bloque in enumerate(bloques, start=1):
                            print(f"{i}. {bloque[0]} - {bloque[1]}")

                        print(f"{len(bloques)+1}. Volver al menú anterior")

                        opcion_eliminar = input(
                            f"Por favor, elige una opción (1 al {len(bloques)+1}): "
                        )

                        if opcion_eliminar.isnumeric():
                            opcion_eliminar = int(opcion_eliminar)

                            if 1 <= opcion_eliminar <= len(bloques):
                                indice = opcion_eliminar - 1
                                bloque_eliminado = bloques.pop(indice)

                                with open(f"{perfil}_bloques.txt", "w") as archivo:
                                    for bloque in bloques:
                                        archivo.write(f"{','.join(bloque)}\n")

                                print(
                                    f"Tarjeta {bloque_eliminado[0]} - {bloque_eliminado[1]} eliminada correctamente."
                                )
                                break

                            elif opcion_eliminar == len(bloques) + 1:
                                break

                            else:
                                print(
                                    "Opción inválida. Por favor, elige una opción válida."
                                )

                        else:
                            print(
                                "Opción inválida. Por favor, elige una opción numérica."
                            )

                elif opcion_bloque == len(bloques) + 3:
                    break

                else:
                    print("Opción inválida. Volviendo al perfil.")

        GestorContraseñas.encriptar_datos(perfil)

    @staticmethod
    def eliminar_anotacion(bloque):
        print("Anotaciones:")
        for i, anotacion in enumerate(bloque[4:], start=1):
            print(f"{i}. {anotacion}")

        opcion_eliminar = input(
            f"Por favor, elige una anotación para eliminar (1 al {len(bloque)-4}): "
        )

        if opcion_eliminar.isnumeric():
            opcion_eliminar = int(opcion_eliminar)

            if 1 <= opcion_eliminar <= len(bloque) - 4:
                bloque.pop(opcion_eliminar + 3)
                print(f"Anotación eliminada correctamente.")
                return
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

        else:
            print("Opción inválida. Por favor, elige una opción numérica.")

    @staticmethod
    def cerrar_aplicacion(perfil):
        print(f"¡Hasta luego, {perfil}! ¡Espero verte pronto!")
        GestorContraseñas.encriptar_perfil()
        exit()

    @staticmethod
    def menu_principal(perfil):
        os.system("cls" if os.name == "nt" else "clear")

        print(f"Bienvenido al gestor de contraseñas, {perfil}!")

        if perfil:
            print(f"1. Gestionar contraseñas")
            print(f"2. Recuperar perfil")
            print(f"3. Modificar perfil")
            print(f"4. Cerrar aplicación")

        opcion = input("Por favor, elige una opción (1 a 4): ")

        if perfil and opcion == "1":
            GestorContraseñas.gestionar_bloques_datos(perfil)

        elif perfil and opcion == "2":
            GestorContraseñas.recuperar_perfil(perfil)

        elif perfil and opcion == "3":
            GestorContraseñas.modificar_perfil(perfil)

        elif perfil and opcion == "4":
            GestorContraseñas.cerrar_aplicacion(perfil)

        else:
            print("Opción inválida. Por favor, elige 1 a 4.")

        return perfil


if __name__ == "__main__":
    GestorContraseñas.generar_key()
    GestorContraseñas.cargar_perfiles()

    perfil = GestorContraseñas.seleccionar_perfil()

    while True:
        perfil = GestorContraseñas.menu_principal(perfil)
