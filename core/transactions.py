class Transaction:
    def __init__(self, date, amount, category, description, trans_type):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description
        self.trans_type = trans_type.lower()

    def to_dict(self):
        """Convert Transaction object to dictionary."""
        return {
            'date': self.date,
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'type': self.trans_type
        }

class TransactionManager:
    def __init__(self, storage):
        self.storage = storage

    def add_transaction(self, transaction):
        transactions = self.storage.load_transactions()
        transactions.append(transaction.to_dict())
        self.storage.save_transactions(transactions)