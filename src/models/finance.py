class FinanceEntry:
    """ A class to represent a financial entry, including income and expenses. """

    def __init__(self, entry_id, name, amount, category, entry_type, date):
        # Ensure entry_id is unique for each financial entry
        self.entry_id = entry_id  
        self.name = name
        self.amount = amount
        self.category = category  # Category like 'utilities', 'salary', 'entertainment'
        self.entry_type = entry_type  # Can be either 'income' or 'expense'
        self.date = date  # Date of the transaction

    def update_amount(self, new_amount):
        """ Update the amount of a financial entry. """
        self.amount = new_amount

    def update_category(self, new_category):
        """ Update the category of a financial entry. """
        self.category = new_category

    def change_type(self, new_type):
        """ Change the type of the entry, e.g., from 'income' to 'expense'. """
        if new_type in ['income', 'expense']:
            self.entry_type = new_type
        else:
            raise ValueError("entry_type must be 'income' or 'expense'")

    def display_entry(self):
        """ Return a string representation of the financial entry. """
        return f"[ID: {self.entry_id}] {self.name}: {self.amount} ({self.category} - {self.entry_type}) on {self.date}"
    
    def __eq__(self, other):
        """ Overriding equality operator to compare two finance entries. """
        return isinstance(other, FinanceEntry) and self.entry_id == other.entry_id

    def __hash__(self):
        """ Provide a hash function to ensure FinanceEntry can be used in sets or as keys in dictionaries. """
        return hash(self.entry_id)
