# data/database.py

import sqlite3
from pathlib import Path

class DatabaseManager:
    """
    A class to manage interactions with the SQLite database.
    """

    def __init__(self, db_name: str = "finance_tracker.db"):
        """
        Initializes the database connection.
        :param db_name: Name of the database file.
        """
        # Set the database file path
        self.db_path = Path(db_name)
        # Initialize a database connection
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        """
        Support the with-statement context manager protocol.
        """
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Automatically close the database connection on exiting the context.
        """
        self.close()

    def close(self):
        """
        Close the connection to the database.
        """
        if self.conn:
            self.conn.close()

    def initialize_tables(self):
        """
        Create necessary tables if they do not exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')
        self.conn.commit()

    def execute_query(self, query: str, params: tuple = ()):
        """
        Execute a parameterized SQL query.
        :param query: SQL statement to be executed.
        :param params: Parameters for the SQL statement.
        :return: Cursor with executed results.
        """
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor

    def fetchall(self, query: str, params: tuple = ()):
        """
        Execute a query and return all rows.
        :param query: SQL statement to be executed.
        :param params: Parameters for the SQL statement.
        :return: List of all matching records.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query: str, params: tuple = ()):
        """
        Execute a query and return a single row.
        :param query: SQL statement to be executed.
        :param params: Parameters for the SQL statement.
        :return: A single matching record or None.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()