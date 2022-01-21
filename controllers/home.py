from .connection import Connection
from .create_user import CreateUser


class Home:
    """Home controller"""
    def __init__(self, views, users):
        """Has views, a list of users, Connection and
        CreateUser.

        Args:
            - views (ViewsManager) : the ViewsManager
            - users (list) : a list of users
        """
        self.views = views
        self.users = users
        self._connection = Connection(self.connection_view, self.users)
        self._create_user = CreateUser(self.create_user_view, self.users)

    @property
    def home_view(self):
        """Simplifies the use of self.views.home_view"""
        return self.views.home_view

    @property
    def connection_view(self):
        """Simplifies the use of self.views.connection_view"""
        return self.views.connection_view

    @property
    def create_user_view(self):
        """Simplifies the use of self.views.create_user_view"""
        return self.views.create_user_view

    def home_manager(self):
        """Home interface manager.

        Returns:
            - user (User) : the user
        """
        result = self.home_view.display_interface()
        if result == '0':
            self._create_user.create_user()
        if result == '1':
            user = self._connection.connect_to_account()
            return user
        if result == '9':
            exit()
