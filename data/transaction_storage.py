import json

class TransactionStorage:
    def __init__(self, filename='finance_data.json'):
        self.filename = filename

    def load_transactions(self):
        """Load transactions from JSON file."""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_transactions(self, transactions):
        """Save transactions to JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(transactions, file, indent=4)
