class HomeView:
    """Home interface view."""
    def display_interface(self):
        """Display the connection interface and get the user's choice."""
        print("Create account(0)  Connection(1)  Exit(9)")
        result = input()
        if result not in ["0", "1", "9"]:
            return None
        return result
