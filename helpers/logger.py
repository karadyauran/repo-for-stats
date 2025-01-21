import logging
import os

class Logger:
    """
    A simple logger wrapper for the application.
    """

    def __init__(self, log_level=logging.INFO):
        # Determine log file path
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        log_file = os.path.join(log_dir, 'app.log')
        
        # Set up logging configuration
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # Create file handler which logs even debug messages
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # Create console handler with a higher log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        """
        Log an informational message.
        """
        self.logger.info(message)

    def warning(self, message):
        """
        Log a warning message.
        """
        self.logger.warning(message)

    def error(self, message):
        """
        Log an error message.
        """
        self.logger.error(message)

    def debug(self, message):
        """
        Log a debug message.
        """
        self.logger.debug(message)

    def critical(self, message):
        """
        Log a critical message.
        """
        self.logger.critical(message)

# The Logger can be instantiated and used across different
# components of the application to log various events and errors.