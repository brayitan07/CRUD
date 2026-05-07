class Usuario:
    # Se crea la clase Usuario.
    # Esta clase sirve como plantilla para crear usuarios.

    def __init__(self, nombre, email, id=None):
        # El método __init__ se ejecuta automáticamente
        # cuando se crea un objeto.

        self.id = id
        # Guarda el id del usuario.
        # Por defecto vale None si no se envía un valor.

        self.nombre = nombre
        # Guarda el nombre del usuario.

        self.email = email
        # Guarda el correo electrónico del usuario.

    def __str__(self):
        # El método __str__ sirve para mostrar el objeto como texto.
        # Se ejecuta automáticamente al usar print().

        return f"{self.id} - {self.nombre} - {self.email}"
        # Retorna un texto con la información del usuario.
