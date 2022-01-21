from pathlib import Path
from models.user import User
from models.crypt import CreateRSAKeys
from .tools import create_folder, save_users


class CreateUser:
    """Class to create an user"""

    USER_FOLDER = 'usr'

    def __init__(self, view, users):
        """Has a view and a list of users."""
        self.view = view
        self.users = users

    def _user_name_available(function):
        """Verify if the username is already used.

        Args :
            - function : function that return a name (str)
        """
        def wrapper(self, *args, **kwargs):
            name = None
            while not name:
                name = function(self, *args, **kwargs)
                for user in self.users:
                    if name == user.name:
                        print("User name already used")
                        name = None
            return name
        return wrapper

    @_user_name_available
    def _get_user_name(self):
        """Get the user name. Function decorated to verify if the
        user name is not already used.

        Returns : 
            - name (str): the name chosen by the user
        """
        name = None
        while not name:
            name = self.view.prompt_for_user()
        return name

    def _get_user_password(self):
        """Get the user password.

        Returns:
            - password (str) : the password chosen by the user
        """
        password = None
        while not password:
            password = self.view.prompt_for_password()
        return password

    def _get_user_path(self, user_name):
        """Get the user path.

        Args:
            - user_name (str) : the user name

        Returns :
            - A path object (path)
        """
        return Path(self.USER_FOLDER, user_name)

    def _create_keys(self, path):
        """Create RSA keys and save them.

        Args:
            - path (Path) : the path to keys files
        """
        keys = CreateRSAKeys(path)
        public_key, private_key = keys.new_keys()
        keys.write_public_key(public_key)
        keys.write_private_key(private_key)

    def create_user(self):
        """Create an user."""
        user_name = self._get_user_name()
        user_password = self._get_user_password()
        user_path = self._get_user_path(user_name)
        create_folder(user_path) # comes from tools
        user = User(user_name, user_password, user_path)
        self._create_keys(user_path)
        self.users.append(user)
        save_users(self.users) # comes from tools
