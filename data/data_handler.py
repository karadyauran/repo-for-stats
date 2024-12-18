import sqlite3

# This module is responsible for creating and managing the database schema.

DATABASE_FILE = 'finance_manager.db'

# SQL statements for creating tables
create_user_table_sql = '''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    hashed_password TEXT NOT NULL
);
'''

create_income_table_sql = '''
CREATE TABLE IF NOT EXISTS incomes (
    income_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
'''

create_expense_table_sql = '''
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
'''

create_budget_table_sql = '''
CREATE TABLE IF NOT EXISTS budgets (
    budget_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    category TEXT NOT NULL,
    limit REAL NOT NULL,
    period TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
'''

create_goal_table_sql = '''
CREATE TABLE IF NOT EXISTS financial_goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    target_amount REAL NOT NULL,
    current_amount REAL NOT NULL,
    due_date TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);
'''

def setup_database():
    """Sets up the required database tables"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(create_user_table_sql)
        cursor.execute(create_income_table_sql)
        cursor.execute(create_expense_table_sql)
        cursor.execute(create_budget_table_sql)
        cursor.execute(create_goal_table_sql)
    print("Database setup complete.")

# The `setup_database` function should be called during application initialization to ensure that the database schema is prepared. 
# This file handles direct interactions with the database, including schema creation and management.