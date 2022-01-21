class AccountView:
    """Account interface view."""
    def display_interface(self):
        """Display the account interface and get the user's choice."""
        print("Create random password(0)  Add password(1)  Access password(2)"
              "  Search password(3)  Exit(9)")
        result = input()
        if result not in ["0", "1", "2", "3", "9"]:
            return None
        return result
