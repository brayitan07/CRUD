from config.db import database

from services.usuario_service import UsuarioService
from services.tarea_service import TareaService

from models.usuario import Usuario
from models.tarea import Tarea


# =========================
# MENU USUARIOS
# =========================
def menu_usuarios(service):

    while True:

        print("\n--- CRUD USUARIOS ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Volver")

        op = input("Opción: ")

        # CREAR
        if op == "1":

            nombre = input("Nombre: ")
            email = input("Email: ")

            service.crear(Usuario(nombre, email))

            print("✅ Usuario creado")

        # LISTAR
        elif op == "2":

            usuarios = service.listar()

            print("\n--- LISTA USUARIOS ---")

            for u in usuarios:
                print(u)

        # ACTUALIZAR
        elif op == "3":

            id_usuario = int(input("ID: "))
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")

            service.actualizar(
                Usuario(nombre, email, id_usuario)
            )

            print("✅ Usuario actualizado")

        # ELIMINAR
        elif op == "4":

            id_usuario = int(input("ID: "))

            service.eliminar(id_usuario)

            print("✅ Usuario eliminado")

        # VOLVER
        elif op == "5":
            break

        else:
            print("❌ Opción inválida")


# =========================
# MENU TAREAS
# =========================
def menu_tareas(service):

    while True:

        print("\n--- CRUD TAREAS ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Volver")

        opcion = input("Opción: ")

        # CREAR
        if opcion == "1":

            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            usuario_id = int(input("ID Usuario: "))

            service.crear(
                Tarea(titulo, descripcion, usuario_id)
            )

            print("✅ Tarea creada correctamente")

        # LISTAR
        elif opcion == "2":

            tareas = service.listar()

            print("\n--- LISTA DE TAREAS ---")

            for t in tareas:
                print(f"{t[0]} | {t[1]} | {t[2]} | Usuario: {t[3]}")

        # ACTUALIZAR
        elif opcion == "3":

            id_tarea = int(input("ID tarea: "))
            titulo = input("Nuevo título: ")
            descripcion = input("Nueva descripción: ")
            usuario_id = int(input("Nuevo ID usuario: "))

            tarea = Tarea(titulo, descripcion, usuario_id)
            tarea.id = id_tarea

            service.actualizar(tarea)

            print("✅ Tarea actualizada correctamente")

        # ELIMINAR
        elif opcion == "4":

            id_tarea = int(input("ID tarea a eliminar: "))

            service.eliminar(id_tarea)

            print("✅ Tarea eliminada correctamente")

        # VOLVER
        elif opcion == "5":
            break

        else:
            print("❌ Opción inválida")


# =========================
# MAIN PRINCIPAL
# =========================
def main():

    db = database()

    usuario_service = UsuarioService(db)
    tarea_service = TareaService(db)

    while True:

        print("\n========== SISTEMA CRUD ==========")
        print("1. CRUD Usuarios")
        print("2. CRUD Tareas")
        print("3. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            menu_usuarios(usuario_service)

        elif op == "2":
            menu_tareas(tarea_service)

        elif op == "3":

            db.close()

            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida")


# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    main()