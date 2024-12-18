import sqlite3
from src.entities import User, Income, Expense, Budget, FinancialGoal
from typing import List

class DatabaseConnection:
    def __init__(self, db_file: str):
        self.db_file = db_file

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        self.conn.close()

# UserRepository handles database operations for User entities
class UserRepository:

    def add_user(self, user: User) -> None:
        with DatabaseConnection('finance_manager.db') as cursor:
            cursor.execute(
                """INSERT INTO users (username, hashed_password) VALUES (?, ?)""",
                (user.username, user.hashed_password)
            )

    def get_user_by_id(self, user_id: int) -> User:
        with DatabaseConnection('finance_manager.db') as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()
            if result:
                return User(*result)

# IncomeRepository for Income-related database operations
class IncomeRepository:

    def get_incomes_for_user(self, user_id: int) -> List[Income]:
        with DatabaseConnection('finance_manager.db') as cursor:
            cursor.execute("SELECT * FROM incomes WHERE user_id = ?", (user_id,))
            return [Income(*row) for row in cursor.fetchall()]

# Similar Repository classes can be created for Expense, Budget, and FinancialGoal

# The repository classes serve as a layer between the domain entities and the database, allowing for clean separation and maintainability of code.