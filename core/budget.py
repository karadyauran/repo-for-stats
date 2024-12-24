class Budget:
    """
    A class to represent a budget for different financial categories.
    """

    def __init__(self):
        """Initialize an empty budget dictionary."""
        self.budget_dict = {}

    def set_budget(self, category: str, amount: float):
        """Set or update the budget for a specific category."""
        self.budget_dict[category] = amount

    def get_budget(self, category: str) -> float:
        """Retrieve the budget set for a specific category."""
        return self.budget_dict.get(category, 0.0)

    def remove_budget(self, category: str):
        """Remove the budget for a specific category, if it exists."""
        if category in self.budget_dict:
            del self.budget_dict[category]
