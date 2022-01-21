from .generate_password import GeneratePassword
from .password_db import PasswordDBController


class Account:
    """Account controller."""
    def __init__(self, views):
        """Has views, an user, GeneratePassword and PasswordDBController.

        Args:
            - views (ViewsManager) : a class ViewsManager
        """
        self.views = views
        self._user = None
        self.generate_password = GeneratePassword(self.password_view)
        self.password_db = PasswordDBController(self.password_db_view)

    @property
    def user(self):
        """Property of self._user"""
        return self._user

    @user.setter
    def user(self, user):
        """Propery setter. When it set the user it set it too 
        to self.generate_password and self.password_db.

        Args:
            - user (User) : User or None
        """
        self._user = user
        self.generate_password.user = user
        self.password_db.user = user

    @property
    def account_view(self):
        """Simplifies the use of self.views.account_view"""
        return self.views.account_view

    @property
    def password_view(self):
        """Simplifies the use of self.views.password_view"""
        return self.views.password_view

    @property
    def password_db_view(self):
        """Simplifies the use of self.views.password_db_view"""
        return self.views.password_db_view

    def account_manager(self):
        """Account interface manager."""

        result = self.account_view.display_interface()
        if result == '0':
            self.generate_password.random_password()
        if result == "1":
            self.generate_password.manual_password()
        if result == "2":
            self.password_db_view.show_all_passwords(self.user)
        if result == '3':
            name = self.password_view.prompt_for_password_name()
            passwords_found = self.password_db.get_password_by_name(name)
            self.password_db_view.show_password_found(passwords_found)

        if result == '9':
            self.user = None
