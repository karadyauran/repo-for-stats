import hashlib
import os
import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Utility function for hashing passwords securely

def generate_hashed_password(password: str) -> str:
    salt = os.urandom(32)  # A new salt for a new user
    pwdhash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return salt + pwdhash

# Utility function to format datetime to string

def get_current_timestamp() -> str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Utility function to convert a string date to a datetime object

def string_to_date(date_string: str) -> datetime.date:
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").date()

# Utility function to compare budgets

def is_budget_exceeded(expenses: float, budget: float) -> bool:
    return expenses > budget

# The utils module provides a set of helper functions used across multiple modules for common operations such as password handling and date formatting.