from src.services import UserService, IncomeService
from src.repositories import UserRepository, IncomeRepository

class UserController:
    """Controller for handling incoming user-related commands and requests"""

    def __init__(self):
        user_repo = UserRepository()
        self.user_service = UserService(user_repo)

    def create_user(self, username: str, password: str):
        user = self.user_service.register_user(username, password)
        return f"User {user.username} created with ID {user.user_id}"

    def get_user_info(self, user_id: int):
        user = self.user_service.get_user_details(user_id)
        if user:
            return f"User ID: {user.user_id}, Username: {user.username}"
        return "User not found."

class FinanceController:
    """Controller for managing income and financial data"""

    def __init__(self):
        income_repo = IncomeRepository()
        self.income_service = IncomeService(income_repo)

    def list_incomes(self, user_id: int):
        incomes = self.income_service.retrieve_incomes(user_id)
        if incomes:
            return [f"Income {inc.income_id}: Amount {inc.amount}, Category {inc.category}" for inc in incomes]
        return "No incomes recorded."

    def add_income(self, user_id: int, amount: float, category: str, date: str):
        self.income_service.add_income_entry(user_id, amount, category, date)
        return "Income entry added successfully."

# The controller layer provides an interface for the front-end or CLI to interact with the application's business logic, encapsulated in services.