class PasswordView:
    """Password view."""
    def prompt_for_password_length(self):
        """Ask the number of characters that the password conatains."""
        length = input("Number of characters : ")
        try:
            int(length)
        except ValueError:
            return False
        return int(length)

    def prompt_for_password_name(self):
        """Ask a name for the password."""
        name = input("Name of the password : ")
        if not name:
            return None
        return name

    def prompt_for_password(self):
        """Ask a password."""
        password = input('Password : ')
        return password

    def accept_password(self, name, password):
        """Ask if the password agrees to the user."""
        print("\n---------------------------------------------------------\n",
              "Password generated :\n",
             f"    Name : {name}",
             f"    Password : {password}",
              "\n---------------------------------------------------------\n",
              "Is the password good for you ? :",
              sep = "\n")
        result = input('y/n : ').lower()
        decline = ["n", "no"]
        if result in decline:
            return False
        return True
