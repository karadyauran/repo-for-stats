# services/authentication_service.py

from data.storage import UserStorage
import hashlib

class AuthenticationService:
    """
    Service for managing user authentication.
    """
    def __init__(self, user_storage: UserStorage):
        self.user_storage = user_storage

    def hash_password(self, password: str) -> str:
        """
        Apply hash function for password security.
        :return: Hashed password.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username: str, password: str) -> bool:
        """
        Register a new user with hashed password.
        :return: Boolean indicating success or failure.
        """
        hashed_password = self.hash_password(password)
        if not self.user_storage.get_user(username):
            return self.user_storage.add_user(username, hashed_password)
        return False

    def authenticate_user(self, username: str, password: str) -> bool:
        """
        Authenticate user login attempt by checking password hash.
        :return: Boolean indicating success or failure.
        """
        user_record = self.user_storage.get_user(username)
        if user_record:
            stored_password_hash = user_record[2]  # assuming password is the third field
            return stored_password_hash == self.hash_password(password)
        return False

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """
        Change a user's password after verifying old password.
        :return: Boolean indicating success or failure.
        """
        if self.authenticate_user(username, old_password):
            new_hashed_password = self.hash_password(new_password)
            self.user_storage.db_manager.execute_query(
                "UPDATE users SET password = ? WHERE username = ?",
                (new_hashed_password, username)
            )
            return True
        return False