class Tarea:
    # Se crea la clase Tarea.
    # Una clase sirve como plantilla para crear objetos.

    def __init__(self, titulo, descripcion, usuario_id, categoria_id, id=None):
        # El método __init__ se ejecuta automáticamente al crear un objeto.
        # Sirve para inicializar los atributos del objeto.

        self.id = id
        # Guarda el id de la tarea.
        # Por defecto vale None si no se envía un valor.

        self.titulo = titulo
        # Guarda el título de la tarea.

        self.descripcion = descripcion
        # Guarda la descripción de la tarea.

        self.usuario_id = usuario_id
        # Guarda el id del usuario al que pertenece la tarea.

        self.categoria_id = categoria_id

    def __str__(self):
        # El método __str__ sirve para mostrar el objeto en forma de texto.
        # Se ejecuta automáticamente cuando usamos print().

        return f"ID: {self.id} - Titulo: {self.titulo} - Descrpcion: {self.descripcion} - Usuario: {self.usuario_id} Categoria: {self.categoria_id}"
        # Retorna un texto con los datos de la tarea usando f-string.
