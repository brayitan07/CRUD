import mysql.connector  # Importa el conector de MySQL para poder conectar Python con la base de datos.

class database:  # Se crea una clase llamada database.

    def __init__(self):
        # El método __init__ se ejecuta automáticamente al crear un objeto.
        
        self.connection = None  
        # Se crea la variable connection y se inicia vacía.

        self.connect()  
        # Llama al método connect() para realizar la conexión con MySQL.

    def connect(self):
        # Método encargado de conectarse a la base de datos.

        self.connection = mysql.connector.connect(
            host="localhost",  
            # Dirección del servidor MySQL. localhost significa tu propio computador.

            user="root",  
            # Usuario de MySQL.

            password="",  
            # Contraseña del usuario. Aquí está vacía.

            database="ejemplo_db"  
            # Nombre de la base de datos a utilizar.
        )

        print("Conectado a MySQL")  
        # Muestra un mensaje indicando que la conexión fue exitosa.

    def get_cursor(self):
        # Este método crea y devuelve un cursor.
        # El cursor sirve para ejecutar consultas SQL.

        return self.connection.cursor()

    def commit(self):
        # Guarda permanentemente los cambios realizados en la base de datos.
        
        self.connection.commit()

    def close(self):
        # Cierra la conexión con la base de datos.
        
        self.connection.close()