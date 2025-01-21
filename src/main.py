from src.controllers.finance_controller import FinanceController
from src.services.finance_service import FinanceService
from src.repositories.finance_repository import FinanceRepository

# Initialize repository, service, and controller
finance_repository = FinanceRepository()
finance_service = FinanceService(finance_repository)
finance_controller = FinanceController(finance_service)

# Main function to run some sample commands
if __name__ == '__main__':
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Entry")
        print("2. Remove Entry")
        print("3. Update Entry")
        print("4. Show All Entries")
        print("5. Show Total Income")
        print("6. Show Total Expenses")
        print("7. Show Balance")
        print("8. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            # Input entry details
            entry_id = input("Enter ID: ")
            name = input("Enter name: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            entry_type = input("Enter entry type (income/expense): ")
            date = input("Enter date (YYYY-MM-DD): ")
            print(finance_controller.add_entry(entry_id, name, amount, category, entry_type, date))

        elif choice == '2':
            entry_id = input("Enter ID to remove: ")
            print(finance_controller.remove_entry(entry_id))

        elif choice == '3':
            # Input updated entry details
            entry_id = input("Enter ID: ")
            name = input("Enter name: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            entry_type = input("Enter entry type (income/expense): ")
            date = input("Enter date (YYYY-MM-DD): ")
            print(finance_controller.modify_entry(entry_id, name, amount, category, entry_type, date))

        elif choice == '4':
            print("\nAll Entries:")
            print(finance_controller.show_all_entries())

        elif choice == '5':
            print(finance_controller.get_total_income())

        elif choice == '6':
            print(finance_controller.get_total_expenses())

        elif choice == '7':
            print(finance_controller.get_balance())

        elif choice == '8':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")