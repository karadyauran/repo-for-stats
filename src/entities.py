from dataclasses import dataclass
from typing import Optional

# Entity: User
@dataclass
class User:
    user_id: int
    username: str
    hashed_password: str

# Entity: Income
@dataclass
class Income:
    income_id: int
    user_id: int
    amount: float
    category: str
    date: str  # Consider using datetime.date for more accuracy

# Entity: Expense
@dataclass
class Expense:
    expense_id: int
    user_id: int
    amount: float
    category: str
    date: str  # Consider using datetime.date for more accuracy

# Entity: Budget
@dataclass
class Budget:
    budget_id: int
    user_id: int
    category: str
    limit: float
    period: str  # Could be 'monthly', 'weekly', etc.

# Entity: FinancialGoal
@dataclass
class FinancialGoal:
    goal_id: int
    user_id: int
    name: str
    target_amount: float
    current_amount: float
    due_date: Optional[str]  # Consider using datetime.date to handle dates properly

# Define additional logic as needed

# Dataclasses provide a convenient way to store data and can be extended with methods for additional functionality when needed. Each entity corresponds to a database table in a clean architecture setup. They can be extended with additional fields or methods as the application evolves.