class PasswordDBView:
    """PasswordDB view."""
    def show_password_found(self, passwords_found):
        """Display passwords found."""
        print("\n---------------------------------------------------------\n")
        if len(passwords_found) > 1:
            print(f"{len(passwords_found)} passwords trouvés :")
        else:
            print(f"{len(passwords_found)} password trouvé :")
        print()
        for password in passwords_found:
            print(f"{password.name} : {password.password}")
        print("\n---------------------------------------------------------\n")

    def show_all_passwords(self, user):
        """Display all passwords."""
        print("\n---------------------------------------------------------\n")
        for password in user.password_db:
            print(f"{password.name} : {password.password}")
        print("\n---------------------------------------------------------\n")

    def prompt_for_choices(self, remove_list):
        """Ask choices to remove in PasswordDB."""
        choices = []
        for index, password in enumerate(remove_list):
            print(f'({index}) {password}')
        print("Enter the numbers you want to delete, "
              "separated by commas")
        choice = input()
        try:
            choices.extend([int(elt) for elt in choice.split(',')])
        except ValueError:
            print('choices must be integer')
            choices = []
        return choices
