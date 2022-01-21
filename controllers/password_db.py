class PasswordDBController:
    """Password database controller"""
    def __init__(self, view):
        """Has a view and an user"""
        self.view = view
        self.user = None

    @property
    def data(self):
        """Simplifies the use of self.user.password.data"""
        return self.user.password_db.data

    def get_password_by_name(self, name):
        """Get each Password whose have this name.

        Args:
            - name (str) : the name of the password

        Returns:
            - password_found (list) : the list of passwords found
        """
        passwords_found = []
        for password in self.data:
            if name == password.name:
                passwords_found.append(password)
        return passwords_found

    def remove(self, name):

        remove_list = []
        for password in self.data:
            if password.name == name:
                remove_list.append(password)
        if len(remove_list) > 1:
            choices = self.view.prompt_for_choices(remove_list)
            for choice in choices:
                del remove_list[choice]
        else:
            if remove_list:
                del remove_list[0]
