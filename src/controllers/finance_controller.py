from src.services.finance_service import FinanceService

class FinanceController:
    """ Controller for handling the input/output interaction with the finance services. """

    def __init__(self, service: FinanceService):
        self.service = service

    def add_entry(self, entry_id, name, amount, category, entry_type, date):
        """ Handle adding a new finance entry. """
        try:
            self.service.create_entry(entry_id, name, amount, category, entry_type, date)
            return "Entry added successfully."
        except Exception as e:
            return str(e)

    def remove_entry(self, entry_id):
        """ Handle removing an existing finance entry. """
        try:
            self.service.delete_entry(entry_id)
            return "Entry removed successfully."
        except Exception as e:
            return str(e)

    def modify_entry(self, entry_id, name, amount, category, entry_type, date):
        """ Handle modifying an existing finance entry. """
        try:
            self.service.update_entry(entry_id, name, amount, category, entry_type, date)
            return "Entry updated successfully."
        except Exception as e:
            return str(e)

    def get_balance(self):
        """ Handle calculating current financial balance. """
        return f"Current Balance: {self.service.balance()}"

    def show_all_entries(self):
        """ Display all finance entries to the user. """
        entries = self.service.list_all_entries()
        if not entries:
            return "No entries available."
        return '\n'.join([entry.display_entry() for entry in entries])

    def get_total_income(self):
        """ Handle calculating the total income. """
        return f"Total Income: {self.service.calculate_total_income()}"

    def get_total_expenses(self):
        """ Handle calculating the total expenses. """
        return f"Total Expenses: {self.service.calculate_total_expense()}"