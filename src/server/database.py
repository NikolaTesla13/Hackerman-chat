import pretty_errors
import sqlite3

class Database:
    def __init__(self, file):
        self.connection = sqlite3.connect(file, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                token TEXT,
                friend TEXT 
            )
        """)
        self.connection.commit()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                reciver TEXT,
                sender TEXT,
                content TEXT
            )
        """)
        self.connection.commit()

    def close_connection(self):
        self.connection.commit()
        self.connection.close()