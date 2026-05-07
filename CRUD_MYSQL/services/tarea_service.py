from models.tarea import Tarea

# Importa la clase Tarea desde la carpeta models.


class TareaService:
    # Se crea la clase TareaService.
    # Esta clase se encarga de manejar las operaciones de las tareas en la base de datos.

    def __init__(self, db):
        # El método __init__ se ejecuta automáticamente al crear el objeto.

        self.db = db
        # Guarda la conexión de la base de datos en la variable db.

    # CREATE
    def crear(self, tarea):
        # Método para crear una nueva tarea en la base de datos.

        cursor = self.db.get_cursor()
        # Obtiene un cursor para ejecutar consultas SQL.

        cursor.execute(
            "INSERT INTO tareas (titulo, descripcion, usuario_id, categoria_id) VALUES (%s, %s, %s, %s)",
            (tarea.titulo, tarea.descripcion, tarea.usuario_id),
        )
        # Inserta una nueva tarea en la tabla tareas.
        # Los valores se toman del objeto tarea.

        self.db.commit()
        # Guarda los cambios en la base de datos.


    def listar(self):
        cursor = self.db.get_cursor()
        cursor.execute("""
            SELECT tareas.id,
                   tareas.titulo,
                   tareas.descripcion,
                   usuarios.nombre
            FROM tareas
            INNER JOIN usuarios
            ON tareas.usuario_id = usuarios.id
        """)
        tareas = cursor.fetchall()
        return tareas

    # UPDATE
    def actualizar(self, tarea):
        # Método para actualizar una tarea existente.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute(
            "UPDATE tareas SET titulo=%s, descripcion=%s, usuario_id=%s,  categoria_id=%s WHERE id=%s",
            (
                tarea.titulo,
                tarea.descripcion,
                tarea.usuario_id,
                tarea.categoria_id,
                tarea.id
            ),
        )
        # UPDATE modifica datos de una tarea.
        # WHERE id=%s indica qué tarea se va a actualizar.

        self.db.commit()
        # Guarda los cambios.

    # DELETE
    def eliminar(self, id):
        # Método para eliminar una tarea.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute("DELETE FROM tareas WHERE id=%s", (id,))
        # DELETE elimina una tarea según su id.

        self.db.commit()
        # Guarda los cambios en la base de datos.
