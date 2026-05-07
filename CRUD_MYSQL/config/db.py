import mysql.connector

class database:

    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ejemplo_db"
        )

        print("✅ Conectado a MySQL")

    def get_cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()