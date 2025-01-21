from models.habit import Habit
import json

class HabitManager:
    def __init__(self, storage_file='habits_data.json'):
        self.storage_file = storage_file
        self.habits = self.load_habits()

    def load_habits(self):
        """Load habits from storage file."""
        try:
            with open(self.storage_file, 'r') as file:
                habits_data = json.load(file)
                return [Habit(**habit) for habit in habits_data]
        except FileNotFoundError:
            return []

    def save_habits(self):
        """Save the current list of habits to the storage file."""
        with open(self.storage_file, 'w') as file:
            json.dump([habit.to_dict() for habit in self.habits], file, indent=4)

    def add_habit(self, habit):
        """Add a new habit and save."""
        self.habits.append(habit)
        self.save_habits()

    def remove_habit(self, name):
        """Remove a habit by name and update storage."""
        self.habits = [habit for habit in self.habits if habit.name != name]
        self.save_habits()