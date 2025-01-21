import os
from dotenv import load_dotenv

class Settings:
    """
    Class to hold application configuration settings.
    """

    def __init__(self):
        # Load environment variables from a .env file
        load_dotenv(".env")
        
        # Initialize settings
        self.app_name = "Personal Finance Tracker"
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///finance_tracker.db')
        self.debug = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
        self.secret_key = os.getenv('SECRET_KEY', 'defaultsecret')

    def get_database_url(self):
        """
        Returns the database URL
        """
        return self.database_url

    def is_debug_mode(self):
        """
        Returns whether application is in debug mode
        """
        return self.debug

    def get_secret_key(self):
        """
        Returns the application secret key
        """
        return self.secret_key

    def app_info(self):
        """
        Returns a simple info about the application
        """
        return f"Application: {self.app_name}"

# Example usage
# This would typically be used in various parts of the application to access settings
# settings = Settings()
# db_url = settings.get_database_url()
# debug_mode = settings.is_debug_mode()