from .password import PasswordView
from .connection import ConnectionView
from .create_user import CreateUserView
from .home import HomeView
from .account import AccountView
from .password_db import PasswordDBView


class ViewsManager:
    """View manager."""
    def __init__(self):
        """Initilize view intances."""
        self.connection_view = ConnectionView()
        self.create_user_view = CreateUserView()
        self.home_view = HomeView()
        self.account_view = AccountView()
        self.password_view = PasswordView()
        self.password_db_view = PasswordDBView()
