from pathlib import Path
import rsa


class KeysPath:
    """Class to get keys path."""

    PUBLIC_KEY_FILE = 'rsa_public_key.pem'
    PRIVATE_KEY_FILE = 'rsa_private_key.pem'

    def __init__(self, user_path):
        self.user_path = user_path

    @property
    def path_public_key(self):
        return self.user_path / self.PUBLIC_KEY_FILE

    @property
    def path_private_key(self):
        return self.user_path / self.PRIVATE_KEY_FILE


class CreateRSAKeys(KeysPath):
    """Create RSA keys and save them."""
    def __init__(self, user_path):
        super().__init__(user_path)
        
    def new_keys(self):
        """Create RSA public key and RSA private key."""
        return rsa.newkeys(4096, poolsize=8)

    def write_public_key(self, public_key):
        """Write public key in user folder."""
        key_pem = public_key.save_pkcs1()
        with open(self.path_public_key, 'wb') as file:
            file.write(key_pem)

    def write_private_key(self, private_key):
        """Write private key in user folder."""
        key_pem = private_key.save_pkcs1()
        with open(self.path_private_key, 'wb') as file:
            file.write(key_pem)


class LoadRSAKeys(KeysPath):
    """Load RSA keys."""
    def __init__(self, user_path):
        super().__init__(user_path)

    def load_public_key(self):
        """Load RSA public key."""
        with open(self.path_public_key, 'rb') as file:
            keydata = file.read()
        return rsa.PublicKey.load_pkcs1(keydata)

    def load_private_key(self):
        """Load RSA private key."""
        with open(self.path_private_key, 'rb') as file:
            keydata = file.read()
        return rsa.PrivateKey.load_pkcs1(keydata)


class Encrypt:
    """Encrypt."""
    def __init__(self, message, public_key):
        self.message = message
        self.public_key = public_key

    def encrypt(self):
        """Encrypt the message with the public key."""
        return rsa.encrypt(self.message.encode(), self.public_key)


class Decrypt:
    """Decrypt."""
    def __init__(self, message, private_key):
        self.message = message
        self.private_key = private_key

    def decrypt(self):
        """Decrypt the message whith the private key."""
        return rsa.decrypt(self.message, self.private_key).decode()
         