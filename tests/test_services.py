import unittest
from unittest.mock import MagicMock
from src.services import UserService, IncomeService
from src.entities import User, Income
from src.repositories import UserRepository, IncomeRepository

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()
        self.user_repo.add_user = MagicMock()
        self.user_repo.get_user_by_id = MagicMock(return_value=User(user_id=1, username="test_user", hashed_password="hashed_pwd"))
        self.user_service = UserService(self.user_repo)

    def test_register_user(self):
        user = self.user_service.register_user("test_user", "password")
        self.user_repo.add_user.assert_called_once()
        self.assertEqual(user.username, "test_user")

    def test_get_user_details(self):
        user = self.user_service.get_user_details(1)
        self.user_repo.get_user_by_id.assert_called_once_with(1)
        self.assertEqual(user.username, "test_user")

class TestIncomeService(unittest.TestCase):
    def setUp(self):
        self.income_repo = IncomeRepository()
        self.income_repo.get_incomes_for_user = MagicMock(return_value=[Income(income_id=1, user_id=1, amount=500.0, category="Freelance", date="2023-01-01")])
        self.income_service = IncomeService(self.income_repo)

    def test_retrieve_incomes(self):
        incomes = self.income_service.retrieve_incomes(1)
        self.income_repo.get_incomes_for_user.assert_called_once_with(1)
        self.assertEqual(len(incomes), 1)
        self.assertEqual(incomes[0].amount, 500.0)

if __name__ == '__main__':
    unittest.main()

# This test suite checks the business logic handled by service layers using mocks for the underlying data repository interactions.