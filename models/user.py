class User:
    """
    A class representing a user in the finance tracker application.
    """

    def __init__(self, user_id, username, email, password_hash):
        """
        Initialize a User with basic information.

        :param user_id: Unique identifier for the user.
        :param username: The username of the user.
        :param email: Email address of the user.
        :param password_hash: Hashed user password.
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def get_user_id(self):
        """
        Returns the user ID.
        """
        return self.user_id

    def get_username(self):
        """
        Returns the username.
        """
        return self.username

    def get_email(self):
        """
        Returns the user's email address.
        """
        return self.email

    def check_password(self, password):
        """
        Checks the entered password against the stored password hash.

        :param password: Plain text password.
        :return: Boolean indicating if the password matches.
        """
        # Password check logic goes here, matching plain password with password hash
        return self._validate_password_hash(password)

    def _validate_password_hash(self, password):
        """
        Private method to validate password hash. Implement hash check logic here.

        :param password: The plain text password to check.
        :return: Boolean if password matches the stored hash or not.
        """
        # A placeholder function for password hash validation logic.
        # Example: return bcrypt.checkpw(password.encode(), self.password_hash)
        raise NotImplementedError("Hash validation must be implemented")