class TaskManager:
    def __init__(self):
        """Initialize the task manager with an empty task list"""
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the task list"""
        if task not in self.tasks:
            self.tasks.append(task)

    def remove_task(self, task):
        """Remove an existing task from the task list"""
        if task in self.tasks:
            self.tasks.remove(task)

    def list_tasks(self):
        """Return the list of tasks"""
        return self.tasks

    def mark_completed(self, task):
        """Mark a task as completed"""
        if task in self.tasks:
            task.completed = True
