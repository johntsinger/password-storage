from .config import ConfigController
from models.crypt import LoadRSAKeys, Encrypt
from models.password import Password
from models.random_password import RandomPassword


class GeneratePassword:
    """Generate password."""
    def __init__(self, view):
        """Has a view, an user and ConfigController."""
        self.view = view
        self.user = None
        self.config = ConfigController()

    def encrypt_password(self, password):
        """Encrypt the password.

        Args:
            - password (str) : the password to encrypt

        Returns:
            - the encrypted password
        """
        loader = LoadRSAKeys(self.user.path)
        public_key = loader.load_public_key()
        encryptor = Encrypt(password, public_key)
        return encryptor.encrypt()

    def random_password(self):
        """Generate a random password."""
        name = self.view.prompt_for_password_name()
        length = self.view.prompt_for_password_length()
        self.config.run()
        answer = False
        instance = RandomPassword(length, self.config.values)
        while not answer:
            password = instance.create_password()
            answer = self.view.accept_password(name, password)

        encrypted_password = self.encrypt_password(password)
        password = Password(name, encrypted_password, self.user.path)
        self.user.password_db.append(password)

    def manual_password(self):
        """Create password manually."""
        name = self.view.prompt_for_password_name()
        if not name:
            name = 'new_password'
        answer = False
        while not answer:
            password = self.view.prompt_for_password()
            answer = self.view.accept_password(name, password)

        encrypted_password = self.encrypt_password(password)
        password = Password(name, encrypted_password, self.user.path)
        self.user.password_db.append(password)
