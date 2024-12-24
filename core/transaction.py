from datetime import datetime

class Transaction:
    """
    A class to represent a financial transaction.
    """

    def __init__(self, amount: float, category: str, description: str = ""):
        """Initialize a transaction with amount, category, description, and timestamp."""
        self.amount = amount
        self.category = category
        self.description = description
        self.timestamp = datetime.now()
    
    def to_dict(self) -> dict:
        """Convert transaction details to a dictionary format."""
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'timestamp': self.timestamp.isoformat()
        }
