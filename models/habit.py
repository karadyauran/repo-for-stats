from datetime import datetime

class Habit:
    def __init__(self, name, description, target_frequency):
        self.name = name
        self.description = description
        self.target_frequency = target_frequency  # e.g., "daily", "weekly"
        self.logs = []  # Store datetime entries when the habit is logged

    def log_habit(self):
        """Log the current date and time when the habit is completed."""
        self.logs.append(datetime.now())

    def get_streak(self):
        """Calculate the current streak based on log entries."""
        if not self.logs:
            return 0
        # Simplified streak calculation for demonstration
        # In real application, refine to consider exact target_frequency
        unique_days = {log.date() for log in self.logs}
        return len(unique_days)

    def to_dict(self):
        """Convert Habit object to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'target_frequency': self.target_frequency,
            'logs': [log.isoformat() for log in self.logs]
        }