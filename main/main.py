from data.transaction_storage import TransactionStorage
from core.transactions import TransactionManager, Transaction
from config.cli import CommandLineInterface


def main():
    storage = TransactionStorage()
    transaction_manager = TransactionManager(storage)
    cli = CommandLineInterface(transaction_manager)
    
    while True:
        cli.display_options()
        choice = input("Choose an option: ")
        
        if choice == '1':
            cli.add_transaction()
        elif choice == '2':
            transactions = storage.load_transactions()
            for t in transactions:
                print(t)
        elif choice.lower() == 'exit':
            break

if __name__ == "__main__":
    main()
