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
            "INSERT INTO tareas (titulo, descripcion, usuario_id) VALUES (%s, %s, %s)",
            (tarea.titulo, tarea.descripcion, tarea.usuario_id),
        )
        # Inserta una nueva tarea en la tabla tareas.
        # Los valores se toman del objeto tarea.

        self.db.commit()
        # Guarda los cambios en la base de datos.

    # READ
    def listar(self):
        # Método para listar todas las tareas.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute("""
        SELECT t.id, t.titulo, t.descripcion, u.nombre
        FROM tareas t
        INNER JOIN usuarios u
        ON t.usuario_id = u.id
    """)
        # Consulta SQL:
        # SELECT obtiene datos.
        # INNER JOIN une la tabla tareas con la tabla usuarios.
        # ON indica la relación entre ambas tablas.

        return cursor.fetchall()
        # fetchall() devuelve todos los registros encontrados.

    # UPDATE
    def actualizar(self, tarea):
        # Método para actualizar una tarea existente.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute(
            "UPDATE tareas SET titulo=%s, descripcion=%s, usuario_id=%s WHERE id=%s",
            (tarea.titulo, tarea.descripcion, tarea.usuario_id, tarea.id),
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
