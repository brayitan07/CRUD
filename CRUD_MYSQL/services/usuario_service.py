from models.usuario import Usuario
# Importa la clase Usuario desde la carpeta models.

class UsuarioService:
    # Se crea la clase UsuarioService.
    # Esta clase maneja las operaciones CRUD de usuarios.

    def __init__(self, db):
        # El método __init__ se ejecuta automáticamente
        # cuando se crea un objeto.

        self.db = db
        # Guarda la conexión de la base de datos.

    # CREATE
    def crear(self, usuario):
        # Método para crear un nuevo usuario.

        cursor = self.db.get_cursor()
        # Obtiene un cursor para ejecutar consultas SQL.

        cursor.execute(
            "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
            (usuario.nombre, usuario.email)
        )
        # INSERT INTO agrega un nuevo registro en la tabla usuarios.
        # Se insertan el nombre y email del objeto usuario.

        self.db.commit()
        # Guarda los cambios en la base de datos.

    # READ
    def listar(self):
        # Método para listar todos los usuarios.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute("SELECT * FROM usuarios")
        # SELECT * obtiene todos los datos de la tabla usuarios.

        usuarios = []
        # Se crea una lista vacía para guardar los usuarios.

        for row in cursor.fetchall():
            # Recorre todos los registros obtenidos.

            usuarios.append(
                Usuario(row[1], row[2], row[0])
            )
            # Crea un objeto Usuario con los datos de cada fila
            # y lo agrega a la lista usuarios.
            #
            # row[0] = id
            # row[1] = nombre
            # row[2] = email

        return usuarios
        # Retorna la lista de usuarios.

    # UPDATE
    def actualizar(self, usuario):
        # Método para actualizar un usuario existente.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute(
            "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
            (usuario.nombre, usuario.email, usuario.id)
        )
        # UPDATE modifica los datos del usuario.
        # WHERE id=%s indica qué usuario se actualizará.

        self.db.commit()
        # Guarda los cambios.

    # DELETE
    def eliminar(self, id):
        # Método para eliminar un usuario.

        cursor = self.db.get_cursor()
        # Obtiene un cursor.

        cursor.execute(
            "DELETE FROM usuarios WHERE id=%s",
            (id,)
        )
        # DELETE elimina el usuario según el id enviado.

        self.db.commit()
        # Guarda los cambios en la base de datos.