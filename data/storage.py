# data/storage.py

from data.database import DatabaseManager

class UserStorage:
    """
    Class to handle operations related to user data storage using the database.
    """
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def add_user(self, username: str, password: str) -> bool:
        """
        Add a new user to the database.
        :return: Boolean indicating success or failure.
        """
        try:
            self.db_manager.execute_query(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
            )
            return True
        except Exception:
            return False

    def get_user(self, username: str) -> tuple:
        """
        Retrieve a user's record by username.
        :return: Tuple containing user record or None.
        """
        return self.db_manager.fetchone(
            "SELECT * FROM users WHERE username = ?", (username,)
        )

class TransactionStorage:
    """
    Class to handle operations related to transaction data storage using the database.
    """
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def add_transaction(self, user_id: int, timestamp: str, amount: float, category: str, trans_type: str) -> bool:
        """
        Add a new transaction to the database.
        :return: Boolean indicating success or failure.
        """
        try:
            self.db_manager.execute_query(
                """
                INSERT INTO transactions (user_id, timestamp, amount, category, type)
                VALUES (?, ?, ?, ?, ?)""",
                (user_id, timestamp, amount, category, trans_type)
            )
            return True
        except Exception:
            return False

    def get_user_transactions(self, user_id: int) -> list:
        """
        Retrieve all transactions for a specific user.
        :return: List of transactions.
        """
        return self.db_manager.fetchall(
            "SELECT * FROM transactions WHERE user_id = ?", (user_id,)
        )