from .password_db import PasswordDb


class User:
    """User"""
    def __init__(self, name, password, path):
        """Has a name, a password, a path and an PasswordDB."""
        self.name = name
        self.password = password
        self.path = path
        self.password_db = PasswordDb()
        """a la place de PasswordDb mettre un chemin pour 
        vers dossier utilisateur a ouvrir avec pickle"""

    def __str__(self):
        """Representation of the user."""
        text = (f'User : {self.name}\n'
                f'Password : {self.password}\n')
        return text
