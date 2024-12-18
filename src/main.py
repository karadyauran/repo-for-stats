from src.controllers import UserController, FinanceController
from data.data_handler import setup_database

# Entry point for running the console application

def main():
    setup_database()  # Initialize database schema
    user_controller = UserController()
    finance_controller = FinanceController()

    while True:
        print("\n=== Personal Finance Manager ===")
        print("1. Register User")
        print("2. View User Details")
        print("3. Add Income")
        print("4. View Incomes")
        print("0. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(user_controller.create_user(username, password))
        elif choice == "2":
            user_id = int(input("Enter user ID: "))
            print(user_controller.get_user_info(user_id))
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            amount = float(input("Enter income amount: "))
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            print(finance_controller.add_income(user_id, amount, category, date))
        elif choice == "4":
            user_id = int(input("Enter user ID: "))
            print("\n".join(finance_controller.list_incomes(user_id)))
        elif choice == "0":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == '__main__':
    main()

# This serves as the command interface for the console app, facilitating user interaction and managing the flow of actions.