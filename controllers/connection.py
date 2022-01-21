class Connection:
    """Class to connect an user to its account."""
    def __init__(self, view, users):
        """Has a view and a list of users."""
        self.view = view
        self.users = users

    def connect_to_account(self):
        """Connect an user to its account.

        Returns:
            - user (User) : the user or None
        """
        asked_user = self.view.prompt_for_user()
        asked_password = self.view.prompt_for_password()
        for user in self.users:
            if asked_user == user.name and asked_password == user.password:
                print(user)
                return user
        print("Invalid username or password")
        return None
