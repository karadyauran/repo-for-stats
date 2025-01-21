from src.core.task_manager import TaskManager
from src.adapters.console_interface import ConsoleInterface
from src.usecases.task_operations import TaskOperations
from src.infrastructure.file_handler import FileHandler

# Initialize required components
file_handler = FileHandler('tasks.json')
task_manager = TaskManager()
console = ConsoleInterface()
operations = TaskOperations(task_manager, console)

# Load existing tasks
existing_tasks = file_handler.load_tasks()
for task_info in existing_tasks:
    task_manager.add_task(Task(**task_info))

# Main application loop
while True:
    console.display_message("1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
    choice = console.get_user_input("Select an option: ")
    if choice == '1':
        operations.execute_add_task()
    elif choice == '2':
        operations.execute_remove_task()
    elif choice == '3':
        console.display_task_list(task_manager.list_tasks())
    elif choice == '4':
        file_handler.save_tasks(task_manager.list_tasks())
        break
    else:
        console.invalid_option()