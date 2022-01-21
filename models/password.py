from .crypt import LoadRSAKeys, Decrypt


class Password:
    """Password"""
    def __init__(self, name, password, user_path):
        """Has a name, a password and a path."""
        self.name = name
        self._password = password
        self._user_path = user_path # needed to get the private key

    @property
    def password(self):
        """Decrypt the password when trying to access it."""
        private_key = self._load_private_key()
        decrypter = Decrypt(self._password, private_key)
        return decrypter.decrypt()

    def _load_private_key(self):
        """Load the private key."""
        loader = LoadRSAKeys(self._user_path)
        return loader.load_private_key()

    def __str__(self):
        return f"{self.name} : {self.password}"

    def __repr__(self):
        return str(self)
