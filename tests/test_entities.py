import unittest
from src.entities import User, Income, Expense, Budget, FinancialGoal

class TestEntities(unittest.TestCase):

    def setUp(self):
        # Initial setup for tests if needed
        self.user = User(user_id=1, username="test_user", hashed_password="hashed_pwd")
        self.income = Income(income_id=1, user_id=1, amount=1000.0, category="Salary", date="2023-01-01")
        self.expense = Expense(expense_id=1, user_id=1, amount=200.0, category="Food", date="2023-01-01")
        self.budget = Budget(budget_id=1, user_id=1, category="Monthly", limit=1500.0, period="monthly")
        self.goal = FinancialGoal(goal_id=1, user_id=1, name="Vacation", target_amount=1000.0, current_amount=500.0, due_date="2023-12-01")

    def test_user_entity(self):
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.hashed_password, "hashed_pwd")

    def test_income_entity(self):
        self.assertEqual(self.income.amount, 1000.0)
        self.assertEqual(self.income.category, "Salary")

    def test_expense_entity(self):
        self.assertEqual(self.expense.amount, 200.0)
        self.assertEqual(self.expense.category, "Food")

    def test_budget_entity(self):
        self.assertEqual(self.budget.limit, 1500.0)
        self.assertEqual(self.budget.period, "monthly")

    def test_goal_entity(self):
        self.assertEqual(self.goal.target_amount, 1000.0)
        self.assertEqual(self.goal.current_amount, 500.0)

if __name__ == '__main__':
    unittest.main()

# The test suite ensures that the entity classes are working as expected, checking property assignments and initial values.