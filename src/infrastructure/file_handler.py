import json

class FileHandler:
    def __init__(self, filename):
        """Initialize with the file name for task storage"""
        self.filename = filename

    def load_tasks(self):
        """Load tasks from the file"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self, tasks):
        """Save tasks to the file"""
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in tasks], file, indent=4)
