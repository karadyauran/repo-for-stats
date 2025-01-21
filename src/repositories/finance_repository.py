from src.models.finance import FinanceEntry

class FinanceRepository:
    """ A repository class to handle storage and retrieval of financial entries. """

    def __init__(self):
        # Initialize an internal dictionary to store finance entries by ID
        self._entries = {}

    def add_entry(self, finance_entry: FinanceEntry):
        """ Add a new finance entry to the repository. """
        if finance_entry.entry_id in self._entries:
            raise ValueError("An entry with this ID already exists.")
        self._entries[finance_entry.entry_id] = finance_entry

    def remove_entry(self, entry_id):
        """ Remove an existing finance entry from the repository by ID. """
        if entry_id in self._entries:
            del self._entries[entry_id]
        else:
            raise KeyError("Entry ID not found.")

    def get_entry(self, entry_id):
        """ Retrieve a finance entry by its ID. """
        if entry_id in self._entries:
            return self._entries[entry_id]
        else:
            raise KeyError("Entry ID not found.")

    def update_entry(self, finance_entry: FinanceEntry):
        """ Update an existing finance entry. """
        if finance_entry.entry_id in self._entries:
            self._entries[finance_entry.entry_id] = finance_entry
        else:
            raise KeyError("Entry ID not found.")

    def list_entries(self):
        """ Return a list of all finance entries. """
        return list(self._entries.values())

    def count_entries(self):
        """ Get the current count of finance entries. """
        return len(self._entries)