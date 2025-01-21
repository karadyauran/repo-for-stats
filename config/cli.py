class CommandLineInterface:
    def __init__(self, transaction_manager):
        self.transaction_manager = transaction_manager

    def prompt_for_transaction(self):
        """Collect inputs from the user for a new transaction."""
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        trans_type = input("Enter type (income/expense): ")
        
        return date, amount, category, description, trans_type
    
    def add_transaction(self):
        """Add a new transaction using user input."""
        transaction_data = self.prompt_for_transaction()
        self.transaction_manager.add_transaction(Transaction(*transaction_data))
    
    def display_options(self):
        """Display command options to the user."""
        print("1. Add Transaction")
        print("2. View Transactions") # This would trigger calling a corresponding method.
