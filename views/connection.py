class ConnectionView:
    """Connection view."""
    def prompt_for_user(self):
        """Ask a username"""
        name = input('Username : ')
        return name

    def prompt_for_password(self):
        """Ask a password."""
        password = input('Password : ')
        return password
