from src.entities import User, Income, Expense
from src.repositories import UserRepository, IncomeRepository

class UserService:
    """Service Layer for User-related operations"""

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, username: str, password: str) -> User:
        # Normally would hash password, here represented simply
        hashed_password = hash_password(password)
        user = User(user_id=None, username=username, hashed_password=hashed_password)
        self.user_repo.add_user(user)
        return user

    def get_user_details(self, user_id: int) -> User:
        return self.user_repo.get_user_by_id(user_id)

class IncomeService:
    """Service Layer for Income-related operations"""

    def __init__(self, income_repo: IncomeRepository):
        self.income_repo = income_repo

    def retrieve_incomes(self, user_id: int):
        return self.income_repo.get_incomes_for_user(user_id)

    def add_income_entry(self, user_id: int, amount: float, category: str, date: str):
        income = Income(income_id=None, user_id=user_id, amount=amount, category=category, date=date)
        # Code to save income to database will be here

# Added mock function to illustrate password hashing

def hash_password(password: str) -> str:
    # Would normally use library like bcrypt to hash passwords
    return "hashed_" + password

# The service layer interacts with the repository and entities layers to encapsulate business logic, making it reusable and testable.