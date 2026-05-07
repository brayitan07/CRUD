from config.db import database
# Importa la clase database desde la carpeta config.

from services.usuario_service import UsuarioService
# Importa el servicio de usuarios.

from services.tarea_service import TareaService
# Importa el servicio de tareas.

from models.usuario import Usuario
# Importa el modelo Usuario.

from models.tarea import Tarea
# Importa el modelo Tarea.


# =========================
# MENU USUARIOS
# =========================
def menu_usuarios(service):
    # Función que muestra el menú CRUD de usuarios.

    while True:
        # while True crea un ciclo infinito hasta usar break.

        print("\n--- CRUD USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Volver")

        op = input("Opción: ")
        # input() permite escribir datos desde teclado.

        # CREAR
        if op == "1":

            nombre = input("Nombre: ")
            # Pide el nombre del usuario.

            email = input("Email: ")
            # Pide el correo del usuario.

            service.crear(Usuario(nombre, email))
            # Crea un objeto Usuario y lo guarda en la base de datos.

            print("✅ Usuario creado")

        # LISTAR
        elif op == "2":

            usuarios = service.listar()
            # Obtiene la lista de usuarios.

            print("\n--- LISTA USUARIOS ---")

            for u in usuarios:
                # Recorre cada usuario de la lista.

                print(u)
                # Muestra el usuario usando __str__().

        # ACTUALIZAR
        elif op == "3":

            id_usuario = int(input("ID: "))
            # Pide el id del usuario y lo convierte a entero.

            nombre = input("Nuevo nombre: ")
            # Pide el nuevo nombre.

            email = input("Nuevo email: ")
            # Pide el nuevo correo.

            service.actualizar(
                Usuario(nombre, email, id_usuario)
            )
            # Actualiza el usuario con los nuevos datos.

            print("✅ Usuario actualizado")

        # ELIMINAR
        elif op == "4":

            id_usuario = int(input("ID: "))
            # Pide el id del usuario.

            service.eliminar(id_usuario)
            # Elimina el usuario.

            print("✅ Usuario eliminado")

        # VOLVER
        elif op == "5":
            # Sale del menú usuarios.

            break

        else:
            print("❌ Opción inválida")
            # Mensaje si la opción no existe.


# =========================
# MENU TAREAS
# =========================
def menu_tareas(service):
    # Función que muestra el menú CRUD de tareas.

    while True:

        print("\n--- CRUD TAREAS ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Volver")

        opcion = input("Opción: ")
        # Guarda la opción escrita por el usuario.

        # CREAR
        if opcion == "1":

            titulo = input("Título: ")
            # Pide el título de la tarea.

            descripcion = input("Descripción: ")
            # Pide la descripción.

            usuario_id = int(input("ID Usuario: "))
            # Pide el id del usuario.

            service.crear(
                Tarea(titulo, descripcion, usuario_id)
            )
            # Crea y guarda una nueva tarea.

            print("✅ Tarea creada correctamente")

        # LISTAR
        elif opcion == "2":

            tareas = service.listar()
            # Obtiene todas las tareas.

            print("\n--- LISTA DE TAREAS ---")

            for t in tareas:
                # Recorre cada tarea.

                print(f"{t[0]} | {t[1]} | {t[2]} | Usuario: {t[3]}")
                # Muestra:
                # t[0] = id
                # t[1] = título
                # t[2] = descripción
                # t[3] = nombre usuario

        # ACTUALIZAR
        elif opcion == "3":

            id_tarea = int(input("ID tarea: "))
            # Pide el id de la tarea.

            titulo = input("Nuevo título: ")
            # Pide el nuevo título.

            descripcion = input("Nueva descripción: ")
            # Pide la nueva descripción.

            usuario_id = int(input("Nuevo ID usuario: "))
            # Pide el nuevo id de usuario.

            tarea = Tarea(titulo, descripcion, usuario_id)
            # Crea el objeto tarea.

            tarea.id = id_tarea
            # Asigna el id de la tarea.

            service.actualizar(tarea)
            # Actualiza la tarea.

            print("✅ Tarea actualizada correctamente")

        # ELIMINAR
        elif opcion == "4":

            id_tarea = int(input("ID tarea a eliminar: "))
            # Pide el id de la tarea.

            service.eliminar(id_tarea)
            # Elimina la tarea.

            print("✅ Tarea eliminada correctamente")

        # VOLVER
        elif opcion == "5":
            # Sale del menú tareas.

            break

        else:
            print("❌ Opción inválida")
            # Mensaje si la opción es incorrecta.


# =========================
# MAIN PRINCIPAL
# =========================
def main():
    # Función principal del programa.

    db = database()
    # Crea la conexión con la base de datos.

    usuario_service = UsuarioService(db)
    # Crea el servicio de usuarios.

    tarea_service = TareaService(db)
    # Crea el servicio de tareas.

    while True:

        print("\n========== SISTEMA CRUD ==========")
        print("1. CRUD Usuarios")
        print("2. CRUD Tareas")
        print("3. Salir")

        op = input("Seleccione una opción: ")
        # Guarda la opción del usuario.

        if op == "1":
            menu_usuarios(usuario_service)
            # Abre el menú de usuarios.

        elif op == "2":
            menu_tareas(tarea_service)
            # Abre el menú de tareas.

        elif op == "3":

            db.close()
            # Cierra la conexión con la base de datos.

            print("👋 Saliendo del sistema...")
            # Mensaje de salida.

            break
            # Finaliza el programa.

        else:
            print("❌ Opción inválida")
            # Mensaje si la opción no existe.


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    # Verifica si este archivo es el principal.

    main()
    # Ejecuta la función principal.