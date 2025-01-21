from src.core.task_manager import TaskManager

class TaskOperations:
    def __init__(self, task_manager, console_interface):
        """Initialize with task manager and console interface"""
        self.task_manager = task_manager
        self.console = console_interface

    def execute_add_task(self):
        """Prompt the user to add a new task"""
        description = self.console.get_user_input("Enter task description: ")
        new_task = Task(description)
        self.task_manager.add_task(new_task)

    def execute_remove_task(self):
        """Prompt the user to remove a task"""
        self.console.display_task_list(self.task_manager.list_tasks())
        index = int(self.console.get_user_input("Enter task number to remove: ")) - 1
        if 0 <= index < len(self.task_manager.tasks):
            self.task_manager.remove_task(self.task_manager.tasks[index])
        else:
            self.console.invalid_option()
