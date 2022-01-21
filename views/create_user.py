class CreateUserView:
    """Create user view."""
    def prompt_for_user(self):
        """Ask a username."""
        name = input('Username : ')
        if len(name) < 3:
            print('The Username must have at least 3 caracters')
            return None
        return name

    def prompt_for_password(self):
        """Ask a password."""
        password = input('Password : ')
        if len(password) < 4:
            print('The Password must have at least 4 caracters')
            return None
        return password
