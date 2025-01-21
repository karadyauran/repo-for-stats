class ConsoleInterface:
    def display_message(self, message):
        """Display a message to the console"""
        print(message)

    def get_user_input(self, prompt):
        """Get user input from the console with a prompt"""
        return input(prompt)

    def display_task_list(self, tasks):
        """Display a list of tasks"""
        for index, task in enumerate(tasks, 1):
            status = "Completed" if task.completed else "Pending"
            print(f"{index}. {task.description} [Status: {status}]")

    def invalid_option(self):
        """Notify user of invalid option"""
        print("Invalid option. Please try again.")
