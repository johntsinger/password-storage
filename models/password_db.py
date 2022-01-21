from collections import UserList
from .password import Password


class PasswordDb(UserList):
    """Password data base."""
    def __init__(self):
        """Initialize the construtor of UserList."""
        super().__init__()
        self.data = []

    def append(self, object):
        """Controls that only a Password object is added."""
        if not isinstance(object, Password):
            return ValueError("You can only add password")
        return super().append(object)
