from src.repositories.finance_repository import FinanceRepository
from src.models.finance import FinanceEntry

class FinanceService:
    """ Service layer for business logic operations on finance entries. """

    def __init__(self, repository: FinanceRepository):
        self.repository = repository  # Injecting dependency for data access

    def create_entry(self, entry_id, name, amount, category, entry_type, date):
        """ Business logic to create a new finance entry. """
        new_entry = FinanceEntry(entry_id, name, amount, category, entry_type, date)
        self.repository.add_entry(new_entry)

    def delete_entry(self, entry_id):
        """ Business logic to delete a finance entry. """
        self.repository.remove_entry(entry_id)

    def update_entry(self, entry_id, name, amount, category, entry_type, date):
        """ Business logic to update an existing finance entry. """
        updated_entry = FinanceEntry(entry_id, name, amount, category, entry_type, date)
        self.repository.update_entry(updated_entry)

    def calculate_total_income(self):
        """ Calculate total income from the entries. """
        entries = self.repository.list_entries()
        return sum(entry.amount for entry in entries if entry.entry_type == 'income')

    def calculate_total_expense(self):
        """ Calculate total expenses from the entries. """
        entries = self.repository.list_entries()
        return sum(entry.amount for entry in entries if entry.entry_type == 'expense')

    def balance(self):
        """ Calculate the balance (total income - total expenses). """
        return self.calculate_total_income() - self.calculate_total_expense()

    def list_all_entries(self):
        """ Retrieve all finance entries. """
        return self.repository.list_entries()