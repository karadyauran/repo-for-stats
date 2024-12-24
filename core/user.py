class User:
    """
    A class to represent a user in the Personal Finance Tracker.
    """
    
    def __init__(self, username: str, password: str):
        """Initialize a user with a username and password."""
        self.username = username
        self._password = password  # Password should ideally be hashed.
    
    def authenticate(self, entered_password: str) -> bool:
        """Method to authenticate user based on entered password."""
        return self._password == entered_password

    def change_password(self, new_password: str):
        """Method to change the user's password."""
        self._password = new_password
    
    @property
    def user_details(self) -> dict:
        """Return user details excluding the password."""
        return {'username': self.username}
