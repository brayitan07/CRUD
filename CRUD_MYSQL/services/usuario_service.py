from models.usuario import Usuario

class UsuarioService:

    def __init__(self, db):
        self.db = db

    # CREATE
    def crear(self, usuario):

        cursor = self.db.get_cursor()

        cursor.execute(
            "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)",
            (usuario.nombre, usuario.email)
        )

        self.db.commit()

    # READ
    def listar(self):

        cursor = self.db.get_cursor()

        cursor.execute("SELECT * FROM usuarios")

        usuarios = []

        for row in cursor.fetchall():

            usuarios.append(
                Usuario(row[1], row[2], row[0])
            )

        return usuarios

    # UPDATE
    def actualizar(self, usuario):

        cursor = self.db.get_cursor()

        cursor.execute(
            "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",
            (usuario.nombre, usuario.email, usuario.id)
        )

        self.db.commit()

    # DELETE
    def eliminar(self, id):

        cursor = self.db.get_cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id=%s",
            (id,)
        )

        self.db.commit()