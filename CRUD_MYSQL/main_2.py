from config.db import database
from services.tarea_service import TareaService
from models.tarea import Tarea

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

            service.crear(Tarea(titulo, descripcion, usuario_id))
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
            print("Saliendo del menú tareas...")
            break

        else:
            print("❌ Opción inválida")


# FUNCIÓN PRINCIPAL
def main():
    db = database()
    service = TareaService(db)

    menu_tareas(service)


# EJECUCIÓN
if __name__ == "__main__":
    main()